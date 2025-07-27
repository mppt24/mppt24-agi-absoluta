# 🐳 mppt24 AGI ABSOLUTA - Docker Image
FROM python:3.11-slim

# 📋 Metadata
LABEL maintainer="mppt24@gmail.com"
LABEL description="mppt24 AGI ABSOLUTA - Inteligência Artificial Geral com Conhecimento Universal"
LABEL version="1.0.0"
LABEL org.opencontainers.image.source="https://github.com/mppt24/mppt24-agi-absoluta"

# 🔧 Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=main.py \
    FLASK_ENV=production \
    PORT=5000

# 👤 Create non-root user for security
RUN groupadd -r mppt24 && useradd -r -g mppt24 mppt24

# 📁 Set work directory
WORKDIR /app

# 📦 Install system dependencies
RUN apt-get update && apt-get install -y \
    --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 📋 Copy requirements first for better caching
COPY requirements.txt .

# 🔧 Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 📁 Copy application code
COPY . .

# 🔒 Change ownership to non-root user
RUN chown -R mppt24:mppt24 /app

# 👤 Switch to non-root user
USER mppt24

# 🌐 Expose port
EXPOSE $PORT

# 🏥 Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:$PORT/ || exit 1

# 🚀 Run the application
CMD ["python", "main.py"]

