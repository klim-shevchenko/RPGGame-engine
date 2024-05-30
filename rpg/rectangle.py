class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def is_in(self, rect):
        '''Проверяет, входит ли прямоугольник self в прямоугольник rect'''
        return (self.x >= rect.x and
                self.y >= rect.y and
                self.x + self.width <= rect.x + rect.width and
                self.y + self.height <= rect.y + rect.height)
    def is_point_inside(self, target_x, target_y):
        """Проверяет, входит ли точка (x, y) в данный прямоугольник."""
        return ((self.x >= target_x + self.width/2) or (self.x <= target_x - self.width/2)) or ((self.y >= target_y + self.height/2) or (self.y <= target_y - self.height/2))