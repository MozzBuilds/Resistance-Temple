DROP TABLE bookings;
DROP TABLE sessions;
DROP TABLE customers;

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    forename VARCHAR,
    surname VARCHAR,
    alias VARCHAR,
    membership_status BOOLEAN,
    membership_type VARCHAR
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
    customer_id INT REFERENCES customers(id) ON DELETE CASCADE,
    session_id INT REFERENCES sessions(id) ON DELETE CASCADE,
    review TEXT
);