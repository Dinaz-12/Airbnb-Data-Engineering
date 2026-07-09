CREATE TABLE dim_host (
    host_id BIGINT PRIMARY KEY,
    host_name VARCHAR,
    host_location VARCHAR,
    host_is_superhost BOOLEAN,
    host_listings_count INTEGER
);

CREATE TABLE dim_location (
    location_id INTEGER PRIMARY KEY,
    neighbourhood VARCHAR,
    latitude DOUBLE,
    longitude DOUBLE
);

CREATE TABLE dim_review (
    review_id INTEGER PRIMARY KEY,
    review_score DOUBLE,
    reviews_per_month DOUBLE,
    number_of_reviews INTEGER
);

CREATE TABLE fact_listings (
    listing_id BIGINT PRIMARY KEY,
    host_id BIGINT,
    location_id INTEGER,
    review_id INTEGER,
    price DOUBLE,
    occupancy_rate DOUBLE,
    estimated_revenue DOUBLE
);