"""
    📌 Создайте три (или более) отдельных классов животных.
    Например рыбы, птицы и т.п.
    📌 У каждого класса должны быть как общие свойства,
    например имя, так и специфичные для класса.
    📌 Для каждого класса создайте метод, выводящий
    информацию специфичную для данного класса.
"""
class Fish:
    def __init__(self, name: str, color: str, size: float, max_depth: float):
        self.name = name
        self.color = color
        self.size = size
        self.max_depth = max_depth

    def get_max_depth(self)->float:  
        return self.max_depth 

class Bird:
    def __init__(self, name: str, color: str, size: float, habitat: str):
        self.name = name
        self.color = color
        self.size = size
        self.habitat = habitat     
    
    def get_habitat(self)->str:  
        return self.habitat   

class Cat:
    def __init__(self, name: str, color: str, size: float, hairy:bool):
        self.name = name
        self.color = color
        self.size = size
        self.hairy = hairy    
       
    def get_hairy(self)->bool():  
        return self.hairy  

if __name__ == '__main__':
    fish = Fish('Nemo', 'gold', 1, 15_000)
    bird = Bird('Chichi', 'white', 82.3, 'forest') 
    cat = Cat('Tom', 'black and white', 11, True)
    print(fish.get_max_depth())
    print(bird.get_habitat())
    print(cat.get_hairy())