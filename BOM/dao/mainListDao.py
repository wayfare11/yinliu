from entity.ComponentUpdateModel import ComponentUpdateConditionType
from connectSql import dbUtil

def list_dandao(s_ProductCode: str, s_dandaoDiameter: str, s_dandaoLength: str, s_drainageMethod: str, s_dandaoHeadStyle: str, s_dandaoConfigurationCode:str):
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        sql = "select * from dandao where 1=1"

        if s_ProductCode.strip() != '':
            sql += " AND ProductCode = '" + s_ProductCode + "'"
        if s_dandaoDiameter.strip() != '':
            sql += " AND dandaoDiameter = '" + s_dandaoDiameter + "'"
        if s_dandaoLength.strip() != '':
            sql += " AND dandaoLength = '" + s_dandaoLength + "'"
        if s_drainageMethod.strip() != '':
            sql += " AND drainageMethod = '" + s_drainageMethod + "'"
        if s_dandaoHeadStyle.strip() != '':
            sql += " AND dandaoHeadStyle = '" + s_dandaoHeadStyle + "'"
        if s_dandaoConfigurationCode.strip() != '':
            sql += " AND dandaoConfigurationCode = '" + s_dandaoConfigurationCode + "'"

        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        con.rollback()
        print(e)
        return None
    finally:
        dbUtil.closeCon(con)

def list_yinliu(s_ProductCode: str, s_yinliuDiameter: str, s_yinliuLength: str, s_yinliuLockStyle: str, s_yinliuHeadStyle: str, s_yinliuConfigurationCode:str):
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        sql = "select * from yinliu where 1=1"

        if s_ProductCode.strip() != '':
            sql += " AND ProductCode = '" + s_ProductCode + "'"
        if s_yinliuDiameter.strip() != '':
            sql += " AND yinliuDiameter = '" + s_yinliuDiameter + "'"
        if s_yinliuLength.strip() != '':
            sql += " AND yinliuLength = '" + s_yinliuLength + "'"
        if s_yinliuLockStyle.strip() != '':
            sql += " AND yinliuLockStyle = '" + s_yinliuLockStyle + "'"
        if s_yinliuHeadStyle.strip() != '':
            sql += " AND yinliuHeadStyle = '" + s_yinliuHeadStyle + "'"
        if s_yinliuConfigurationCode.strip() != '':
            sql += " AND yinliuConfigurationCode = '" + s_yinliuConfigurationCode + "'"

        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        con.rollback()
        print(e)
        return None
    finally:
        dbUtil.closeCon(con)

def list_component(s_name: str, s_materialCode: str):
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        sql = "select * from component where 1=1"

        if s_name.strip() != '':
            sql += " AND Name LIKE '%" + s_name + "%'"
        if s_materialCode.strip() != '':
            sql += " AND materialCode LIKE '%" + s_materialCode + "%'"

        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        con.rollback()
        print(e)
        return None
    finally:
        dbUtil.closeCon(con)

def list_bdc_component(s_name: str, s_majorCategory: str, s_productCode: str, s_dandaoDiameter: str, s_dandaoLength: str, s_drainageMethod: str, s_dandaoHeadStyle: str, s_dandaoConfigurationCode:str):
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()

        sql = "select * from component where 1=1"

        if s_name.strip() != '':
            sql += " AND Name LIKE '%" + s_name + "%'"
        if s_majorCategory.strip() != '':
            sql += " AND majorCategory = '" + s_majorCategory + "'"
        if s_productCode:
            sql += " AND ProductCode REGEXP '(^|,)" + s_productCode + "($|,)'"
        if s_dandaoDiameter:
            sql += " AND dandaoDiameter REGEXP '(^|,)" + s_dandaoDiameter + "($|,)'"
        if s_dandaoLength:
            sql += " AND dandaoLength REGEXP '(^|,)" + s_dandaoLength + "($|,)'"
        if s_drainageMethod:
            sql += " AND drainageMethod REGEXP '(^|,)" + s_drainageMethod + "($|,)'"
        if s_dandaoHeadStyle:
            sql += " AND dandaoHeadStyle REGEXP '(^|,)" + s_dandaoHeadStyle + "($|,)'"
        if s_dandaoConfigurationCode:
            sql += " AND dandaoConfigurationCode REGEXP '(^|,)" + s_dandaoConfigurationCode + "($|,)'"
            
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        con.rollback()
        print(e)
        return None
    finally:
        dbUtil.closeCon(con)
        
