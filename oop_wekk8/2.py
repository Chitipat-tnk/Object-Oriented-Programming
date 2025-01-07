class emoloyee:
    def __init__(self,name,job,salary):
        self.Name = name
        self.Job = job
        self.Salary = salary
    def salary1(self):
        return self.Salary * 12
       

emoloyee1 = emoloyee('โซเฟีย','ครู',12000)
emoloyee2 = emoloyee('ปีเตอร์','หมอ',45000)
emoloyee3 = emoloyee('บ๊อบ','โปรเเกรมเมอร์',40000)

print(emoloyee1.Name ,'ประกอบอาชีพ',emoloyee1.Job,'มีเงินเดือนทั้งปี = ',emoloyee1.salary1() )
print(emoloyee2.Name ,'ประกอบอาชีพ',emoloyee2.Job,'มีเงินเดือนทั้งปี = ',emoloyee2.salary1() )
print(emoloyee3.Name ,'ประกอบอาชีพ',emoloyee3.Job,'มีเงินเดือนทั้งปี = ',emoloyee3.salary1() )