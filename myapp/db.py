import os
import psycopg2

# Load Environment Variables From .env File
from dotenv import load_dotenv
load_dotenv()

# Details For Connecting To PostgreSQL Database
db_config = {
    "database": os.environ.get("DATABASE_NAME"),
    "user": os.environ.get("DATABASE_USER"),
    "password": os.environ.get("DATABASE_PASSWORD"),
    "host": os.environ.get("DATABASE_HOST"),
    "port": os.environ.get("DATABASE_PORT")
}


# Connects To Database Using Provided Details
def get_db_connection():
    return psycopg2.connect(**db_config)


# Checks If Bookings Already Exists
def db_check_booking(
        new_first_name,
        new_last_name,
        new_num_people,
        new_date,
        new_time,
        username):
    try:
        conn = get_db_connection()  # Starts New Database Connection
        cursor = conn.cursor()
        query = """
            SELECT * FROM bookings
            WHERE first_name=%s AND
            last_name=%s AND
            num_people=%s AND
            date = %s AND
            time = %s AND
            userd = %s;
                """
        cursor.execute(query, (new_first_name, new_last_name,
                       new_num_people, new_date, new_time, username))
        options = cursor.fetchall()
        conn.close()  # Closes Database Connection
        return options
    except Exception as e:
        return f"An error occurred: {str(e)}"


# Inserts New Booking Into Database
def db_insert_new_booking(
        new_first_name,
        new_last_name,
        new_num_people,
        new_date,
        new_time,
        username):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO bookings
            (first_name, last_name, num_people, date, time, userd)
            VALUES (%s, %s, %s, %s, %s, %s);
                """
        cursor.execute(query, (new_first_name, new_last_name,
                       new_num_people, new_date, new_time, username))
        conn.commit()  # Commits Transaction
        conn.close()
        return "Booking successfully inserted."
    except Exception as e:
        return f"An error occurred: {str(e)}"


# Retrieves Bookings From User
def db_get_all_bookings(username):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            SELECT * FROM bookings where userd = %s;
                """
        cursor.execute(query, (username,))
        options = cursor.fetchall()
        conn.close()
        return options
    except Exception as e:
        return f"An error occurred: {str(e)}"


# Retrieves Booking From ID
def db_get_booking(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            SELECT * FROM bookings where id=%s;
                """
        cursor.execute(query, (id,))
        options = cursor.fetchall()
        conn.close()
        return options
    except Exception as e:
        return f"An error occurred: {str(e)}"


# Deletes Booking From Database By Its ID
def db_delete_booking(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            DELETE FROM bookings WHERE id=%s;
                """
        cursor.execute(query, (id,))
        conn.commit()
        conn.close()
        return "Booking successfully deleted."
    except Exception as e:
        return f"An error occurred: {str(e)}"


# Updates Existing Booking In Database
def db_update_booking(
        id,
        new_first_name,
        new_last_name,
        new_num_people,
        new_date,
        new_time):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            UPDATE bookings
            SET first_name=%s, last_name=%s, num_people=%s, date=%s, time=%s
            WHERE id=%s;
            """
        cursor.execute(query, (new_first_name, new_last_name,
                       new_num_people, new_date, new_time, id))
        conn.commit()
        conn.close()
        return "Booking successfully updated."
    except Exception as e:
        return f"An error occurred: {str(e)}"
