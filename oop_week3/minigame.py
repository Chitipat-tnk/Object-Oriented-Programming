import random
print('โปรเเกรมเป่ายิงฉุบ')
while True:
    a = random.choice(["ค้อน","กรรไกร","กระดาษ"])
    print(f'{a}')
    print("ค้อน ","กรรไกร ","กระดาษ ")
    Value = str(input('คุณเลือก : '))
    if (a == Value ):
        print("ผลลัพท์คือ เสมอ")
        print("------------------ ")
    elif (Value =="ค้อน" and a=="กรรไกร" ):
        print("ผลลัพท์ คือ ชนะ")
        print("------------------ ")
    elif (Value =="กระดาษ" and a=="ค้อน"):
        print("ผลลัพท์ คือ ชนะ")
        print("------------------ ")
    elif (Value =="กรรไกร" and a=="กระดาษ"):
        print("ผลลัพท์ คือ ชนะ")
        print("------------------ ")
    else:
        print('ผลลัพท์ คือ เเพ้')
        print("------------------ ")
 