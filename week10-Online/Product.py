class Product:
    def __init__(self, name):
        self.name = name 
        self.__prices = [] 
        self.__stock = []

    def add_price(self, price):
        if price > 0:
            self.__prices.append(price)
        else:
            print("ราคาไม่ถูกต้อง")

    def add_stock(self, amount):
        if amount > 0:
            self.__stock.append(amount)
        else:
            print("จำนวนไม่ถูกต้อง")

    def remove_stock(self, amount):
        if amount > 0 :
            self.__stock[0] -= amount
        else:
            print("จำนวนไม่ถูกต้อง")

    def check_product(self):
        return f"Product-Name: {self.name}\nPrices: {self.__prices}\nStock: {self.__stock}"

class Phone(Product):
    def __init__(self, name, category):
        super().__init__(name)
        self.category = category

    def check_product(self):
        base_info = super().check_product()
        return f"หมวดหมู่: {self.category}\n{base_info}"
    
class Notebook(Product):
    def __init__(self, name, category):
        super().__init__(name)
        self.category = category

    def check_product(self):
        base_info = super().check_product()
        return f"หมวดหมู่: {self.category}\n{base_info}"
    
class Clothes(Product):
    def __init__(self, name, category):
        super().__init__(name)
        self.category = category

    def check_product(self):
        base_info = super().check_product()
        return f"หมวดหมู่: {self.category}\n{base_info}"
    
product1 = Product("Chitipat")
product1.add_price(100000)
product1.add_stock(50)

phone1 = Phone("iPhone 15", "Smartphone")
phone1.add_price(45000)
phone1.add_stock(25)

Notebook2 = Notebook("Acer", "Notebook")
Notebook2.add_price(22000)
Notebook2.add_stock(20)

Clothes1 = Clothes("T-เชิ้ต", "Clothes")
Clothes1.add_price(290)
Clothes1.add_stock(5)

print(product1.check_product())
print('-------------------------------------------------------')
print(phone1.check_product())
print('-------------------------------------------------------')
print(Notebook2.check_product())
print('-------------------------------------------------------')
print(Clothes1.check_product())


