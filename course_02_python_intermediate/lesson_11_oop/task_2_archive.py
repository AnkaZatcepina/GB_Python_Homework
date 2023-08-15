"""
    📌 Создайте класс Архив, который хранит пару свойств.
    Например, число и строку.
    📌 При нового экземпляра класса, старые данные из ранее
    созданных экземпляров сохраняются в пару списков-
    архивов
    📌 list-архивы также являются свойствами экземпляра
"""

class Archive:
    """
    Singleton класс Архив, который хранит пару число и строка
    Старые данные из ранее созданных экземпляров сохраняются в списках
    """
    _instance = None

    def __init__(self,numb:int,text:str):
        print('Init')
        self.numb = numb
        self.text = text

    def __new__(cls,*args,**kwargs):
        """
        При нового экземпляра класса, старые данные из ранее
        созданных экземпляров сохраняются в пару списков-
        архивов
        """
        print('New: ' + cls.__name__)
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.numbs_archive = []   
            cls._instance.texts_archive = []  
        else:    
            cls._instance.numbs_archive.append(cls._instance.numb)   
            cls._instance.texts_archive.append(cls._instance.text)   
        return cls._instance   

if __name__ == '__main__':
    archive_1 = Archive(1,'text_1') 
    archive_2 = Archive(2,'text_2') 
    archive_3 = Archive(3,'text_3') 
    print(archive_1._instance.numbs_archive)
    print(archive_2._instance.numbs_archive)
    
    print(archive_3._instance.texts_archive)
    print(f'{archive_1 == archive_3}')

    print(archive_1.__doc__)

