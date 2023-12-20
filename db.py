import psycopg2

db_config = {
    "database": "restaurant5",
    "user": "postgres",
    "password": "0000",
    "host": "localhost",
    "port": "5432"
}

def get_db_connection():
    return psycopg2.connect(**db_config)

def check_booking(new_first_name, new_last_name, new_num_people, new_date, new_time):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            SELECT * FROM bookings WHERE first_name=%s AND last_name=%s AND num_people=%s AND date = %s AND time = %s;
            """
        cursor.execute(query, (new_first_name, new_last_name, new_num_people, new_date, new_time))
        options = cursor.fetchall()
        conn.close()
        return options
    except Exception as e:
        return f"An error occurred: {str(e)}"

def insert_new_booking(new_first_name, new_last_name, new_num_people, new_date, new_time):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO bookings (first_name, last_name, num_people, date, time) VALUES (%s, %s, %s, %s, %s);
            """
        cursor.execute(query, (new_first_name, new_last_name, new_num_people, new_date, new_time))
        conn.commit()  # Commit the transaction after an INSERT
        conn.close()
        return "Booking successfully inserted."
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
def get_all_bookings():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            SELECT * FROM bookings;
            """
        cursor.execute(query)
        options = cursor.fetchall()
        conn.close()
        return options
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
def get_booking(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            SELECT * FROM bookings where id=%s;
            """
        cursor.execute(query,(id,))
        options = cursor.fetchall()
        conn.close()
        return options
    except Exception as e:
        return f"An error occurred: {str(e)}"

def delete_booking(id):
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
    
def update_booking(id, new_first_name, new_last_name, new_num_people, new_date, new_time):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            UPDATE bookings
            SET first_name=%s, last_name=%s, num_people=%s, date=%s, time=%s
            WHERE id=%s;
        """
        cursor.execute(query, (new_first_name, new_last_name, new_num_people, new_date, new_time, id))
        conn.commit()
        conn.close()
        return "Booking successfully updated."
    except Exception as e:
        return f"An error occurred: {str(e)}"
