"""
Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
    📌 возврат строки без изменений
    📌 возврат строки с преобразованием регистра без потери символов
    📌 возврат строки с удалением знаков пунктуации
    📌 возврат строки с удалением букв других алфавитов
    📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""
import unittest
from string import ascii_letters

def delete_non_char(text: str) -> str:
    return "".join(char for char in text if char in ascii_letters or char == ' ').lower()

class TestDeleteNonChar(unittest.TestCase):
    def test_not_changed(self):
        self.assertEqual(delete_non_char('hello python'), 'hello python')
    def test_lower(self):
        self.assertEqual(delete_non_char('Hello Python'), 'hello python')
    def test_non_asccii(self):
        self.assertEqual(delete_non_char('hello, python!'), 'hello python')
    def test_non_english(self):
        self.assertEqual(delete_non_char('hello привет python'), 'hello  python')
    def test_all(self):
        self.assertEqual(delete_non_char('"HelloПривет1223;№ Python2"'), 'hello python')



if __name__ == '__main__':
    unittest.main(verbosity=True)
