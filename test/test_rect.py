import unittest
from rpg.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        # Прямоугольник для использования в тестах
        self.rect = Rectangle(1, 1, 4, 4)

    def test_inside(self):
        '''Тест: прямоугольник внутри другого'''
        rect_outside = Rectangle(0, 0, 6, 6)
        self.assertTrue(self.rect.is_in(rect_outside))

    def test_outside(self):
        '''Тест: прямоугольник снаружи другого'''
        rect_inside = Rectangle(2, 2, 2, 2)
        self.assertFalse(self.rect.is_in(rect_inside))

    def test_apartside(self):
        '''Тест: прямоугольник отдельно от другого'''
        rect_apart = Rectangle(6, 6, 2, 2)
        self.assertFalse(self.rect.is_in(rect_apart))

    def test_touching_left(self):
        '''Тест: прямоугольник касается слева'''
        touching_left = Rectangle(0, 2, 1, 1)
        self.assertFalse(self.rect.is_in(touching_left))

    def test_touching_right(self):
        '''Тест: прямоугольник касается справа'''
        touching_right = Rectangle(5, 2, 1, 1)
        self.assertFalse(self.rect.is_in(touching_right))

    def test_touching_top(self):
        '''Тест: прямоугольник касается сверху'''
        touching_top = Rectangle(2, 5, 1, 1)
        self.assertFalse(self.rect.is_in(touching_top))

    def test_touching_bottom(self):
        '''Тест: прямоугольник касается снизу'''
        touching_bottom = Rectangle(2, 0, 1, 1)
        self.assertFalse(self.rect.is_in(touching_bottom))

    def test_intersect_left(self):
        '''Тест: пересечение прямоугольника слева'''
        intersect_left = Rectangle(0, 2, 3, 2)
        self.assertTrue(self.rect.is_in(intersect_left))

    def test_intersect_right(self):
        '''Тест: пересечение прямоугольника справа'''
        intersect_right = Rectangle(3, 2, 3, 2)
        self.assertTrue(self.rect.is_in(intersect_right))

    def test_intersect_top(self):
        '''Тест: пересечение прямоугольника сверху'''
        intersect_top = Rectangle(2, 3, 2, 3)
        self.assertTrue(self.rect.is_in(intersect_top))

    def test_intersect_bottom(self):
        '''Тест: пересечение прямоугольника снизу'''
        intersect_bottom = Rectangle(2, 0, 2, 3)
        self.assertTrue(self.rect.is_in(intersect_bottom))

    def test_is_point_inside(self):
        # Создайте прямоугольник
        rect = Rectangle(0, 0, 10, 10)

        # Точка внутри прямоугольника
        self.assertTrue(rect.is_point_inside(5, 5))

        # Точка на границе прямоугольника
        self.assertTrue(rect.is_point_inside(0, 0))
        self.assertTrue(rect.is_point_inside(0, 10))
        self.assertTrue(rect.is_point_inside(10, 0))
        self.assertTrue(rect.is_point_inside(10, 10))

        # Точка вне прямоугольника
        self.assertFalse(rect.is_point_inside(-1, -1))
        self.assertFalse(rect.is_point_inside(11, 11))
        self.assertFalse(rect.is_point_inside(5, -5))
        self.assertFalse(rect.is_point_inside(-5, 5))

if __name__ == '__main__':
    unittest.main()