import mysql.connector

def get_connection():
    connection = mysql.connector.connect(host='localhost',
                                         database='test',
                                         user='root',
                                         password='12345678')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def read_database_version():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM hospital;")
        db_version = cursor.fetchall()
        print("You are connected to MySQL version: ", db_version)
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

print("Question 1: Print Database version")
read_database_version()
