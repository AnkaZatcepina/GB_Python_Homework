"""
    📌 Создайте функцию, которая удаляет из текста все символы
    кроме букв латинского алфавита и пробелов.
    📌 Возвращается строка в нижнем регистре.
"""
from string import ascii_letters

def delete_non_char(text: str) -> str:
    return "".join(char for char in text if char in ascii_letters or char == ' ').lower()

if __name__ == '__main__':
    s = '"HelloПривет1223;№ Python2 "'
    print(delete_non_char(s))    