"""
Доработаем задачи 5-6. Создайте класс-фабрику.
    ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
    ○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""

from task_6_animals import Animal, Fish, Bird, Cat
from enum import Enum

class AnimalType(Enum):
    fish = 'Fish'
    bird = 'Bird'
    cat = 'Cat'

class Factory():
    def __init__(self, animal_type: AnimalType, *args):
         
        match animal_type:
            case AnimalType.fish:        
                self.animal = Fish(*args)
            case AnimalType.bird:
                self.animal = Bird(*args)
            case AnimalType.cat:
                self.animal = Cat(*args)
    def get_animal(self)->Animal:
        return self.animal      

if __name__ == '__main__':
    fish = Factory(AnimalType.fish, 'Nemo', 'gold', 1.0, 15_000.0).get_animal()
    bird = Factory(AnimalType.bird, 'Chichi', 'white', 82.3, 'forest').get_animal()
    cat = Factory(AnimalType.cat, 'Tom', 'black and white', 11, True).get_animal()
    animals = (fish,bird,cat)
    for animal in animals:
        print(animal.get_unique()) 
        print(type(animal))           
