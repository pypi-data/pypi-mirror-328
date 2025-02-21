import logging
import platform
from contextlib import contextmanager
from typing import Any, Dict, Optional

from opentelemetry import trace


class StructuredLogger:
    """
    Logger that produces structured logs with tracing context.
    """

    def __init__(
            self,
            service_name: str,
            default_attributes: Optional[Dict[str, Any]] = None
    ):
        self.logger = logging.getLogger(service_name)
        self.default_attributes = {
            "service.name": service_name,
            "host.name": platform.node(),
            **(default_attributes or {})
        }

    def _get_trace_context(self) -> Dict[str, str]:
        """
        Gets the current tracing context if it exists.
        """
        span = trace.get_current_span()
        if span.is_recording():
            ctx = span.get_span_context()
            return {
                "trace_id": format(ctx.trace_id, "032x"),
                "span_id": format(ctx.span_id, "016x")
            }
        return {}

    def _log(
            self,
            level: int,
            message: str,
            *args,
            **kwargs
    ):
        trace_context = self._get_trace_context()

        log_attributes = {
            **self.default_attributes,
            "timestamp": datetime.utcnow().isoformat(),
            "severity": logging.getLevelName(level),
            "logger.name": self.logger.name,
            **trace_context
        }

        additional_info = []
        if kwargs.get("error_type"):
            additional_info.append(f"type={kwargs['error_type']}")
            log_attributes["error.type"] = kwargs["error_type"]
        if kwargs.get("error_message"):
            additional_info.append(f"message={kwargs['error_message']}")
            log_attributes["error.message"] = kwargs["error_message"]
        if kwargs.get("operation"):
            additional_info.append(f"operation={kwargs['operation']}")
            log_attributes["operation"] = kwargs["operation"]

        remaining_attrs = {
            k: v for k, v in kwargs.items()
            if k not in ["error_type", "error_message", "operation"]
        }
        if remaining_attrs:
            log_attributes["attributes"] = remaining_attrs

        additional_str = f" - {', '.join(additional_info)}" if additional_info else ""
        trace_str = f"[trace_id={trace_context.get('trace_id', '0')}]" if trace_context else ""
        log_message = f"{trace_str} {message}{additional_str}"

        self.logger.log(
            level,
            log_message,
            extra={
                "structured": True,
                "otel.name": "log",
                "otel.kind": "event",
                "otelTraceID": trace_context.get("trace_id", ""),
                "otelSpanID": trace_context.get("span_id", ""),
                **log_attributes
            }
        )

    def debug(self, message: str, *args, **kwargs):
        self._log(logging.DEBUG, message, *args, **kwargs)

    def info(self, message: str, *args, **kwargs):
        self._log(logging.INFO, message, *args, **kwargs)

    def error(self, message: str, *args, **kwargs):
        self._log(logging.ERROR, message, *args, **kwargs)

    @contextmanager
    def operation_context(
            self,
            operation_name: str,
            **context
    ):
        """
        Provides context for an operation, recording its beginning and end.
        """
        try:
            self.info(
                f"Iniciando {operation_name}",
                operation=operation_name,
                status="started",
                **context
            )
            yield
            self.info(
                f"Completado {operation_name}",
                operation=operation_name,
                status="completed",
                **context
            )
        except Exception as e:
            self.error(
                f"Error en {operation_name}: {str(e)}",
                operation=operation_name,
                status="failed",
                error=str(e),
                **context
            )
            raise
