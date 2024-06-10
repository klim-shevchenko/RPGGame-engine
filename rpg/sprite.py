import tkinter as tk
class Sprite:

    def __init__(self, image):
        '''
        Класс спрайта для работы с изображениями на Canvas

        :param image: адресс изображения который
        '''
        self.image = tk.PhotoImage(file=image)
        self.tag = None
        self.x = 0
        self.y = 0
        self.z = 0  # z-координата спрайта

    def set_tag(self, tag):
        '''
        Устанавливает тег спрайта

        :param tag: тег спрайта
        '''
        self.tag = tag

    def set_z(self, z):
        '''
        Устанавливает z-координату спрайта

        :param z: координата z
        '''
        self.z = z

    def get_tag(self):
        '''
        Возвращает тег спрайта

        '''
        return self.tag

    def set_coords(self, new_x, new_y):
        '''
        Обновляет координаты спрайта

        :param new_x: координата x
        :param new_y: координата y
        '''
        if self.tag:
            self.x = new_x
            self.y = new_y
    def update(self):
        '''
        Обновляет анимацию спрайта

        '''
        pass