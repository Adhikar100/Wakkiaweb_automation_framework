# Optional Docker image for running tests in CI
FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir pytest pytest-xdist python-dotenv playwright \
    && python -m playwright install --with-deps

CMD ["pytest"]
