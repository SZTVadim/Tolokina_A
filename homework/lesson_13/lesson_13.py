from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):  #
        print(f"{self.name} говорит: Гав-гав!")


class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Мяу!")


class Zoo:
    def __init__(self, name):
        self.name = name
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)

    def get_animals_count(self):
        return len(self.__animals)


def animal_sound(animal):  # вызываем один и тот же метод make_sound() но по разному
    animal.make_sound()


dog1 = Dog("Бобик", 3)
dog2 = Dog("Шарик", 5)
cat1 = Cat("Мурка", 2)

zoo = Zoo("Городской зоопарк")

zoo.add_animal(dog1)
zoo.add_animal(dog2)
zoo.add_animal(cat1)

print(f"Животных в зоопарке: {zoo.get_animals_count()}")  # 3

for animal in zoo._Zoo__animals:
    animal_sound(animal)

# animal = Animal()
# TypeError: Can't instantiate abstract class Animal without an implementation for abstract method 'make_sound'
# Создавать можно только наследников с методом make_sound()
