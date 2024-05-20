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

    '''def update_coords(self, x1, y1, x2, y2):
        изменяет координаты прямоугольника
        self.canvas.coords(self.rect, x1, y1, x2, y2)

    def delete(self):
        удаляет прямоугольник
        self.canvas.delete(self.rect)'''