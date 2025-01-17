import mysql.connector
class Managerdb:
    def __init__(self, host, user, password, database):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.mycursor = self.mydb.cursor()

    def selectdb(self, table):
        sql = f"SELECT * FROM {table}"
        self.mycursor.execute(sql) 
        show = self.mycursor.fetchall()
        return show
    
#--------------------------------------------------------------------------------# 
#    
    def deletdb(self,table, id, id_name):
        sql = f"DELETE FROM {table} WHERE {id_name} = {id}"
        self.mycursor.execute(sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False
        
#--------------------------------------------------------------------------------# 

    def editdb(self, table, column, id_name,id,val):
        sql = f"UPDATE {table} SET {column} = %s WHERE {id_name} = %s"
        val_sql = (val,id)
        self.mycursor.execute(sql, val_sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False
#--------------------------------------------------------------------------------

    def insert_categories(self, name):
        sql = "INSERT INTO categories (category_id,category_name) VALUES (%s, %s)"
        val_sql = (None, name)
        self.mycursor.execute(sql, val_sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False 
        
    def insert_user(self, name,password,email,role_user):
        sql = "INSERT INTO user VALUES (%s,%s,%s,%s,%s)"
        val_sql = (None, name,password,email,role_user)
        self.mycursor.execute(sql, val_sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False
        
    def insert_orders(self,user_id,order_date,total_amount,status):
        sql = "INSERT INTO orders VALUES (%s,%s,%s,%s,%s)"
        val_sql = (None,user_id,order_date,total_amount,status)
        self.mycursor.execute(sql, val_sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False
        
    def insert_product(self,product_name,description,price,stock):
        sql = "INSERT INTO product VALUES (%s, %s, %s, %s, %s)"
        val_sql = (None, product_name,description,price,stock)
        self.mycursor.execute(sql, val_sql)
        self.mydb.commit()
        if self.mycursor.rowcount > 0:
            return True
        else:
            return False
#--------------------------------------------------------------------------------
result_select = Managerdb('localhost','root','Nice0145','shop')

#ลบ
#print(result_select.deletdb('products', 'product_id', 102))

#เรียกดู
#print(result_select.selectdb('products'))

#เเก้ไข
#print(result_select.editdb('categories', 'category_name', 'category_id', 103, 'เสื้อผ้า'))

#เพิ่มข้อมูล
print(result_select.insert_categories('เสื้อผ้า'))