install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C,W1203,E1101 stationarity app

test:
	python -m pytest -vv --cov=cli --cov=stationarity --cov=app test_stationarity.py

format:
	black *.py

deploy:
	REPOSITORY_URI=public.ecr.aws/d9i8a4o5/docker-microservices
	$(aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/d9i8a4o5)
	docker build -t $REPOSITORY_URI:latest .
	docker tag $REPOSITORY_URI:latest $REPOSITORY_URI:latest
	docker push $REPOSITORY_URI:latest

all:
	install lint test format deploy