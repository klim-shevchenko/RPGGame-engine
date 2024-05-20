import unittest
from rpg.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect = Rectangle(0, 0, 2, 2)

    def test_inside(self):
        '''Проверяет, входит ли прямоугольник полностью в другой'''
        inside_rect = Rectangle(1, 1, 1, 1)
        self.assertTrue(inside_rect.is_in(self.rect))

    def test_overlap(self):
        '''Проверяет, пересекаются ли прямоугольники'''
        overlap_rect = Rectangle(1, 1, 2, 2)
        self.assertTrue(overlap_rect.is_in(self.rect))

    def test_touch(self):
        '''Проверяет, касаются ли прямоугольники'''
        touch_rect = Rectangle(2, 0, 1, 2)
        self.assertTrue(touch_rect.is_in(self.rect))

if __name__ == '__main__':
    unittest.main()
