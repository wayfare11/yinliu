from pymysql import Connection

def getCon():
    """
    获取数据库连接
    :return:
    """
    con = Connection(
        host="localhost",  # 主机名
        port=3306,  # 端口
        user="root",  # 账号
        password="123456",  # 密码
        database="yinliu",  # 数据库
        autocommit=True  # 设置自动提交
    )
    return con


def closeCon(con: Connection):
    """
    关闭数据库连接
    :param con:
    :return:
    """
    if con:
        con.close()

if __name__ == '__main__':
    con = None
    try:
        con = getCon()
        cursor = con.cursor()
        cursor.execute("select * from yinliu_home")
        print(cursor.fetchall())
    except Exception as e:
        print(e)
    finally:
        closeCon(con)