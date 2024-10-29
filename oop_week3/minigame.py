import random
print('โปรเเกรมเป่ายิงฉุบ')
while True:
    a = random.choice(["ค้อน","กรรไกร","กระดาษ"])
    print(f'{a}')
    print("ค้อน ","กรรไกร ","กระดาษ ")
    Value = str(input('คุณเลือก : '))
    if Value == a:
        print("ผลลัพท์คือ ชนะ")
        print("------------------ ")
    else:
        print('ผลลัพท์ คือ เเพ้')
        print("------------------ ")
 