class Animal:
    num_of_animal = 0

class Dog(Animal):
    sound = '멍멍'

class Cat(Animal):
    sound = '야옹'

class Pet(Cat, Dog):
    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'

pet = Pet()
print(pet)