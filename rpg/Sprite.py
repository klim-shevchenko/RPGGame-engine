import tkinter as tk
class Sprite:
    """Класс спрайта для работы с изображениями на Canvas."""
    def __init__(self, canvas, image):
        self.canvas = canvas
        self.image = tk.PhotoImage(file=image)
        self.tag = None

    def update(self, new_x, new_y):
        """Обновляет координаты спрайта на Canvas."""
        if self.tag:
            self.canvas.coords(self.tag, new_x, new_y)

    def get_tag(self):
        """Возвращает тег спрайта."""
        return self.tag

    def set_tag(self, tag):
        """Устанавливает тег спрайта."""
        self.tag = tag