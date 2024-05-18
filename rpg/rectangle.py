class MyRectangle:
    def __init__(self, canvas, x1, y1, x2, y2, color):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def update_coords(self, x1, y1, x2, y2):
        '''изменяет координаты прямоугольника'''
        self.canvas.coords(self.rect, x1, y1, x2, y2)

    def delete(self):
        '''удаляет прямоугольник '''
        self.canvas.delete(self.rect)