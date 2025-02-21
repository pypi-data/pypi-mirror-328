from __future__ import annotations

import argparse
import asyncio
import hashlib
import ssl
import time
from contextlib import AsyncExitStack
from pathlib import Path
from traceback import format_exc
from typing import Any, ClassVar, Dict, List
import yaml
import aiohttp
import certifi
import dask.dataframe as dd
import pandas as pd
import uvloop
from aiohttp import ClientSession
from aiohttp.http_exceptions import TransferEncodingError
from aiohttp.client_exceptions import ClientPayloadError
from os import cpu_count
from pydantic import BaseModel, ConfigDict, Field, computed_field

from wombat.multiprocessing.models import Prop, RequiresProps, ResultTaskPair
from wombat.multiprocessing.qpool import Orchestrator, Worker
from wombat.multiprocessing.tasks import RetryableTask

from pydantic_partial import create_partial_model
# from foundry.transforms import Dataset

BASE_API_URL = "https://ghoapi.azureedge.net/api"

class BHIVEException(Exception):
    """Base exception for bhive things."""
    pass

class EmptyDataPullException(BHIVEException):
    def __init__(self, url: str, indicator: str) -> None:
        self.url = url
        self.indicator = indicator
        super().__init__(f"Received no data when pulling {self.indicator} from {self.url}")

class TransferInterruptException(BHIVEException):
    def __init__(self, url: str, indicator: str) -> None:
        self.url = url
        self.indicator = indicator
        super().__init__(f"Transfer interrupted when pulling {self.indicator} from {self.url}")

class AsyncFetchUrlTask(RetryableTask, RequiresProps):
    """Task for asynchronous URL fetching."""
    action: str = "async_fetch_url"
    requires_props: List[str] = ["aiohttp_session"]

def compute_sha1(path: Path) -> hashlib._hashlib.HASH:
    sha1sum = hashlib.sha1()
    with open(path, "rb") as source:
        while block := source.read(2**16):
            sha1sum.update(block)
    return sha1sum

###############################################################################
# Indicator Data Models & State Transitions
###############################################################################

class ParametrizedIndicator(BaseModel):
    """
    Represents an indicator from the WHO GHO API with injected parameters
    (download URL and output path). State: PARAMETRIZED (ready for acquisition)
    """
    model_config = ConfigDict(populate_by_name=True)
    code: str = Field(alias="IndicatorCode")
    name: str = Field(alias="IndicatorName")
    url: str
    language: str = Field(alias="Language", default="EN")
    output_path: Path

# Raw API responses are missing the URL/output_path. Use a partial model.
UnparametrizedIndicator = create_partial_model(
    ParametrizedIndicator,
    "url",
    "output_path"
)

class UnparametrizedIndicatorList(BaseModel):
    """
    Represents a list of raw indicators from the WHO GHO API,
    prior to parameter injection.
    """
    url: ClassVar[str] = f"{BASE_API_URL}/Indicator/"
    context: ClassVar[str] = Field(alias="@odata.context")
    value: List[UnparametrizedIndicator]


class ParametrizedIndicatorList(BaseModel):
    """
    Represents a list of parametrized indicators, ready for acquisition.
    """
    url: ClassVar[str] = f"{BASE_API_URL}/Indicator/"
    context: ClassVar[str] = Field(alias="@odata.context")
    value: List[ParametrizedIndicator]

class ConcreteIndicator(ParametrizedIndicator):
    """
    Represents an indicator that has been downloaded.
    State: CONCRETE (acquired)
    """
    @computed_field
    @property
    def sha1(self) -> str:
        return compute_sha1(self.output_path).hexdigest()

    @computed_field
    @property
    def exists(self) -> bool:
        return self.output_path.exists()

###############################################################################
# Helper Functions for Indicator State Transitions
###############################################################################

async def fetch_raw_indicators() -> UnparametrizedIndicatorList:
    """Fetch raw (unparametrized) indicators from the WHO GHO API."""
    try:
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context)) as session:
            async with session.get(f"{BASE_API_URL}/Indicator/") as resp:
                raw = await resp.json()
        return UnparametrizedIndicatorList(**raw)
    except Exception:
        print(format_exc())
        raise

