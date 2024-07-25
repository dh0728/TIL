# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0
    def __init__(self):
        Animal.num_of_animal += 1

class Dog:
    sound = '멍멍'
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return f'애완동물은 {Dog.sound} 소리를 냅니다.'

class Cat(Animal):
    sound = '야옹'
    
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return f'애완동물은 {Cat.sound} 소리를 냅니다.' 
    
class Pet(Dog , Cat):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return super().__str__()


    
animal1 = Pet()
print(animal1)
 
