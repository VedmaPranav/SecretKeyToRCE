import mysql.connector
from datetime import datetime
from config import mysql_host,mysql_password



def mysqlconnect():
    # To connect MySQL database
    conn = None
    try:
        conn = mysql.connector.connect(host=mysql_host, user='root', password= mysql_password, db='Mock_data_db')
    except mysql.connector.Error as error:
        print(error)
    return conn


def get_data_db():
    try:
        conn = mysqlconnect()
        cur = conn.cursor(prepared=True)
        query = "select * from MOCK_DATA"
        cur.execute(query)
        return cur.fetchall()
    except mysql.connector.Error as error:
        print(error)