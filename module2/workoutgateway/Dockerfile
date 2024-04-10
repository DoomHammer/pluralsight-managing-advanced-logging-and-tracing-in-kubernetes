FROM alpine:3.18

RUN apk add --no-cache python3 py-pip

COPY requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir -r /app/requirements.txt

COPY . /app/

ENV PORT=8000

EXPOSE 8000

CMD ["python3", "/app/main.py"]
