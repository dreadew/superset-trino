# Superset Dashboard Examples

## Hotel Analytics Dashboard

### Chart 1: Hotels by Country (Bar Chart)
```sql
SELECT 
  country,
  COUNT(*) as hotel_count
FROM prod_hotels.hotels
WHERE country IS NOT NULL
GROUP BY country
ORDER BY hotel_count DESC
LIMIT 10;
```

### Chart 2: Average Rating by City (Map)
```sql
SELECT 
  city,
  country,
  AVG(rating) as avg_rating,
  latitude,
  longitude
FROM prod_hotels.hotels
WHERE rating IS NOT NULL 
  AND latitude IS NOT NULL
  AND longitude IS NOT NULL
GROUP BY city, country, latitude, longitude;
```

### Chart 3: Hotel Distribution (Pie Chart)
```sql
SELECT 
  CASE 
    WHEN rating >= 4.5 THEN '5 Star'
    WHEN rating >= 3.5 THEN '4 Star'
    WHEN rating >= 2.5 THEN '3 Star'
    ELSE 'Budget'
  END as category,
  COUNT(*) as count
FROM prod_hotels.hotels
WHERE rating IS NOT NULL
GROUP BY category;
```

## Review Analytics Dashboard

### Chart 1: Monthly Review Trends (Line Chart)
```sql
SELECT 
  DATE_TRUNC('month', review_date) as month,
  COUNT(*) as review_count,
  AVG(overall_rating) as avg_rating
FROM prod_reviews.reviews
WHERE review_date >= DATE '2023-01-01'
GROUP BY DATE_TRUNC('month', review_date)
ORDER BY month;
```

### Chart 2: Rating Distribution (Histogram)
```sql
SELECT 
  CAST(overall_rating AS INT) as rating,
  COUNT(*) as count
FROM prod_reviews.reviews
WHERE overall_rating IS NOT NULL
GROUP BY CAST(overall_rating AS INT)
ORDER BY rating;
```

### Chart 3: Top Reviewed Hotels (Table)
```sql
SELECT 
  hotel_name,
  COUNT(*) as review_count,
  AVG(overall_rating) as avg_rating,
  AVG(cleanliness_rating) as cleanliness,
  AVG(service_rating) as service
FROM prod_reviews.reviews
GROUP BY hotel_name
ORDER BY review_count DESC
LIMIT 20;
```

### Chart 4: Reviews by Nationality (Sunburst)
```sql
SELECT 
  reviewer_nationality,
  COUNT(*) as count,
  AVG(overall_rating) as avg_rating
FROM prod_reviews.reviews
WHERE reviewer_nationality IS NOT NULL
GROUP BY reviewer_nationality
ORDER BY count DESC
LIMIT 15;
```

## Reservation Analytics Dashboard

### Chart 1: Monthly Revenue Trend (Area Chart)
```sql
SELECT 
  arrival_year,
  arrival_month,
  COUNT(*) as bookings,
  SUM(total_cost) as revenue,
  AVG(total_cost) as avg_booking_value
FROM prod_reservations.reservations
WHERE is_canceled = false
GROUP BY arrival_year, arrival_month
ORDER BY arrival_year, arrival_month;
```

### Chart 2: Lead Time Distribution (Histogram)
```sql
SELECT 
  CASE 
    WHEN lead_time < 7 THEN '< 1 week'
    WHEN lead_time < 30 THEN '1-4 weeks'
    WHEN lead_time < 90 THEN '1-3 months'
    WHEN lead_time < 180 THEN '3-6 months'
    ELSE '6+ months'
  END as lead_time_bucket,
  COUNT(*) as count
FROM prod_reservations.reservations
GROUP BY lead_time_bucket
ORDER BY 
  CASE lead_time_bucket
    WHEN '< 1 week' THEN 1
    WHEN '1-4 weeks' THEN 2
    WHEN '1-3 months' THEN 3
    WHEN '3-6 months' THEN 4
    ELSE 5
  END;
```

### Chart 3: Cancellation Rate by Market Segment (Bar Chart)
```sql
SELECT 
  market_segment,
  COUNT(*) as total_bookings,
  SUM(CASE WHEN is_canceled THEN 1 ELSE 0 END) as canceled,
  CAST(SUM(CASE WHEN is_canceled THEN 1 ELSE 0 END) AS DOUBLE) / COUNT(*) * 100 as cancellation_rate
FROM prod_reservations.reservations
GROUP BY market_segment
ORDER BY cancellation_rate DESC;
```

### Chart 4: Guest Type Analysis (Stacked Bar)
```sql
SELECT 
  CASE 
    WHEN num_children > 0 OR num_babies > 0 THEN 'Family'
    WHEN num_adults = 1 THEN 'Solo'
    WHEN num_adults = 2 THEN 'Couple'
    ELSE 'Group'
  END as guest_type,
  COUNT(*) as bookings,
  AVG(total_cost) as avg_spend,
  AVG(num_special_requests) as avg_requests
FROM prod_reservations.reservations
GROUP BY guest_type;
```

## Combined KPI Dashboard

### Metric 1: Total Hotels
```sql
SELECT COUNT(*) as total_hotels
FROM prod_hotels.hotels;
```

### Metric 2: Total Reviews
```sql
SELECT COUNT(*) as total_reviews
FROM prod_reviews.reviews;
```

### Metric 3: Total Bookings (YTD)
```sql
SELECT COUNT(*) as ytd_bookings
FROM prod_reservations.reservations
WHERE arrival_year = YEAR(CURRENT_DATE);
```

### Metric 4: Average Rating
```sql
SELECT ROUND(AVG(overall_rating), 2) as avg_rating
FROM prod_reviews.reviews
WHERE overall_rating IS NOT NULL;
```

### Metric 5: Revenue (YTD)
```sql
SELECT ROUND(SUM(total_cost), 2) as ytd_revenue
FROM prod_reservations.reservations
WHERE arrival_year = YEAR(CURRENT_DATE)
  AND is_canceled = false;
```

## Filter Configuration

### Date Range Filter
- Column: `review_date` or `arrival_date`
- Type: Time Range
- Default: Last 90 days

### Country Filter
- Column: `country`
- Type: Select Filter
- Multi-select: Yes

### Rating Filter
- Column: `overall_rating`
- Type: Range Filter
- Min: 0, Max: 10

## Dashboard Layout Tips

1. **Top Row:** KPI metrics (5 big numbers)
2. **Second Row:** Time series trends (2-3 line/area charts)
3. **Third Row:** Distribution charts (bar, pie, histogram)
4. **Bottom Row:** Detailed tables and maps

## Cross-filtering

Enable cross-filtering to allow clicking on one chart to filter others:
- Settings > Edit Dashboard > Enable Cross-filtering
