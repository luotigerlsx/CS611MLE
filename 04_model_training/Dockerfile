FROM tensorflow/tensorflow:2.1.0-py3

COPY requirements.txt .

RUN python -m pip install -r \
    requirements.txt --quiet --no-cache-dir \
    && rm -f requirements.txt

WORKDIR /app

COPY . /app

ENTRYPOINT ["python","./app.py"]