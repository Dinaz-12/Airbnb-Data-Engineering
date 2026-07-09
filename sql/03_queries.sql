-- Query 1
SELECT COUNT(*) AS total_listings
FROM fact_listings;


-- Query 2
SELECT
room_type,
COUNT(*) AS total_listings
FROM fact_listings
GROUP BY room_type
ORDER BY total_listings DESC;


-- Query 3
SELECT
room_type,
ROUND(AVG(price),2) AS average_price
FROM fact_listings
GROUP BY room_type
ORDER BY average_price DESC;


-- Query 4
SELECT
property_type,
COUNT(*) AS total
FROM fact_listings
GROUP BY property_type
ORDER BY total DESC;

-- Query 5
SELECT
listing_name,
price
FROM fact_listings
ORDER BY price DESC
LIMIT 10;

-- Query 6
SELECT
dh.host_name,
COUNT(*) AS listings
FROM fact_listings f
JOIN dim_host dh
ON f.host_key = dh.host_key
GROUP BY dh.host_name
ORDER BY listings DESC
LIMIT 10;


-- Query 7
SELECT
dl.neighbourhood,
ROUND(AVG(f.price),2) AS avg_price
FROM fact_listings f
JOIN dim_location dl
ON f.location_key = dl.location_key
GROUP BY dl.neighbourhood
ORDER BY avg_price DESC
LIMIT 10;


-- Query 8
SELECT
dh.is_superhost,
ROUND(AVG(f.price),2) AS avg_price
FROM fact_listings f
JOIN dim_host dh
ON f.host_key = dh.host_key
GROUP BY dh.is_superhost;


-- Query 9
SELECT
review_scores_rating,
COUNT(*)
FROM fact_listings
GROUP BY review_scores_rating
ORDER BY review_scores_rating DESC;


-- Query 10
SELECT
listing_name,
price * availability_365 AS estimated_revenue
FROM fact_listings
ORDER BY estimated_revenue DESC
LIMIT 10;


