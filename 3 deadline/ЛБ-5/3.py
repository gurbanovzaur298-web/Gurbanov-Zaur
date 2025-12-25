class Animal:
    def __init__(self, name):
        self.name = name   
    def make_sound(self):
        print("Животное издает звук")
class Dog(Animal): 
    def __init__(self, name):
        super().__init__(name)  
    def make_sound(self):  
        print("Гав!")
class Cat(Animal):  
    def __init__(self, name):
        super().__init__(name)    
    def make_sound(self):  
        print("Мяу!")
def animal_chorus(animals):
    for animal in animals:
        animal.make_sound()
print("\nЗадание 3: Животные и наследование")
animals = [Dog("Шарик"), Cat("Матроскин")]
print("Хор животных:")
animal_chorus(animals)
print("\nОтдельные животные:")
dog = Dog("Бобик")
cat = Cat("Мурка")
print(f"{dog.name}: ", end="")
dog.make_sound()
print(f"{cat.name}: ", end="")
cat.make_sound()