name = input('โปรดกรอกชื่อ : ')
age = (input('โปรดกรอกอายุ : '))
id = input('โปรดกรอกรหัสประจำตัวนักศึกษา : ')
Year = input('โปรดกรอกชั้นปี : ')
NickName = input('โปรดกรอกชื่อเล่น : ')
Height = int(input('โปรดกรอกส่วนสูง : '))
W = int(input('โปรดกรอกน้ำหนัก : '))
Value = Height + W

print(f"ชื่อ : {name} อายุ {age}   ปี")
print(f'รหัสประจำตัวนักศึกษา : {id} ระดับชั้น : {Year}')
print(f'ชื่อเล่น {NickName}')
print(f"ส่วนสูง : {Height}  น้ำหนัก {W}  กิโลกรัม" )
print(f'ส่วนสูง + น้ำหนัก =  {Value}')
