FROM public.ecr.aws/lambda/python:3.9

WORKDIR /ts-micro

COPY . app.py /ts-micro/

RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]