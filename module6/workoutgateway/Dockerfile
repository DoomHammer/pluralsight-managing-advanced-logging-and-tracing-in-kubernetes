FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir -r /app/requirements.txt

COPY . /app/

RUN opentelemetry-bootstrap -a install

ENV PORT=8000

EXPOSE ${PORT}

CMD ["opentelemetry-instrument", "python3", "/app/main.py"]
