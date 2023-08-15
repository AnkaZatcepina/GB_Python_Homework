"""
Создайте класс Моя Строка, где:
    📌 будут доступны все возможности str
    📌 дополнительно хранятся имя автора строки и время создания (time.time)
"""
import time

class MyString(str):
    """
    String with author name and creation time
    """
    def __new__(cls,text:str,creator:str):
        instance = super().__new__(cls,text)
        instance.creator = creator
        instance.time = time.time()
        print('New')
        return instance

    def __str__(self):
        """
        Shows original string, author name and creation time
        """
        return f'"{super().__str__()}", created by: {self.creator} at {self.time}'  

    def __repr__(self):
        """
        Example
        """
        return f"MyString('{super().__str__()}','{self.creator}')"         

if __name__ == '__main__':
    example = MyString('Hello','Anka')
    print(example)  
    print(MyString.__doc__)
    print(MyString.__str__.__doc__)   
    print(repr(example))
#    print(help(MyString))