def list_dc_component(s_name:str, s_majorCategory, s_productCode: str, s_yinliuDiameter: str, s_yinliuLength: str, s_yinliuLockStyle: str, s_yinliuHeadStyle: str, s_yinliuConfigurationCode:str):
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()

        sql = "select * from component where 1=1"

        if s_name.strip() != '':
            sql += " AND Name LIKE '%" + s_name + "%'"
        if s_majorCategory.strip() != '':
            sql += " AND majorCategory = '" + s_majorCategory + "'"
        if s_productCode:
            sql += " AND ProductCode REGEXP '(^|,)" + s_productCode + "($|,)'"
        if s_yinliuDiameter:
            sql += " AND yinliuDiameter REGEXP '(^|,)" + s_yinliuDiameter + "($|,)'"
        if s_yinliuLength:
            sql += " AND yinliuLength REGEXP '(^|,)" + s_yinliuLength + "($|,)'"
        if s_yinliuLockStyle:
            sql += " AND yinliuLockStyle REGEXP '(^|,)" + s_yinliuLockStyle + "($|,)'"
        if s_yinliuHeadStyle:
            sql += " AND yinliuHeadStyle REGEXP '(^|,)" + s_yinliuHeadStyle + "($|,)'"
        if s_yinliuConfigurationCode:
            sql += " AND yinliuConfigurationCode REGEXP '(^|,)" + s_yinliuConfigurationCode + "($|,)'"
        
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        con.rollback()
        print(e)
        return None
    finally:
        dbUtil.closeCon(con)

def list_son_set(s_materialCode: str, s_name: str, s_materialSearchCode: str):
    con = None
    try:
        con = dbUtil.getCon()  # 获取数据库连接
        cursor = con.cursor()

        sql = "SELECT * FROM component WHERE materialCode != '" + s_materialCode + "'"

        if s_name.strip() != '':
            sql += " AND Name LIKE '%" + s_name + "%'"
        if s_materialSearchCode.strip() != '':
            sql += " AND materialCode LIKE '%" + s_materialSearchCode + "%'"

        cursor.execute(sql)
        return cursor.fetchall()  # 获取查询结果的所有行
    except Exception as e:
        print(e)
        return None
    finally:
        dbUtil.closeCon(con)  # 关闭数据库连接


def list_son_set_by_id(s_materialCode: str):
    con = None
    try:
        con = dbUtil.getCon()  # 获取数据库连接
        cursor = con.cursor()
        cursor.execute("SELECT * FROM component WHERE materialCode = %s", (s_materialCode,))
        return cursor.fetchall()  # 获取查询结果的第一行
    except Exception as e:
        print(e)
        return None
    finally:
        dbUtil.closeCon(con)  # 关闭数据库连接

def searchConditionById(s_materialCode: str):
    con = None
    try:
        con = dbUtil.getCon()  # 获取数据库连接
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM component where materialCode = {s_materialCode}")
        return cursor.fetchall()  # 获取查询结果的第一行
    except Exception as e:
        print(e)
        return None
    finally:
        dbUtil.closeCon(con)  # 关闭数据库连接

def search_BDC_MaterialById(s_materialCode: str):
    con = None
    try:
        con = dbUtil.getCon()  # 获取数据库连接
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM dandao where materialCode = {s_materialCode}")
        return cursor.fetchall()  # 获取查询结果的第一行
    except Exception as e:
        print(e)
        return None
    finally:
        dbUtil.closeCon(con)  # 关闭数据库连接

def search_DC_MaterialById(s_materialCode: str):
    con = None
    try:
        con = dbUtil.getCon()  # 获取数据库连接
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM yinliu where materialCode = {s_materialCode}")
        return cursor.fetchall()  # 获取查询结果的第一行
    except Exception as e:
        print(e)
        return None
    finally:
        dbUtil.closeCon(con)  # 关闭数据库连接

def updateCondaition(listType: ComponentUpdateConditionType, s_materialCode: str):
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        cursor.execute(
            f"update component set ProductCode='{listType.ProductCode}', dandaoDiameter='{listType.dandaoDiameter}', dandaoLength='{listType.dandaoLength}', drainageMethod='{listType.drainageMethod}', dandaoHeadStyle='{listType.dandaoHeadStyle}', dandaoConfigurationCode='{listType.dandaoConfigurationCode}', yinliuDiameter='{listType.yinliuDiameter}', yinliuLength='{listType.yinliuLength}', yinliuLockStyle='{listType.yinliuLockStyle}', yinliuHeadStyle='{listType.yinliuHeadStyle}', yinliuConfigurationCode='{listType.yinliuConfigurationCode}' where materialCode={s_materialCode}")
        return cursor.rowcount
    except Exception as e:
        con.rollback()
        print(e)
        return 0
    finally:
        dbUtil.closeCon(con)

def updateSonSet(s_sonSet: str, s_materialCode: str):
    con = None
    try:
        con = dbUtil.getCon()
        cursor = con.cursor()
        cursor.execute(
            "update component set subSet=%s where materialCode=%s", (s_sonSet, s_materialCode)
        )
        return cursor.rowcount
    except Exception as e:
        con.rollback()
        print(e)
        return 0
    finally:
        dbUtil.closeCon(con)