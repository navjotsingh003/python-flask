from pymysql import connect, cursors

def create_connection():
    connection = connect(host='localhost',
                             user='root',
                             password='',
                             charset='utf8mb4',
                             cursorclass=cursors.DictCursor)
    return connection

def create_database(db_name):
    connection = create_connection()
    cursor = connection.cursor()
    sql = 'Create Database %s'%(db_name)
    cursor.execute(sql)
    connection.commit()

if __name__ == "__main__":
    create_database('db_name')
