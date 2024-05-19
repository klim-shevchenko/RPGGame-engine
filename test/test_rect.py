import unittest
from rpg.rectangle import MyRectangle

class MyTestCase(unittest.TestCase):
    def test_is_in(self):
        #прямоугольники для тестирования
        rect1 = MyRectangle(0, 0, 4, 4)
        rect2 = MyRectangle(1, 1, 2, 2)
        rect3 = MyRectangle(5, 5, 2, 2)

        # Проверка, что rect2 находится внутри rect1
        self.assertTrue(rect2.is_in(rect1))

        # Проверка, что rect3 не находится внутри rect1
        self.assertFalse(rect3.is_in(rect1))


if __name__ == '__main__':
    unittest.main()
