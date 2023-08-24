"""
Возьмите 1-3 задачи из тех, что были на прошлых
семинарах или в домашних заданиях.
📌 Напишите к ним тесты.    
"""

from hw_task_1_circle_doctest import Circle
import unittest

class TestCircle(unittest.TestCase):

    def setUp(self) -> None:
        self.circle = Circle(3)

    def test_length(self):
        self.assertEqual(self.circle.get_length(), 18.84955592153876)

    def test_area(self):
        self.assertEqual(self.circle.get_area(), 28.274333882308138)

if __name__ == '__main__':
    unittest.main(verbosity=True)