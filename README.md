# Apache Superset with Trino, Hive, and S3 Support

Custom Docker image for Apache Superset 4.1.0 with drivers for Trino, Hive, PostgreSQL, and S3 integration.

## Features

- Apache Superset 4.1.0
- Trino connector (for Delta Lake and analytics)
- PyHive connector (for Hive Metastore)
- PostgreSQL driver (metadata store)
- S3 support via boto3
- Playwright for screenshots and PDF reports

## Quick Start

1. Build the image:

   ```bash
   cd superset
   docker build -t superset_local .
   ```

2. Start services (from services directory):

   ```bash
   cd ../services
   make -f Makefile.local up
   ```

3. Access Superset UI:

   ```
   http://localhost:8089
   ```
   
   Default credentials: `admin` / `admin`

## Database Connection Strings

### Trino (recommended for analytics)
```
trino://trino:8080/hive
trino://trino:8080/delta
```

### Hive (direct metastore connection)
```
hive://hive-metastore:10000/default
```

### PostgreSQL (for Superset metadata)
```
postgresql+psycopg2://user:password@postgres:5432/superset
```

## Exposed Ports

- 8088 - Superset Web UI

## Initial Setup

After first run, initialize the database and create admin user:

```bash
docker exec -it superset superset db upgrade
docker exec -it superset superset fab create-admin
docker exec -it superset superset init
```
