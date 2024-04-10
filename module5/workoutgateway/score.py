import os
import time
from opentelemetry import trace, metrics

service_name = os.environ.get('OTEL_SERVICE_NAME')

# Initialize Traces and Metrics
tracer = trace.get_tracer_provider().get_tracer(service_name)
meter = metrics.get_meter_provider().get_meter(service_name)

@tracer.start_as_current_span("do_some_work")
def do_some_work(x: int) -> int:
    """Efficiently computes a simple polynomial just for kicks

    5 + 3x + 4x^2
    """
    return 5 + x * (3 + x * (4))
