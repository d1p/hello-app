FROM python:3.12-slim AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

FROM base AS test
RUN pip install --no-cache-dir pytest
COPY test_app.py .
RUN pytest -q

FROM base AS runtime
ARG APP_VERSION=dev
ENV APP_VERSION=$APP_VERSION
USER 10001
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]