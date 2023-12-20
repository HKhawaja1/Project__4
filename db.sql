CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    num_people INTEGER CHECK (num_people >= 0 AND num_people <= 20) NOT NULL,
    date DATE NOT NULL,
    time TIME NOT NULL
);
