import database
mycursor = database.mydb.cursor()
#----------------------------------#
def selectdb(table):
    sql = f"SELECT * FROM {table}"
    mycursor.execute(sql)
    show = mycursor.fetchall()
    return show
#----------------------------------#
def deletedb(table,id,id_name):
    sql = f"DELETE FROM {table} WHERE {id_name} = {id}"
    mycursor.execute(sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False
##print(deletedb("products","product_id",102))
#----------------------------------#
def editdb(table,column,id_name,val):
    sql = f"UPDATE {table} SET {column} = %s WHERE {id_name} = %s"
    val_sql = (val,id_name)
    mycursor.execute(sql,val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False
##print(editdb("products","price",101,999))
#----------------------------------#
def insert_product(name):
    sql = "INSERT INTO categories VALUES (%s,%s)"
    val_sql = (None,name)
    mycursor.execute(sql,val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False
##print(insert_product("เสื้อผ้า"))
