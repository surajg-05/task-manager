FROM python:3.12-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy dependency files first
COPY pyproject.toml uv.lock ./

# Install dependencies into the container
RUN uv sync --frozen --no-dev

# Copy application code
COPY . .

EXPOSE 5000

CMD ["uv", "run", "--no-dev", "python", "app.py"]