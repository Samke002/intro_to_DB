import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Establish connection to the MySQL server
        # Replace 'your_username' and 'your_password' with your credentials
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create the database without using SELECT or SHOW
            # IF NOT EXISTS prevents the script from failing if it already exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Handling connection and execution errors
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Handle closing the database connection and cursor
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