def inject_indicator_parameters(
    datasets: Dict[str, UnparametrizedIndicatorList], output_root: Path
) -> Dict[str, ParametrizedIndicatorList]:
    """
    Convert raw indicators into parametrized indicators by injecting the download URL
    and the output file path.
    """
    results = {}
    # Rewrite as for loop so we can mkdir each dataset_dir
    for dataset_name, dataset in datasets.items():
        dataset_dir = output_root / dataset_name
        dataset_dir.mkdir(exist_ok=True)
        results[dataset_name] = ParametrizedIndicatorList(
            value=[
                ParametrizedIndicator(
                    code=indicator.code,
                    name=indicator.name,
                    url=f"{BASE_API_URL}/{indicator.code}",
                    output_path=dataset_dir / f"{indicator.code}.csv",
                )
                for indicator in dataset.value
            ]
        )
    return results

###############################################################################
# Asynchronous Download Task
###############################################################################

async def async_fetch_url(
    worker: Worker,
    dataset_name: str,
    indicator_name: str,
    url: str,
    output_path: Path,
    force: bool,
    props: Dict[str, Prop]
) -> Any:
    """
    Download the indicator data from the provided URL and save it to output_path.
    If force is True, download regardless of file existence.
    This transitions the indicator from parametrized to concrete.
    """
    status: Optional[int] = None
    exception: Optional[Exception] = None
    result: Optional[pd.DataFrame] = None
    if output_path.exists() and not force:
        df = pd.read_csv(output_path)
        status, exception, result = 200, None, df

    session_prop: Prop = props["aiohttp_session"]
    session_instance: ClientSession = session_prop.instance
    try:
        async with session_instance.get(url) as resp:
            await asyncio.sleep(0)
            data = await resp.json()
            await asyncio.sleep(0)
            df = pd.DataFrame(data.get("value", []))
            # Add a column for the indicator name
            df["IndicatorName"] = indicator_name
            if df.empty:
                raise EmptyDataPullException(url=url, indicator=indicator_name)
            df.to_csv(output_path, index=False)
            status, exception, result = resp.status, None, df
    except EmptyDataPullException as e:
        status, exception, result = None, EmptyDataPullException, format_exc()
    except (asyncio.TimeoutError, RuntimeError, ClientPayloadError, TransferEncodingError) as e:
        await worker.initialize_prop(props, "aiohttp_session")
        raise e
    finally:
        return status, exception, result

###############################################################################
# Main Workflow
###############################################################################

def split_indicators_to_dataset(indicators: ParametrizedIndicatorList, config: Path = "./datasets.yml") -> Dict[str, UnparametrizedIndicatorList]:
    """
    Split indicators into datasets based on the indicator's group.
    """
    indicators = indicators.value
    datasets = {}
    # Load the datasets.yml which maps Datasets to their lookup methods
    with open(config, "r") as f:
        dataset_configs = yaml.safe_load(f)
        df = pd.DataFrame(list(map(lambda x: x.model_dump(), indicators)))
        for dataset_name, dataset_config in dataset_configs.items():
            dataset_indicators = []
            for filter_name, filter_value in dataset_config.items():
                # Get the indicator codes
                dataset_indicators.extend([ind for ind in indicators if ind.code in df.query(filter_value, engine="python").code.to_list()])
            datasets[dataset_name] = UnparametrizedIndicatorList(value=dataset_indicators)
    return datasets

def aggregate_datasets(raw_root: Path, datasets_root: Path, datasets: Dict[str, UnparametrizedIndicatorList]) -> Generator[Tuple[str, dd.DataFrame], None, None]:
    """
    Aggregate datasets into a single DataFrame.
    """
    for dataset_name, dataset in datasets.items():
        dataset_dir = datasets_root / dataset_name
        dataset_dir.mkdir(exist_ok=True, parents=True)
        ddf = dd.read_csv(
            str(raw_root / dataset_name / "*.csv"),
            assume_missing=True,
            dtype={
                "Dim3": "object",
                "Dim3Type": "object",
                "Comments": "object",
                "TimeDimensionValue": "object",
                "DataSourceDim": "object",
                "DataSourceDimType": "object",
                "Value": "object",
                # ... additional column types as needed
            },
        )
        df = ddf.compute()
        df.to_csv(str(dataset_dir / dataset_name) + ".csv", index=False)
        yield dataset_name, df

        # Foundry dataset generation
        # dataset = Dataset.get(dataset_name)
        # dataset.write_table(df)



