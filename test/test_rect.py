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
        intersect_left = Rectangle(0, 2, 1, 1)
        self.assertTrue(self.rect.is_in(intersect_left))

    def test_intersect_right(self):
        '''Тест: пересечение прямоугольника справа'''
        intersect_right = Rectangle(5, 2, 1, 1)
        self.assertTrue(self.rect.is_in(intersect_right))

    def test_intersect_top(self):
        '''Тест: пересечение прямоугольника сверху'''
        intersect_top = Rectangle(2, 5, 1, 1)
        self.assertTrue(self.rect.is_in(intersect_top))

    def test_intersect_bottom(self):
        '''Тест: пересечение прямоугольника снизу'''
        intersect_bottom = Rectangle(2, 0, 1, 1)
        self.assertTrue(self.rect.is_in(intersect_bottom))

if __name__ == '__main__':
    unittest.main()