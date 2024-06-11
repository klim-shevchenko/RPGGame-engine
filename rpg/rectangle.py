class Rectangle:
    def __init__(self, x, y, width, height):
        '''
        Класс прямоугольник

        :param x: координата x прямоугольника
        :param y: координата y прямоугольника
        :param width: ширина прямоугольника
        :param height: высота прямоугольника
        '''
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def is_in(self, rect):
        '''
        Проверяет, входит ли прямоугольник self в прямоугольник rect

        :param rect: прямоугольник
        '''
        return (self.x >= rect.x and
                self.y >= rect.y and
                self.x + self.width <= rect.x + rect.width and
                self.y + self.height <= rect.y + rect.height)

    def is_point_inside(self, target_x, target_y):
        '''
        Проверяет, входит ли точка (x, y) в данный прямоугольник

        :param target_x: точка x
        :param target_y: точка y
        return ((self.x <= target_x + self.width) or (self.x >= target_x - self.width)) and ((self.y <= target_y + self.height) or (self.y >= target_y - self.height))
        return ((self.x <= target_x <= self.width) or (self.x >= target_x >= self.width)) and ((self.y <= target_y <= self.height) or (self.y <= target_y <= self.height))

        '''
        return ((self.x >= target_x + self.width / 2) or (self.x <= target_x - self.width / 2)) or (
                    (self.y >= target_y + self.height / 2) or (self.y <= target_y - self.height / 2))