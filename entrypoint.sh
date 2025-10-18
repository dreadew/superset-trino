#!/bin/bash
set -e

echo "Initializing Superset..."

until PGPASSWORD=$SUPERSET_DB_PASSWORD psql -h "$SUPERSET_DB_HOST" -U "$SUPERSET_DB_USER" -d "$SUPERSET_DB_NAME" -c '\q'; do
  echo "Waiting for PostgreSQL..."
  sleep 2
done

echo "PostgreSQL is ready"

if [ "$SUPERSET_ADMIN_USERNAME" ] && [ "$SUPERSET_ADMIN_PASSWORD" ]; then
  echo "Creating admin user..."
  superset fab create-admin \
    --username "$SUPERSET_ADMIN_USERNAME" \
    --firstname "$SUPERSET_ADMIN_FIRSTNAME" \
    --lastname "$SUPERSET_ADMIN_LASTNAME" \
    --email "$SUPERSET_ADMIN_EMAIL" \
    --password "$SUPERSET_ADMIN_PASSWORD" || true
fi

echo "Upgrading database..."
superset db upgrade

echo "Initializing Superset..."
superset init

echo "Superset initialized successfully"

exec /usr/bin/run-server.sh
