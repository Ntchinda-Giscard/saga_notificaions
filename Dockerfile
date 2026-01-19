FROM ghcr.io/astral-sh/uv:python3.12-alpine AS builder
WORKDIR /app
COPY pyproject.toml uv.lock* ./
# Install dependencies
RUN uv sync --frozen --no-dev

FROM gcr.io/distroless/python3-debian12
WORKDIR /app
# Copy venv
COPY --from=builder /app/.venv /app/.venv
# Copy source code
COPY src src
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app"

# Command to run the application using uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
