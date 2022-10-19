from stationarity import build_series, fillna
import numpy as np
import pandas as pd
import pytest
from click.testing import CliRunner
from cli import stationarity_testcli
from app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_format_input():
    built_from_str = build_series("1, 2, 3, 4")
    built_from_lst = build_series([1, 2, 3, 4])
    assert type(built_from_str) == pd.core.series.Series
    assert type(built_from_lst) == pd.core.series.Series


def test_fillna():
    series = build_series([1, 2, np.nan, 4])
    filled_interpolate = fillna(series, method="interpolate")
    filled_ffill = fillna(series, method="ffill")
    filled_bfill = fillna(series, method="bfill")
    assert np.nan not in filled_interpolate
    assert np.nan not in filled_ffill
    assert np.nan not in filled_bfill


def test_stationarity_testcli():
    runner = CliRunner()
    result = runner.invoke(stationarity_testcli, ["--timeseries", "1, 2, 3, 4"])
    assert result.exit_code == 0


# Smoke test Flask
def test_index(app, client):
    res = client.get("/")
    assert res.status_code == 200
    expected = "Time Series stationarity check with ADF and KPSS tests"
    assert expected in res.get_data(as_text=True)
