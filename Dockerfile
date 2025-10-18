FROM apache/superset:master

USER root

ENV PLAYWRIGHT_BROWSERS_PATH=/usr/local/share/playwright-browsers

RUN apt-get update && \ 
    apt-get install -y \
    postgresql-client && \ 
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv

RUN uv pip install --system --no-cache \
    psycopg2-binary \
    trino \
    pyhive[hive] \
    boto3 \
    openpyxl \
    Pillow \
    playwright \
    && playwright install-deps \
    && PLAYWRIGHT_BROWSERS_PATH=/usr/local/share/playwright-browsers playwright install chromium

RUN mkdir -p /app/superset_home/uploads && chown -R superset:superset /app/superset_home

COPY superset_config.py /app/pythonpath/superset_config.py
COPY entrypoint.sh /app/docker/entrypoints/custom-entrypoint.sh

RUN chmod +x /app/docker/entrypoints/custom-entrypoint.sh

USER superset

ENTRYPOINT ["/app/docker/entrypoints/custom-entrypoint.sh"]
