# 파이썬의 class를 연습하고자 한다.
# '자동차'의 특성을 가진 class를 요구 사항에 맞춰 정의하시오.

class Car:

    def __init__(self, engine, driving_system, sound):
        self.engine = engine
        self.driving_system = driving_system
        self.sound = sound

    def drive(self):
        print(self.sound)
        return self.engine
    
    def introduce(self):
        print(f'제 차의 엔진은 {self.engine} 방식이고, {self.driving_system} (으)로 동작합니다.')

    wheels = 4
    inc_wheels = 0
    @classmethod
    def increase_wheels(self):
        Car.wheels += 1
        Car.inc_wheels += 1
        print(f'법이 개정되어 모든 자동차의 필요 바퀴 수 가 {Car.inc_wheels}증가하였습니다.')


    @staticmethod
    def description():
        print(f'자동차(自動車, 영어:car,automoblie)는 엔진에서 만든 동력을 바퀴에 전달하여 지상에서 승객이나 화물을 운반하는 교통 수단이다.')



car1 = Car('gasoline', '후륜구동', '부릉부릉')
car2 = Car('diesel', '전륜구동', '달달달달')
car3 = Car('hybrid', '4wd', '슈웅')

car1.drive()
print(car2.drive())

print('===')
car1.introduce()
car3.introduce()

print('===')
print(f'이 세상의 자동차는 {Car.wheels}개의 바퀴를 가집니다.')
Car.increase_wheels()
print(f'이 세상의 자동차는 {Car.wheels}개의 바퀴를 가집니다.')
