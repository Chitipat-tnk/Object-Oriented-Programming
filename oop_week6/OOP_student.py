import random
class student:
    def __init__(self,ชื่อ_นามสกุล,ชื่อเล่น):
        self.name = ชื่อ_นามสกุล
        self.Nickname = ชื่อเล่น
        self.Value = random.randint(1,10)
        self.Value1 = random.randint(1,10)

    def score(self):
        if self.Value >=5:
            print(f'ชื่อ-นามสกุล = ({self.name})  ชื่อเล่น = ({self.Nickname}) คะเเนน = {self.Value} สอบผ่าน')
        else :
            print(f'ชื่อ-นามสกุล = ({self.name})  ชื่อเล่น = ({self.Nickname}) คะเเนน = {self.Value} ไม่ผ่าน')
            if self.Value1 < 5:
                print(f'สอบเเก้  {self.Value1}  ไม่ผ่าน')
            else:
                print(f'{self.Value1} = ผ่านเเล้ว')

student1 = student("เตชินท์ ศรีพุฒ","สไปร์ท")
student2 = student("เสาวลักษณ์ ปานแก้ว","เเตงกวา")
student3 = student("กมลศักดิ์ จิรังพันธ์","ลูกออฟ")
student4 = student("ปิติพงค์ ภูมิพงศ์","ปอน")
student5 = student("หนึ่งตะวัน แสนสูงเนิน","กล้า")

student1.score()
student2.score()
student3.score()
student4.score()
student5.score()