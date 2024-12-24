class Car :
    name = ""
    speed = 0

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def getName(self) : # 자동차의 이름을 반환
        return self.name
    
    def getSpeed(self) : # 자동차의 현재속도를 반환
        return self.speed
    
car1, car2 = None, None

car1 = Car("아우디", 0)
car2 = Car("벤츠", 30)

print("%s의 현재 속도 %d" % (car1.getName(), car1.getSpeed()))
print("%s의 현재 속도 %d" % (car2.getName(), car2.getSpeed()))