FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 \
    MPPT24_HOST=0.0.0.0 MPPT24_DB_PATH=/app/data/conversas.db PORT=5013

WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y --no-install-recommends espeak-ng && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r requirements.txt && \
    useradd --system --user-group mppt24 && \
    mkdir /app/data && chown mppt24:mppt24 /app/data

COPY main.py knowledge.py ./
COPY templates ./templates
COPY static ./static

USER mppt24
EXPOSE 5013
CMD ["python", "main.py"]
