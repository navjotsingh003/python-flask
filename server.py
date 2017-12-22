from pymysql import connect, cursors, Error
from flask import Flask, g
from db import mysql_connection

app = Flask(__name__)

@app.route('/checktable/<string:tablename>')
def checkTableExists(tablename):
    try:
        connection = mysql_connection.create_connection()
        cursor = connection.cursor()
        stmt = "SHOW TABLES LIKE '%s'"%(tablename)
        cursor.execute(stmt)
        print(cursor.fetchone())
        a=cursor.fetchone()
        if a:
            cursor.close()
            return True
        cursor.close()
        return False
    except (Error, Exception) as e:
        print("Error occured %s"%e)

@app.route('/')
def welcome():
    return "Welcome"

@app.route("/create/<string:table_name>" ,methods = ["GET","POST"])
def create_table(table_name):
    try:
        connection = mysql_connection.create_connection()
        cursor = connection.cursor()
        sql_statement = """Create Table %s (ID int auto_increment Primary Key, lastname VARCHAR(255), age int,
                        email VARCHAR(255))""" %(table_name)
        cursor.execute(sql_statement)
        connection.commit()
        data ={"table": "%s created" %(table_name)}
    except (Error, Exception) as e:
        print("Error occured %s"%e)
        data = {"Error": e}
    return data

@app.route("/drop/<string:tableName>")
def dropTable(tableName):
    try:
        connection = mysql_connection.create_connection()
        cursor = connection.cursor()
        sql_statement = "Drop Table %s" % (tableName)
        cursor.execute(sql_statement)
        connection.commit()
        data = {"table": "%s dropped"%(tableName)}
    except (Error, Exception) as e:
        print("Error occured %s"%e)
        data = {"Error": e}
    return data

@app.route("/insert/<string:last_name>/<int:ages>/<string:email_id>")
def insert_entry(last_name,ages,email_id):
    try:
        connection = mysql_connection.create_connection()
        cursor = connection.cursor()
        sql_statement = "Insert into %s (lastname,age,email) Values ('%s',%d,'%s')" %(table_namee,last_name,ages,email_id)
        cursor.execute(sql_statement)
        connection.commit()
        data = {"inserted entry": "%s %d %s"%(last_name,ages,email_id)}
    except (Error, Exception) as e:
        print("Error occured %s"%e )
        data = {"Error": e}
    return data

@app.route("/delete/<int:id_no>")
def delete_entry(id_no):
    try:
        connection = mysql_connection.create_connection()
        cursor = connection.cursor()
        sql_staement = "Delete from nav2 where id= %s"%(id_no)
        cursor.execute(sql_staement)
        connection.commit()
        data = {"entry": "%d deleted"%(id_no)}
    except (Error, Exception) as e:
        print("Error occured %s"%e)
        data = {"Error": e}
    return data

@app.route("/update/<string:last_name>/<int:ages>/<string:email_id>/<int:ids>")
def update_entry(last_name, ages, email_id, ids):
    try:
        connection = mysql_connection.create_connection()
        cursor = connection.cursor()
        sql_statement = "UPDATE nav2 SET lastname= '%s', age = %d, email= '%s' where id = %d" %(last_name, ages, email_id, ids)
        cursor.execute(sql_statement)
        connection.commit()
        data = {"deleted entryid": "%d"%(ids)}
    except (Error, Exception) as e:
        print("Error occured %s"%e)
        data = {"Error": e}
    return data


if __name__ == "__main__":
    app.run()
