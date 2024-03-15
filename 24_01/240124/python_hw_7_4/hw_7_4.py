# 사람의 이름과 나이를 입력받아 자신을 소개하는 Person 클래스를 작성하십시오.
# 클래스에는 자신을 소개하는 introduce 인스턴스 메서드가 포함되어야 하고, 
# 인스턴스가 생성될 때마다 증가하는 number_of_people 클래스 변수가 작성되어야한다.
class Person:
    number_of_people = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f'제 이름은 {self.name} 이고, 저는 {self.age} 살 입니다.')
        Person.number_of_people += 1




person1 = Person("Alice", 25)
person1.introduce()
print(Person.number_of_people)
