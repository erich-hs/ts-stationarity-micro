install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C,W1203,E1101 stationarity app

test:
	python -m pytest -vv --cov=cli --cov=stationarity --cov=app test_stationarity.py

format:
	black *.py

all:
	install lint test format