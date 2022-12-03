import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="python",
    passwd="python",
    database="pythonappdb"
)

cursor = connection.cursor()


def db_data(user_name, user_number):
    cursor.execute("INSERT INTO users(user_name, user_number) VALUES (%s, %s)", (user_name, user_number))
    connection.commit()
    connection.close()