async def main(output_root: Path, mode: str) -> Any:
    """
    Workflow:
      1. Fetch raw indicators.
      2. Inject parameters to obtain parametrized indicators.
      3. Identify which indicators are already concrete (downloaded) if in delta mode.
      4. Enqueue delta tasks (or all tasks in full mode).
      5. Combine downloaded data into a unified dataset.
    """
    output_root.mkdir(exist_ok=True, parents=True)
    raw_root = output_root / "raw"
    bronze_root = output_root / "bronze"
    datasets_root = output_root / "datasets"
    bronze_root.mkdir(exist_ok=True, parents=True)

    # 1. Fetch raw indicators
    raw_indicators = await fetch_raw_indicators()

    datasets = split_indicators_to_dataset(raw_indicators)

    known_indicators = {ind.code for dataset in datasets.values() for ind in dataset.value}

    # 2. Transition to parametrized indicators
    datasets = inject_indicator_parameters(datasets, bronze_root)

    if mode == "delta":
        # Rewrite above concrete indicators but account for dataset_name folder
        concrete_indicators = [
            ConcreteIndicator(
                code=ind.code,
                name=ind.name,
                url=ind.url,
                language=ind.language,
                output_path=bronze_root / f"{dataset_name}/{ind.code}.csv",
            )
            for dataset_name, dataset in datasets.items()
            for ind in dataset.value
            if (bronze_root / f"{dataset_name}/{ind.code}.csv").exists()
        ]
        concrete_codes = {ci.code for ci in concrete_indicators}
        print(f"Already acquired indicators: {len(concrete_codes)}")
        delta_indicators = [ind for ind in known_indicators if ind.code not in concrete_codes]
        force_download = False
    elif mode == "full":
        # In full mode, re-download all indicators
        delta_indicators = known_indicators
        force_download = True
    else:
        raise ValueError("Invalid mode. Must be 'full' or 'delta'.")

    # Create tasks for each dataset
    tasks = {
        dataset_name: [
            AsyncFetchUrlTask(
                args=[
                    dataset_name,
                    ind.name,
                    ind.url,
                    ind.output_path,
                    force_download,
                ]
            )
            for ind in indicator_list.value
        ]
        for dataset_name, indicator_list in datasets.items()
    }

    total_tasks = sum(len(tasks) for tasks in tasks.values())

    print(f"Enqueueing {total_tasks} tasks.")

    num_workers = min(16, (min(cpu_count(), total_tasks) // 2) if tasks else 1)
    orchestrator = Orchestrator(
        num_workers=num_workers,
        show_progress=True,
        task_models=[AsyncFetchUrlTask],
        actions={"async_fetch_url": async_fetch_url},
        props={
            "aiohttp_session": Prop(
                initializer=init_aiohttp_session,
                use_context_manager=True,
            )
        },
        tasks_per_minute_limit=500,
    )

    start_time = time.monotonic()
    pending_enqueues = []
    for dataset_name, dataset_tasks in tasks.items():
        print(f"Enqueueing {len(dataset_tasks)} tasks for {dataset_name} dataset.")
        pending_enqueues.append(orchestrator.add_tasks(dataset_tasks))
    enqueue_failures = await asyncio.gather(*pending_enqueues)
    job_results: List[ResultTaskPair] = await orchestrator.stop_workers()
    elapsed = time.monotonic() - start_time
    print(f"Delta tasks completed in {elapsed:.2f} seconds with {len(enqueue_failures)} enqueue failures.")

    df = pd.DataFrame(list(map(lambda x: {**x.task.model_dump(), **dict(zip(["status_code", "exception"], (x.result[0], x.result[1])))}, job_results)))
    exceptions = set(df[~df["exception"].isna()]["exception"].unique().tolist())

    if exceptions != {EmptyDataPullException}:
        raise Exception(f"Unexpected exceptions: {exceptions - {EmptyDataPullException}}")

    df['dataset'] = list(map(lambda x: x[0], df["args"]))
    # Pretty print the counts by dataset
    print(df.groupby("dataset").agg({"status_code": "count", "exception": "count"}))

    df.to_csv(output_root / "task_results.csv", index=False)
    # 5. Aggregate datasets
    final_datasets = list(aggregate_datasets(bronze_root, datasets_root, datasets))
    return final_datasets

def init_aiohttp_session() -> ClientSession:
    """Initialize an aiohttp session for workers."""
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    timeout = aiohttp.ClientTimeout(total=60, connect=60, sock_read=60, sock_connect=60)
    return ClientSession(connector=aiohttp.TCPConnector(ssl=ssl_context), timeout=timeout)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch WHO GHO indicators.")
    parser.add_argument(
        "--mode",
        choices=["full", "delta"],
        default="delta",
        help="Mode: 'full' to pull all indicators (force re-download), or 'delta' to pull only missing ones.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="./data",
        help="Output directory for CSV files.",
    )
    args = parser.parse_args()

    output_root = Path(args.output)
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        loop.run_until_complete(main(output_root, args.mode))
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
