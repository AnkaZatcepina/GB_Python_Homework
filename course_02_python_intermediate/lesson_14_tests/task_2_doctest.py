"""
Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
    📌 возврат строки без изменений
    📌 возврат строки с преобразованием регистра без потери символов
    📌 возврат строки с удалением знаков пунктуации
    📌 возврат строки с удалением букв других алфавитов
    📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""

from string import ascii_letters

def delete_non_char(text: str) -> str:
    """
    Deletes non asccii letters and format to lower 

    >>> delete_non_char('hello python')
    'hello python'
    >>> delete_non_char('Hello Python')
    'hello python'
    >>> delete_non_char('hello, python!')
    'hello python'
    >>> delete_non_char('hello привет python')
    'hello  python'
    >>> delete_non_char('"HelloПривет1223;№ Python2"')
    'hello python'
    """
    return "".join(char for char in text if char in ascii_letters or char == ' ').lower()

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True) 