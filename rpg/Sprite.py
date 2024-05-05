import tkinter as tk
class Sprite:
    """Класс спрайта для работы с изображениями на Canvas."""
    def __init__(self, image):
        self.image = tk.PhotoImage(file=image)
        self.tag = None
        self.x = 0
        self.y = 0
        self.z = 0  # z-координата спрайта

    def set_tag(self, tag):
        """Устанавливает тег спрайта."""
        self.tag = tag

    def set_z(self, z):
        """Устанавливает z-координату спрайта."""
        self.z = z

    def get_tag(self):
        """Возвращает тег спрайта."""
        return self.tag
    def update(self, new_x, new_y):
        """Обновляет координаты спрайта."""
        if self.tag:
            self.x = new_x
            self.y = new_y