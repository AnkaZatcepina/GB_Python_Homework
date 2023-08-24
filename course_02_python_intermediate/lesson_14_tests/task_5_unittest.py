"""
    📌 На семинарах по ООП был создан класс прямоугольник
    хранящий длину и ширину, а также вычисляющую периметр,
    площадь и позволяющий складывать и вычитать
    прямоугольники беря за основу периметр.
    📌 Напишите 3-7 тестов unittest для данного класса.
"""
import sys
import pathlib
if __package__ is None:                  
    DIR = pathlib.Path(__file__).resolve().parent
    sys.path.insert(0, str(DIR.parent))
    __package__ = DIR.name

from lesson_11_oop.task_6_rectangle import RectanglePro
import unittest

class TestDeleteNonChar(unittest.TestCase):

    def setUp(self) -> None:
        self.r1 = RectanglePro(3,2)
        self.r2 = RectanglePro(7)
        self.r3 = RectanglePro(1,9)
        self.r4 = RectanglePro(1,1)

    def test_create_rectangle(self):
        self.assertEqual(self.r1, RectanglePro(3,2)) 

    def test_perimeter(self):
        self.assertEqual(self.r2.get_perimeter(), 28)

    def test_area(self):
        self.assertEqual(self.r3.get_area(), 9)    

    def test_not_eq(self):
        self.assertNotEqual(self.r1, self.r4)  

    def test_gt(self):
        self.assertGreater(self.r1, self.r4)

    def test_sum(self):
        self.assertEqual(self.r2 + self.r3, RectanglePro(8,16))

    def test_sub(self):
        self.assertEqual(self.r1 - self.r4, RectanglePro(2,1))   

if __name__ == '__main__':
    unittest.main(verbosity=True)        