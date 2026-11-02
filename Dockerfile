FROM python:3.12-slim

LABEL org.opencontainers.image.title="accounts" \
      org.opencontainers.image.description="Customer Accounts REST API" \
      org.opencontainers.image.licenses="Apache-2.0"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

WORKDIR /app

# Run as an unprivileged user
RUN groupadd --system app && useradd --system --gid app --home /app app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY --chown=app:app . .

# Flask-SQLAlchemy resolves a relative SQLite URI against app.instance_path
# (/app/instance), so the unprivileged user must own that directory.
RUN mkdir -p /app/instance && chown -R app:app /app/instance

USER app

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
    CMD python -c "import sys,urllib.request; sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:8080/health').status == 200 else 1)"

CMD ["/app/bin/entrypoint.sh"]
