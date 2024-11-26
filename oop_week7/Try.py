try:    
    while True:
        print('โปรเเกรมหาพื้นที่สี่เหลี่ยม')
        width = int(input('กรอกความกว้าง : '))
        length = int(input('กรอกความยาว : '))
        ans = width * length
        if width == 0 or length == 0 :
            raise ZeroDivisionError
        elif width < 0 or length <0:
            raise Exception
        print(f'ค่าของพื้นที่สี่เหลี่ยม = {ans}')

        print('----------------------------------------')
        print('โปรเเกรมหาพื้นที่สามเหลี่ยม ')
        base = int(input('กรุณากรอกฐาน :'))
        height = int(input('กรุณากรอกความสูง :'))
        ans1 = base * height
        if base == 0 or height == 0 :
            raise ZeroDivisionError
        elif base < 0 or height <0:
            raise Exception
        print(f'ค่าของพื้นที่สามเหลี่ยม = {ans1}')

        print('----------------------------------------')
        print('โปรเเกรมหาวงกลม')
        r = int(input('กรุณากรอกฐาน :'))
        ans2 = 3.14*(r**2) 
        if r == 0 :
            raise ZeroDivisionError
        elif r < 0 :
            raise Exception
        print(f'ค่าของพื้นที่วงกลม = {ans2}') 
except ValueError:
    print('กรอกได้เเค่ตัวเลข')
    
except ZeroDivisionError:
    print('ห้ามใส่ 0 ')
except:
    print('ห้ามค่าติดลบ')