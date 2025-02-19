from __future__ import annotations

import os
from typing import TYPE_CHECKING

from pytest import fixture
from yaw.randoms import BoxRandoms

from rail.core.stage import RailStage
from rail.yaw_rail.utils import get_dc2_test_data

if TYPE_CHECKING:  # pragma: no cover
    from pandas import DataFrame
    from rail.core.data import DataStore


# disable mulitprocessing, which is only beneficial on large datasets
os.environ["YAW_NUM_THREADS"] = "1"


@fixture(name="data_store", scope="session", autouse=True)
def fixture_data_store() -> DataStore:
    data_store = RailStage.data_store
    data_store.__class__.allow_overwrite = True
    return data_store


@fixture(name="seed", scope="session")
def fixture_seed() -> int:
    return 12345


@fixture(name="mock_data", scope="session")
def fixture_mock_data(seed) -> DataFrame:
    return get_dc2_test_data().sample(20000, random_state=seed)


@fixture(name="mock_data_small", scope="session")
def fixture_mock_data_small(seed) -> DataFrame:
    return get_dc2_test_data().sample(100, random_state=seed)


@fixture(name="zlim", scope="session")
def fixture_zlim(mock_data):
    redshifts = mock_data["z"].to_numpy()
    return (redshifts.min(), redshifts.max())


@fixture(name="mock_rand", scope="session")
def fixture_mock_rand(mock_data, seed) -> DataFrame:
    n_data = len(mock_data)
    redshifts = mock_data["z"].to_numpy()

    generator = BoxRandoms(
        mock_data["ra"].min(),
        mock_data["ra"].max(),
        mock_data["dec"].min(),
        mock_data["dec"].max(),
        redshifts=redshifts,
        seed=seed,
    )
    test_rand = generator.generate_dataframe(n_data * 10)
    return test_rand.rename(columns=dict(redshifts="z"))
