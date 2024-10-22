name = input('โปรดกรอกชื่อ : ')
age = (input('โปรดกรอกอายุ : '))
id = input('โปรดกรอกรหัสประจำตัวนักศึกษา : ')
Year = input('โปรดกรอกชั้นปี : ')
NickName = input('โปรดกรอกชื่อเล่น : ')
Height = int(input('โปรดกรอกส่วนสูง : '))
W = int(input('โปรดกรอกน้ำหนัก : '))
Value = Height + W

print("ชื่อ : " + name + " อายุ "+ age + " ปี")
print('รหัสประจำตัวนักศึกษา : ' +id,' ระดับชั้น : '+Year)
print('ชื่อเล่น '+NickName)
print("ส่วนสูง : " + str(Height) + "  น้ำหนัก "+ str(W) + "  กิโลกรัม" )
print('ส่วนสูง + น้ำหนัก = '+ str(Value))
