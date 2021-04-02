DROP TABLE bookings;
DROP TABLE sessions;
DROP TABLE customers;

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR
    -- membership_type VARCHAR
    -- membership_status BOOLEAN
    -- monthly_sessions_had INT
);

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    type VARCHAR,
    date VARCHAR,
    start_time VARCHAR,
    end_time VARCHAR
    -- finished BOOLEAN
    -- room VARCHAR
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    session_id INT REFERENCES sessions(id),
    review TEXT
);