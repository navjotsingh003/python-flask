def read_table(table_name):
    connection = create_connection()
    cursor = connection.cursor()
    sql_statement = "Select * from %s"%(table_name)
    cursor.execute(sql_statement)

    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()
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

if __name__ == "__main__":
    read_table('nav2')
if __name__ == "__main__":
    insert_entry('nav2', 'Bains', 19, 'bbbbbbb@gmail.com')
if __name__ == "__main__":
    delete_entry('nav2','4')
if __name__ == "__main__":
    update_entry('nav2', "Bains", 25, "navjotsingh003@gmail.com", 3)