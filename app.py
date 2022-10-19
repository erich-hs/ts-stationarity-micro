from flask import Flask, request
from flask.logging import create_logger
import logging
import stationarity

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route("/")
def home():
    html = f"<h3>Time Series stationarity check with ADF and KPSS tests</h3>"
    return html.format(format)

@app.route("/test_stationarity", methods=["POST"])
def test_stationarity():
    """
    Perform and return results for "ADF" and "KPSS" stationarity tests.
    """
    json_payload = request.json
    LOG.info(f"JSON payload: {json_payload}")
    test_results=stationarity.stationarity_test(json_payload["timeseries"])
    return test_results

if __name__=="__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

