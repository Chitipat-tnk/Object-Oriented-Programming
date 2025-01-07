class Student:
    def __init__(self,name,age):
        self.Name = name
        self.Age = age
        self.score = {}
        self.grades = {}
    def score1(self):
        self.score['thai'] = int(input('ใส่คะเเนนไทย : '))
        self.score['Math'] = int(input('ใส่คะเเนนคณิต : '))
        self.score['Eng'] = int(input('ใส่คะเเนนอังกฤษ : '))
        self.score['วิทย์'] = int(input('ใส่คะเเนนวิทย์ : '))
        self.score['สังคม'] = int(input('ใส่คะเเนนสังคม : '))
        return self.score   
    def grades1(self,score):
        if score >= 80:
            self.grades = 4
        elif score >=70:
            self.grades = 3
        elif self >=60:
            self.grades = 2
        elif score >=50:
            self.grades = 1
        else:
            self.grades = 0
        return self.grades


Student1 = Student('aa',1)

Student1.score1()
print(Student1.score)
print(Student1.grades1())