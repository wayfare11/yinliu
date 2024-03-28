from entity.ListModel import ListType
from connectSql import dbUtil

def add(listType: ListType):
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        cursor.execute(f"insert into yinliu_home values(null,'{listType.Name}','{listType.FileCode}','{listType.VersionCode}','{listType.ProductSize}','{listType.ProductCode}','{listType.DandaoSize}','{listType.DandaoStyle}','{listType.DandaoCode}','{listType.YinliuSize}','{listType.YinliuLock}','{listType.YinliuStyle}','{listType.YinliuCode}','{listType.MaterialCode}')")
        return cursor.rowcount
    except Exception as e:
        con.rollback()
        print(e)
        return 0
    finally:
        dbUtil.closeCon(con)
 


def list(s_Name: str):
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        sql = "select id, Name, FileCode, VersionCode, ProductSize, MaterialCode from yinliu_home where 1=1"

        if s_Name.strip() != '':
            sql += " and Name like '%" + s_Name + "%' "
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        con.rollback()
        print(e)
        return None
    finally:
        dbUtil.closeCon(con)

def update(listType: ListType, id):
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        cursor.execute(
            f"update yinliu_home set Name='{listType.Name}', FileCode='{listType.FileCode}', VersionCode='{listType.VersionCode}', ProductSize='{listType.ProductSize}', ProductCode='{listType.ProductCode}', DandaoSize='{listType.DandaoSize}', DandaoStyle='{listType.DandaoStyle}', DandaoCode='{listType.DandaoCode}', YinliuSize='{listType.YinliuSize}', YinliuLock='{listType.YinliuLock}', YinliuStyle='{listType.YinliuStyle}', YinliuCode='{listType.YinliuCode}', MaterialCode='{listType.MaterialCode}' where id={id}")
        return cursor.rowcount
    except Exception as e:
        con.rollback()
        print(e)
        return 0
    finally:
        dbUtil.closeCon(con)

def delete(ids):
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        for id in ids:
            cursor.execute(
                f"delete from yinliu_home where id={id}")
        con.commit()
        return len(ids)  # 返回成功删除的记录数
    except Exception as e:
        con.rollback()
        print(e)
        return 0
    finally:
        dbUtil.closeCon(con)

def searchById(id):
    con = None
    try:
        con = dbUtil.getCon()  # 获取数据库连接
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM yinliu_home where id = {id}")
        return cursor.fetchall()  # 获取查询结果的第一行
    except Exception as e:
        print(e)
        return None
    finally:
        dbUtil.closeCon(con)  # 关闭数据库连接

