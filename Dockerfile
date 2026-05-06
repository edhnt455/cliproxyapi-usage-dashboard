FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    CLIPROXY_USAGE_BASE_DIR=/data \
    CLIPROXY_AUTH_DIR=/cliproxy-auth

WORKDIR /app

COPY usage_dashboard.py /app/usage_dashboard.py

RUN useradd -r -u 10001 appuser \
    && mkdir -p /data /cliproxy-auth \
    && chown -R appuser:appuser /data /cliproxy-auth /app

USER appuser

ENTRYPOINT ["python", "/app/usage_dashboard.py"]
CMD ["serve"]
