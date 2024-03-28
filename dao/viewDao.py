from entity.ViewModel import ViewType
from connectSql import dbUtil


def list(s_Name: str):
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        sql = "select * from view_list where 1=1"

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
