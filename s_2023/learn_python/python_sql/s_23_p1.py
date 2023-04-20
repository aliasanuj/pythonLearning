import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password
        )
        print("MYSQL is successfull connected")

    except Error as err:
        print(f"Erros is :{err}")

    return connection


pw = "Root@2022"
db = ""
db =



















