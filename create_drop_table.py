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

if __name__ == "__main__":
    a = checkTableExists('')
    if a:
        print("table alrteady exist")
    else:
        create_table('')
if __name__ == "__main__":
    dropTable('')