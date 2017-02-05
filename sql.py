"""
一般 Python 用于连接 MySQL 的工具：pymysql
"""
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123',
                             db='mid_DB',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# cursor = connection.cursor()

# store the encrypted mid
def insert_mid(mid, encrypted_mid):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `mid_DB` (`mid`, `encrypted_mid`) VALUES (%s, %s)"
        cursor.execute(sql, (mid, encrypted_mid))
        connection.commit()


def dis_connect():
    connection.close()