import mysql.connector
from mysql.connector import Error

def connect_and_create_db():
    """
    Connects to MySQL server and creates the database alx_book_store.
    Handles errors and ensures the connection is closed.
    """
    connection = None
    try:
        # Connect to the MySQL Server
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',  # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database command (IF NOT EXISTS handles the 'no fail' requirement)
            # No SELECT or SHOW statements are used here.
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Standard error handling as requested
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Handle the closing of the DB connection and cursor
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    connect_and_create_db()
