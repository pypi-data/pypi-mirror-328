import asyncio
from typing import Any, Awaitable, Callable, Dict, NoReturn, Optional, TypeVar

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.trace import Status, StatusCode

from ..constants import DEFAULT_CONFIG, ENDPOINTS
from ..types import TelemetryConfig, TelemetryService
from ..utils.error_util import TelemetryError
from ..utils.logging_util import custom_error_logger, custom_logger

T = TypeVar("T")


class TracingService(TelemetryService):
    def __init__(self, config: TelemetryConfig, resource: Resource):
        self.config = config
        trace_exporter = OTLPSpanExporter(
            endpoint=f"{config.otlp_endpoint or DEFAULT_CONFIG['otlp_endpoint']}{ENDPOINTS['TRACES']}"
        )

        self.tracer_provider = TracerProvider(resource=resource)
        self.tracer_provider.add_span_processor(BatchSpanProcessor(trace_exporter))
        trace.set_tracer_provider(self.tracer_provider)

    async def start(self) -> None:
        try:
            await self._test()
            custom_logger("Tracing service started successfully")
        except Exception as error:
            custom_error_logger("Failed to start tracing service:", error)
            raise

    async def _test(self) -> None:
        try:

            async def test_operation():
                await asyncio.sleep(0.1)
                return "test completed"

            await self.create_span(
                "telemetry.initialization.test",
                test_operation,
                {"status": "initialized"},
            )
            custom_logger("Test span created successfully")
        except Exception as error:
            custom_error_logger("Failed to create test span:", error)
            raise

    async def shutdown(self) -> None:
        try:
            await self.tracer_provider.shutdown()  # type: ignore
        except Exception as error:
            custom_error_logger("Failed to shutdown tracing service:", error)
            raise TelemetryError("Failed to shutdown tracing service", error)

    def instrument_fastapi(self, app) -> None:
        FastAPIInstrumentor.instrument_app(app)

    async def create_span(
        self,
        name: str,
        operation: Callable[[], Awaitable[T]],
        attributes: Optional[Dict[str, Any]] = None,
    ) -> T:
        tracer = trace.get_tracer("default")

        with tracer.start_as_current_span(name) as span:
            try:
                if attributes:
                    for key, value in attributes.items():
                        span.set_attribute(key, value)

                result = await operation()
                span.set_status(Status(StatusCode.OK))
                return result

            except Exception as error:
                span.record_exception(error)
                span.set_status(Status(StatusCode.ERROR, description=str(error)))
                raise

    def add_attributes(self, attributes: Dict[str, Any]) -> None:
        span = trace.get_current_span()
        if span and attributes:
            for key, value in attributes.items():
                span.set_attribute(key, value)

    def record_error(self, error: Exception) -> None:
        span = trace.get_current_span()
        if span:
            span.record_exception(error)
            span.set_status(Status(StatusCode.ERROR, description=str(error)))
