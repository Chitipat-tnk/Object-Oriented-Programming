b = 0
while True:
    value = str(input('กรุณาใส่ค่า : '))
    if value =='หยุด':
        break
    try:
        c = int(value)
        if c > 0:
            b += c
            print(f'ผลรวมตอนนี้ = {b}')
        if c == 0:
            raise ZeroDivisionError
        elif c < 0:
            raise Exception
    except ZeroDivisionError:
        print('ห้ามใส่ 0 ')
    except ValueError :
        print('ห้ามใส่ตัวอักษร')
    except:
        print('ห้ามใส่ติดลบ')