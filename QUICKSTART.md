# Superset Quick Start

## 1. Build Image

```bash
cd superset
docker build -t superset_local .
```

## 2. Start Services

```bash
cd ../services
make -f Makefile.local up
```

## 3. Access Superset

Open browser: http://localhost:8089

**Default credentials:**
- Username: `admin`
- Password: `admin`

## 4. Add Trino Connection

1. Go to **Data > Databases > + Database**
2. Select **Presto** (Trino uses Presto protocol)
3. Enter URI: `trino://admin@trino:8080/delta`
4. Click **Test Connection** then **Connect**

## 4. Create Your First Chart

1. Go to **SQL Lab > SQL Editor**
2. Select database: **Trino - Delta Lake**
3. Run query:
   ```sql
   SELECT * FROM prod_hotels.hotels LIMIT 10
   ```
4. Click **Explore** to create visualizations

## Connection Strings

- Delta Lake: `trino://admin@trino:8080/delta`
- Hive Raw: `trino://admin@trino:8080/hive`

**Note:** Use **Presto** connector type in Superset UI.

See [CONNECTIONS.md](CONNECTIONS.md) for detailed guide.

## Commands

```bash
# Rebuild Superset image
cd superset
docker build -t superset_local .

# Restart Superset
cd services
docker compose -f compose.local.yaml restart superset

# View logs
docker logs superset -f

# Access Superset CLI
docker exec -it superset superset --help
```
