print("aa")
################################
'''checking mysql server connection'''
import mysql.connector
# Replace these values with your database credentials
host = "localhost"
user = "root"
password = "Switch@2023"
database = "Databasename01"
try:
    # Establish a database connection
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    if connection.is_connected():
        print("Connected to the database")
        # Create a cursor object to interact with the database
        cursor = connection.cursor()
        # Example: Execute a simple query
        cursor.execute("SELECT * FROM MOCK_DATA")
        # Fetch and print the results
        rows = cursor.fetchall()
        for row in rows:
            print(row)
except mysql.connector.Error as error:
    print("Error:", error)
finally:
    # Close the cursor and the connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed")

'''if 'cursor' in locals(): cursor.close(): This line checks if a variable named cursor 
exists in the local scope (i.e., it was defined earlier in the program). If it exists, 
it means that a database cursor was created, and this line calls the close() method on the 
cursor to close it. Closing the cursor is important to release associated resources and to 
ensure that it won't be used further.'''

'''if 'connection' in locals() and connection.is_connected(): connection.close(): This line first 
checks if a variable named connection exists in the local scope and also if the connection is currently 
connected (i.e., the is_connected() method returns True). If both conditions are met, it means that a 
database connection was established and it's still open. In that case, this line calls the close() method 
on the connection to close it. Closing the connection is essential to release resources and properly terminate 
the database connection.'''
