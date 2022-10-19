import click
from stationarity import stationarity_test

@click.command()
@click.option(
    "--timeseries",
    prompt="List-like, comma separated time series",
    help="Pass in a time series to test for stationarity"
)

def stationarity_testcli(timeseries):
    """
    Check for time series stationarity with ADF and KPSS tests.
    """
    payload = stationarity_test(timeseries)
    adf_result = payload["ADF Test Result"]
    kpss_result = payload["KPSS Test Result"]
    # Font formatting
    adf_fg="green"
    kpss_fg="green"
    if adf_result["Decision"]=="Non-Stationary":
        adf_fg="red"
    if kpss_result["Decision"]=="Non-Stationary":
        kpss_fg="red"
    # Echoing results
    click.echo("ADF: " + click.style(adf_result, fg=adf_fg))
    click.echo("KPSS: " + click.style(kpss_result, fg=kpss_fg))

if __name__=="__main__":
    stationarity_testcli()