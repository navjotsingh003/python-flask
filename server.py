from pymysql import connect, cursors
import db

def create_connection():
    connection = connect(host='localhost',
                             user='root',
                             password='',
                             db='database007',
                             charset='utf8mb4',
                             cursorclass=cursors.DictCursor)
    return connection

def checkTableExists(tablename):
    connection = create_connection()
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

def create_table(table_name):
    connection = create_connection()
    cursor = connection.cursor()
    sql_statement = """Create Table %s (ID int auto_increment Primary Key, lastname VARCHAR(255), age int,
                    email VARCHAR(255))""" %(table_name)
    cursor.execute(sql_statement)
    connection.commit()

def dropTable(tableName):
    connection = create_connection()
    cursor = connection.cursor()
    sql_statement = "Drop Table %s" % (tableName)
    cursor.execute(sql_statement)
    connection.commit()

def insert_entry(table_namee,last_name,ages,email_id):
    connection = create_connection()
    cursor = connection.cursor()
    sql_statement = "Insert into %s (lastname,age,email) Values ('%s',%d,'%s')" %(table_namee,last_name,ages,email_id)
    cursor.execute(sql_statement)
    connection.commit()

def delete_entry(table_name,id_no):
    connection = create_connection()
    cursor = connection.cursor()
    sql_staement = "Delete from %s where id= %s"%(table_name,id_no)
    cursor.execute(sql_staement)
    connection.commit()

def update_entry(table_name, last_name, ages, email_id, ids):
    connection = create_connection()
    cursor = connection.cursor()
    sql_statement = "UPDATE %s SET lastname= '%s', age = %d, email= '%s' where id = %d" %(table_name, last_name, ages, email_id, ids)
    cursor.execute(sql_statement)
    connection.commit()

#if __name__ == "__main__":
#    a = checkTableExists('na')
#    if a:
#        print("table alrteady exist")
#    else:
#        create_table('fff')

#if __name__ == "__main__":
#    dropTable('nnnn')
#if __name__ == "__main__":
#    insert_entry('nav2', 'Bains', 19, 'bbbbbbb@gmail.com')
#if __name__ == "__main__":
#    delete_entry('nav2','4')
#if __name__ == "__main__":
#    update_entry('nav2', "Bains", 25, "navjotsingh003@gmail.com", 3)
