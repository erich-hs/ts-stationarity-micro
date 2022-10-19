[![Python application test with Github Actions](https://github.com/erich-hs/ts-stationarity-micro/actions/workflows/main.yml/badge.svg)](https://github.com/erich-hs/ts-stationarity-micro/actions/workflows/main.yml) ![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)

# Time Series Stationarity Check Microservice
Containerized microservice for Time Series stationarity testing with Augmented Dickey-Fuller (ADF) and Kwiatkowski-Phillips-Schmidt-Shin (KPSS) tests.

### To post a sample stationarity test
Add permissions to sample_post.sh:
```bash
$ chmod +x ./sample_post.sh
```
Execute sample_post.sh
```bash
$ ./sample_post.sh
```

### To directly access the Python function:
Call the python interpeter -c code:
```
$ python -c 'import stationarity; print(stationarity.stationarity_test([1, 2, 3, 4]))'
```

### To post a request locally:
Run the Flask app locally:
```bash
$ python app.py
```
POST request
```bash
$ curl -d '{"timeseries":[1, 2, 3, 4]}' \
-H "Content-Type: application/json" \
-X POST http://localhost:5000/test_stationarity
```

### To run from your CLI:
Call the custom CLI function
```bash
$ python cli.py
```
It should prompt you for the time series input:

```
List-like, comma separated time series: 1, 2, 3, 4
```
After inserting a comma separated example the result should be similar to the output below:

![image](https://user-images.githubusercontent.com/77303576/196686095-4953aeb6-2bd7-4b1e-86ca-d5f7b64756bd.png)
