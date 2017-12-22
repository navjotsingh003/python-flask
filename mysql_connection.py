#!/usr/bin/python
from pymysql import connect, cursors

def create_connection():
    connection = connect(host='localhost',
                             user='root',
                             password='',
                             charset='utf8mb4',
                             cursorclass=cursors.DictCursor)
    return connection
