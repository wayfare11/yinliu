from entity.ViewModel import ViewType
from entity.ViewEditModel import ViewEditType
from connectSql import dbUtil


def list(s_Name: str, id):
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        sql = "select * from view_list where 1=1"

        if s_Name.strip() != '':
            sql += " and Name like '%" + s_Name + "%' "

        # 添加额外的约束条件
        sql += " and id_list = " + str(id)

        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        con.rollback()
        print(e)
        return None
    finally:
        dbUtil.closeCon(con)

def delete(ids):
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        for id in ids:
            cursor.execute(
                f"delete from view_list where id={id}")
        con.commit()
        return len(ids)  # 返回成功删除的记录数
    except Exception as e:
        con.rollback()
        print(e)
        return 0
    finally:
        dbUtil.closeCon(con)

def add(view: ViewType):
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        cursor.execute(f"insert into view_list values(null,'{view.id_list}','{view.MaterialCode}','{view.DrawingCode}','{view.Name}','{view.ProductSize}','{view.Material}','{view.Color}','{view.Quantity}','{view.Unit}','{view.MaterialCategory}','{view.Note}')")
        return cursor.rowcount
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
        cursor.execute(f"SELECT * FROM view_list where id = {id}")
        return cursor.fetchall()  # 获取查询结果的第一行
    except Exception as e:
        print(e)
        return None
    finally:
        dbUtil.closeCon(con)  # 关闭数据库连接

def update(viewType: ViewEditType, id):
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        cursor.execute(
            f"update view_list set MaterialCode='{viewType.MaterialCode}', DrawingCode='{viewType.DrawingCode}', Name='{viewType.Name}', ProductSize='{viewType.ProductSize}', Material='{viewType.Material}', Color='{viewType.Color}', Quantity='{viewType.Quantity}', Unit='{viewType.Unit}', MaterialCategory='{viewType.MaterialCategory}', Note='{viewType.Note}' where id={id}")
        return cursor.rowcount
    except Exception as e:
        con.rollback()
        print(e)
        return 0
    finally:
        dbUtil.closeCon(con)