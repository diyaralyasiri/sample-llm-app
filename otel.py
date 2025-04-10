from traceloop.sdk import Traceloop
# from opentelemetry.sdk.trace.export import ConsoleSpanExporter
import os

def setup_openllmetry(app):
    Traceloop.init(
        "basic_llm_token_service",
        api_endpoint=os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT"),
        disable_batch=True
        # , exporter=ConsoleSpanExporter()    
    )