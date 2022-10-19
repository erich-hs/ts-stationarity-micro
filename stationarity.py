import warnings
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller, kpss

warnings.filterwarnings("ignore", category=UserWarning)


def build_series(series):
    """
    Build Pandas Series from input data.
    """
    # Typecasting from string to accept CLI inputs
    if type(series) == str:
        series = series.replace(" ", "").split(",")
        series = [float(t) for t in series]
    series = np.array(series)
    series = series.flatten()
    series = pd.Series(series)
    return series


def fillna(data, method="Interpolate"):
    """
    Fill missing values with one of the following methods:
    Interpolate: linear interpolation.
    Ffill: Forward filling with nearest past available value.
    Bfill: Backward filling with nearest future available value.
    """
    if method.lower() == "interpolate":
        data = data.interpolate()
    elif method.lower() == "ffill":
        data = data.ffill()
    elif method.lower() == "bfill":
        data = data.bfill()

    return data


def interprete_results(output, test):
    """
    Parse ADF and KPSS test results to a human readable interpretation.
    """
    pval = output[1]
    test_score = output[0]
    lags = output[2]
    decision = "Non-Stationary"
    if test == "adf":
        if pval < 0.05:
            decision = "Stationary"
    elif test == "kpss":
        if pval >= 0.05:
            decision = "Stationary"
    output_dict = {
        "Test Statistic": round(test_score, 4),
        "P-Value": round(pval, 4),
        "Lags Used": lags,
        "Decision": decision,
    }
    return output_dict


def stationarity_test(timeseries):
    """
    Check for time series stationarity with ADF and KPSS tests.
    """
    # Build Pandas Series
    timeseries = build_series(timeseries)

    # Filling missing values
    # dropna ensures no missing values on either end of the time series
    timeseries = fillna(timeseries).dropna()

    # ADF and KPSS tests outputs
    adf_output = adfuller(timeseries, autolag="AIC")
    kpss_output = kpss(timeseries)

    # Parsing results
    payload = {}
    # ADF test
    payload["ADF Test Result"] = interprete_results(adf_output, test="adf")
    # KPSS test
    payload["KPSS Test Result"] = interprete_results(kpss_output, test="kpss")

    return payload
