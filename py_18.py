class Car :
    color = ""
    speed = 0

    def __init__(self): # 생성자
        self.color = "빨강"
        self.speed = 0

    def upSpeed(self, value) :
        self.speed += value

    def downSpeed(self, value) :
        self.speed -= value

myCar1 = Car() # 자동으로 값을 초기화
myCar2 = Car()

print("자동차1의 색상 %s, 현재 속도 %d" % (myCar1.color, myCar1.speed))
print("자동차2의 색상 %s, 현재 속도 %d" % (myCar2.color, myCar2.speed))