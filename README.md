# ts-stationarity-micro
Containerized microservice for Time Series stationarity testing


To directly access the Python function:
python -c 'import stationarity; print(stationarity.stationarity_test([1, 2, 3, 4]))'

To post a request locally:
curl -d '{"timeseries":[1, 2, 3, 4]}' -H "Content-Type: application/json" -X POST http://localhost:5000/test_stationarity
