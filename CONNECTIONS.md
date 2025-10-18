# Superset Database Connections Guide

## Trino Connections

**Important:** Use **Presto** connector type in Superset (Trino is compatible with Presto protocol).

### 1. Delta Lake Tables (Production Data)

**Connection String:**
```
trino://admin@trino:8080/delta
```

**Alternative with user specification:**
```
trino://superset@trino:8080/delta
```

**SQLAlchemy URI:**
```
trino://admin@trino:8080/delta
```

**Test Query:**
```sql
SELECT * FROM prod_hotels.hotels LIMIT 10;
```

### 2. Hive Tables (Raw Data)

**Connection String:**
```
trino://admin@trino:8080/hive
```

**SQLAlchemy URI:**
```
trino://admin@trino:8080/hive
```

**Test Query:**
```sql
SELECT * FROM raw_hotels.hotels_makemytrip LIMIT 10;
```

## Hive Direct Connection

**Connection String (PyHive):**
```
hive://hive-metastore:10000/default
```

Note: Requires Hive Server2 to be running (currently not configured).

## Connection Setup in Superset

1. Navigate to: **Data > Databases > + Database**

2. Select **Presto** from supported databases (Trino uses Presto protocol)

3. Enter connection details:
   - **Display Name:** `Trino - Delta Lake`
   - **SQLAlchemy URI:** `trino://admin@trino:8080/delta`
   
4. Click **Test Connection**

5. Click **Connect**

### Alternative: Manual Connection String

If using the manual connection string input:

```
trino://admin@trino:8080/delta
```

**Notes:**
- User can be any name (e.g., `admin`, `superset`, `trino`)
- No password required for local Trino setup
- Use `delta` catalog for production Delta Lake tables
- Use `hive` catalog for raw CSV data

## Available Schemas

### Delta Catalog (Production)
- `prod_hotels` - Hotel master data
- `prod_reviews` - Customer reviews
- `prod_reservations` - Booking data

### Hive Catalog (Raw Data)
- `raw_hotels` - Raw hotel data
- `raw_reviews` - Raw review data
- `raw_reservations` - Raw reservation data

## Example Queries

### Hotels by Country
```sql
SELECT country, COUNT(*) as hotel_count
FROM prod_hotels.hotels
GROUP BY country
ORDER BY hotel_count DESC;
```

### Reviews Rating Distribution
```sql
SELECT 
  CAST(overall_rating AS INT) as rating,
  COUNT(*) as count
FROM prod_reviews.reviews
WHERE overall_rating IS NOT NULL
GROUP BY CAST(overall_rating AS INT)
ORDER BY rating;
```

### Monthly Reservations
```sql
SELECT 
  arrival_year,
  arrival_month,
  COUNT(*) as bookings,
  SUM(total_cost) as revenue
FROM prod_reservations.reservations
GROUP BY arrival_year, arrival_month
ORDER BY arrival_year DESC, arrival_month DESC;
```

## S3 Access

Superset can access S3 data through Trino. All queries to Delta Lake and Hive tables automatically read from MinIO S3.

**S3 Buckets:**
- `s3://raw/` - Raw CSV data
- `s3://prod/` - Production Delta Lake tables
- `s3://warehouse/` - Hive warehouse

## Troubleshooting

### Connection Refused
- Ensure Trino container is running: `docker ps | grep trino`
- Check Trino is accessible: `docker exec trino trino --execute "SELECT 1"`

### Schema Not Found
- Verify schemas exist: `SHOW SCHEMAS IN delta`
- Run schema creation script: `bash create_trino_schemas.sh`

### No Data Returned
- Check S3 buckets have data: `docker exec trino trino --execute "SELECT * FROM hive.raw_hotels.hotels_makemytrip LIMIT 1"`
- Verify file upload: `bash upload_raw_to_s3.sh`
