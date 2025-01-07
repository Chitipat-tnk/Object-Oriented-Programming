class Pay:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount >= 100:
            self.balance += amount
        else:
            print('ฝากมากกว่า 100')

    def withdraw(self, amount):
        if amount >= 100 and amount <= self.balance:
            self.balance -= amount
        else:
            print('ใส่จำนวนที่ถูกต้อง')

    def showbalance(self):
        print(self.balance)
        return self.balance

Pay1 = Pay(1, "Nice", 1000)

Pay1.deposit(500)
Pay1.withdraw(1000)
print(Pay1.id, Pay1.name, Pay1.showbalance())
