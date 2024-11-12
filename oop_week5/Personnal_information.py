Value = int(input('จำนวนคนที่จะป้อน : '))
Sum = {}
for i in range(Value):
    print(f'กรุณากรอกคนที่ : {i}' )
    Sum['name'] = str(input('กรุณากรอกชื่อ : '))
    Sum['NickName'] = str(input('กรุณากรอกชื่อเล่น : '))
    Sum['id'] = str(input('กรุณากรอกเลขประจำตัว : '))
    Sum['hobby'] = str(input('กรุณากรอกงานอดิเรก : '))
    Sum['age'] = str(input('กรุณากรอกอายุ : '))
    print(f'ข้อมูลคนที่ {i+1}')
    print(f'{Sum}')

    