# OpenTelemetry Utils

A Python library designed to simplify application instrumentation using OpenTelemetry. This library provides an abstraction layer that makes instrumentation more intuitive and less intrusive in your business logic.

## Features

- Simplified OpenTelemetry configuration
- Intuitive API for distributed tracing
- Utilities for metrics and structured logging
- OpenTelemetry Collector integration
- Complete context propagation support
- Full compatibility with asynchronous applications

## Installation

To install the library from the private repository:

```bash
pip install git+ssh://git@github.com/your-organization/otel-utils.git
```

Or add this to your requirements.txt:
```bash
git+ssh://git@github.com/your-organization/otel-utils.git@v0.1.0
```

# Basic Usage
## Initial Configuration
```python
from otel_utils import OtelConfig, OtelConfigurator

config = OtelConfig(
    service_name="my-service",
    environment="production"
)

OtelConfigurator(config)
```

## Tracing
```python
from otel_utils import Tracer

tracer = Tracer("my-service")

# Using the decorator
@tracer.trace("my_operation")
async def my_function():
    # Your code here
    pass

# Using the context manager
with tracer.create_span("my_operation") as span:
    span.set_attribute("key", "value")
    # Your code here
```

## Metrics
```python
from otel_utils import Metrics

metrics = Metrics("my-service")

# Simple counter
counter = metrics.get_counter("requests_total")
counter.add(1, {"endpoint": "/api/v1/resource"})

# Histogram for latencies
with metrics.measure_duration("request_duration"):
    # Your code here
    pass
```

## Structured Logging
```python
from otel_utils import StructuredLogger

logger = StructuredLogger("my-service")

with logger.operation_context("process_order", order_id="123"):
    logger.info("Starting processing")
    # Your code here
```

# OpenTelemetry Collector Integration
This library is designed to work seamlessly with the OpenTelemetry Collector. Telemetry data is sent using the OTLP protocol, which is the OpenTelemetry standard.
```yaml
# collector configuration example
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

exporters:
  # configure your exporters here

service:
  pipelines:
    traces:
      receivers: [otlp]
      exporters: [your-exporter]
```

# Best Practices
## Separation of Concerns
Keep instrumentation separate from business logic by creating domain-specific abstractions. Your business code should remain clean and focused on its primary responsibilities.

## Consistent Naming
Use coherent naming conventions for spans, metrics, and logs across your services. This makes it easier to correlate and analyze telemetry data.

## Relevant Context
Include useful contextual information in spans and logs, but be mindful of sensitive data. Focus on information that aids debugging and monitoring.

## Appropriate Granularity
Don't instrument everything. Focus on significant operations that provide value for monitoring and debugging. Consider the overhead and noise ratio when adding instrumentation.

# Development
To set up the development environment:
    
```bash
# Create virtualenv
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

# Contributing
1. Create a feature branch (`git checkout -b feature/new-feature`)
2. Commit your changes (`git commit -am 'Add new feature'`)
3. Push to the branch (`git push origin feature/new-feature`)
4. Create a Pull Request

I hope this documentation helps you understand and effectively use the OpenTelemetry Utils library. Each section is designed to guide you through the essential aspects of instrumenting your applications while maintaining clean and maintainable code.
Let me know if you need any clarification or have questions about specific features or use cases. We can explore any aspect of the library in more detail.