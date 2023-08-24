"""
Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
    📌 возврат строки без изменений
    📌 возврат строки с преобразованием регистра без потери символов
    📌 возврат строки с удалением знаков пунктуации
    📌 возврат строки с удалением букв других алфавитов
    📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""
import pytest
from task_1_delete_non_char import delete_non_char

def test_not_changed():
    assert delete_non_char('hello python') == 'hello python', 'что-то пошло не так'

def test_lower():
    assert delete_non_char('Hello Python') == 'hello python'

def test_non_asccii():
    assert delete_non_char('hello, python!') == 'hello python'

def test_non_english():
    assert delete_non_char('hello привет python') == 'hello  python'
    
def test_all():
    assert delete_non_char('"HelloПривет1223;№ Python2"') == 'hello python'

if __name__ == '__main__':
    pytest.main(['-vv'])    
