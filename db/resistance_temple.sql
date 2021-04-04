DROP TABLE bookings;
DROP TABLE sessions;
DROP TABLE customers;

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    forename VARCHAR,
    surname VARCHAR,
    alias VARCHAR,
    membership_status VARCHAR,
    membership_type VARCHAR
    -- monthly_sessions_had INT
);

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    type VARCHAR,
    date VARCHAR,
    start_time VARCHAR,
    end_time VARCHAR,
    capacity INT
    -- finished/in the past BOOLEAN
    -- room VARCHAR
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id) ON DELETE CASCADE,
    session_id INT REFERENCES sessions(id) ON DELETE CASCADE,
    review TEXT
);
-- To delete a customer OR a session, I need to have ON DELETE CASCADE at the end of lines 28 and 29
-- However
-- When I delete a booking, this then deletes the customer