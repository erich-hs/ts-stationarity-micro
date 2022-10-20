[![Python application test with Github Actions](https://github.com/erich-hs/ts-stationarity-micro/actions/workflows/main.yml/badge.svg)](https://github.com/erich-hs/ts-stationarity-micro/actions/workflows/main.yml) ![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)

# Time Series Stationarity Check Microservice
Containerized microservice for Time Series stationarity testing with Augmented Dickey-Fuller (ADF) and Kwiatkowski-Phillips-Schmidt-Shin (KPSS) tests.

## About this Repository
This is a template repository of a containerized Python Flask App Microservice that can be deployed locally or on cloud. You can find notes on deploying the Docker image locally, on an AWS Cloud9 environment or on a Google Cloud Shell.

## Local Deployment - Docker
### Docker Image
Build image locally
```bash
$ docker build --tag ts-micro .
```
Check the built image
```
$ docker image ls
```
Run a -d dettached local container based on built image, and map localhost:8080 to container port 8080
```
$ docker run -p 127.0.0.1:8080:8080 --name ts-micro-local -d ts-micro
```
Docker should return the container ID. You can see it running with
```
$ docker ps
```
You can now curl from the local machine to send data with a POST method
```bash
$ curl -d '{"timeseries":[1, 2, 3, 4]}' \
-H "Content-Type: application/json" \
-X POST http://localhost:8080/test_stationarity
```

### Shutting down
Shut down the container
```
$ docker stop ts-micro-local
```
Remove the container
```
$ docker rm ts-micro-local
```

## Local Deployment - Native Environment
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
-X POST http://localhost:8080/test_stationarity
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