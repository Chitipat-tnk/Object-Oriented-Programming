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

    def Check_product(self):
        print(f"Product-Name: {self.name}")
        print(f"Prices: {self.__prices}")
        print(f"Stock: {self.__stock}")

product1 = Product("Chitipat")
product1.add_price(1000)
product1.add_stock(20)
product1.remove_stock(15)
product1.Check_product()
print("------------------------")
product2 = Product("ไออ๊อฟ")
product2.add_price(20000)
product2.add_stock(50)
product2.remove_stock(25)
product2.Check_product()


