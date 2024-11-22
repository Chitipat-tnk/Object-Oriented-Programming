class Cat:
    def __init__(self,ชื่อ,อายุ,สี,ความหิว):
        self.name = ชื่อ
        self.age = อายุ
        self.color = สี
        self.hungry = ความหิว
    def eat(self,อาหาร):
        self.hungry+= อาหาร

cat1 = Cat(ชื่อ="ลูกออฟ",อายุ=19,สี="ดอ",ความหิว=5)
cat2 = Cat("ศรีออฟ",18,"เเดง",1)
print(cat1.name,cat1.age)
print(cat2.name,cat2.age)