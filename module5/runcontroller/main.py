import atexit
import json
import os
import uuid

from flask import Flask, request, jsonify
from opentelemetry import trace, metrics
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
import redis

service_name = os.environ.get('OTEL_SERVICE_NAME')

# Initialize Traces and Metrics
tracer = trace.get_tracer_provider().get_tracer(service_name)
meter = metrics.get_meter_provider().get_meter(service_name)


app = Flask(__name__)

tracer = trace.get_tracer("run-controller")


@app.route("/", methods=('POST',))
def main(r=request):
    span_ctx = TraceContextTextMapPropagator().extract(carrier=request.headers)
    with tracer.start_as_current_span('processRun', context=span_ctx) as span:
        request_id = str(uuid.uuid4())
        app.logger.debug("Received request %s to /", request_id)

        with tracer.start_as_current_span('validatePayload') as span:
            content = r.json

            app.logger.debug("Request %s positively validated", request_id)

        workout_id = content["workout_id"]
        app.logger.debug("Processing workout %s in request %s", workout_id, request_id)

        with tracer.start_as_current_span('calculateScore') as span:
            # TODO: actually calculate the run score based on random and log the random && score + request id!
            score = 73
            content["score"] = score

        with tracer.start_as_current_span('storeRun') as span:
            r = redis.Redis(host=os.environ["REDIS_HOST"], password=os.environ["REDIS_PASSWORD"])
            r.set(workout_id, json.dumps(content))
            app.logger.debug("Persisted workout %s in db for request %s", workout_id, request_id)

        return jsonify({"workout_id": workout_id, "score": score})


@app.route("/divide", methods=('GET',))
def divide(r=request):
    return jsonify({"results": 5/0})


@app.route("/health", methods=('GET',))
def health():
    return jsonify({"status": "ok"})

def shutdown_hook():
    app.logger.info("Gracefully shutting down")

if __name__ == "__main__":
    port = os.environ["PORT"]
    debug = bool(os.environ.get("DEBUG"))

    atexit.register(shutdown_hook)

    app.run('0.0.0.0', debug=debug, port=port)
