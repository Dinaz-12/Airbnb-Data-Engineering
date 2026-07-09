#Query 1 - Total Listings
SELECT COUNT(*) AS total_listings
FROM listings;


# Query 2 - Average Price
SELECT
ROUND(AVG(price),2) AS average_price
FROM listings;


# Query 3 - Average Price by Room Type
SELECT
room_type,
COUNT(*) AS total_listings,
ROUND(AVG(price),2) AS average_price
FROM listings
GROUP BY room_type
ORDER BY average_price DESC;


# Query 4 - Property Types
SELECT
property_type,
COUNT(*) AS total
FROM listings
GROUP BY property_type
ORDER BY total DESC;

# Query 5 - Top 10 Expensive Listings
SELECT
name,
price
FROM listings
ORDER BY price DESC
LIMIT 10;


# Query 6 - Top Hosts
SELECT
host_name,
host_listings_count
FROM listings
ORDER BY host_listings_count DESC
LIMIT 10;


# Query 7 - Neighbourhood Analysis
SELECT
neighbourhood_cleansed,
COUNT(*) AS listings,
ROUND(AVG(price),2) AS average_price
FROM listings
GROUP BY neighbourhood_cleansed
ORDER BY average_price DESC;


# Query 8 - Superhost Analysis
SELECT
host_is_superhost,
COUNT(*) AS total_hosts,
ROUND(AVG(price),2) AS average_price
FROM listings
GROUP BY host_is_superhost;


# Query 9 - Review Analysis
SELECT
ROUND(AVG(review_scores_rating),2) AS average_rating,
ROUND(AVG(number_of_reviews),2) AS average_reviews
FROM listings;


# Query 10 - Occupancy Analysis
SELECT
ROUND(AVG(occupancy_rate),2) AS average_occupancy_rate,
ROUND(AVG(estimated_revenue_l365d),2) AS average_estimated_revenue
FROM listings;


