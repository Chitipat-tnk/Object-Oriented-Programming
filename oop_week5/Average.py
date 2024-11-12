sum1 = int(input('ใส่จำนวนค่า : '))
num = []
for i in range(sum1):
    num1 = int(input('ใส่ค่า : '))
    num.append(num1)
Value = (sum(num) // len(num))
print(Value)
