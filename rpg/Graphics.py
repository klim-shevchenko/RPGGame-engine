import tkinter as tk
#from Sprite import Sprite
class Graphics(tk.Canvas):
    """Класс Canvas с дополнительными методами для работы со спрайтами."""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.sprites = []  # список спрайтов

    def add_sprite(self, sprite, x, y, **kwargs):
        """Добавляет спрайт на Canvas."""
        tag = self.create_image(x, y, image=sprite.image, anchor='center', **kwargs)
        sprite.set_tag(tag)
        self.sprites.append(sprite)
    # anchor='center'

    def change_sprite(self, sprite, new_image):
        """Изменяет изображение спрайта."""
        self.itemconfig(sprite.get_tag(), image=new_image)

    def delete_sprite(self, sprite):
        """Удаляет спрайт с Canvas."""
        self.delete(sprite.get_tag())
        self.sprites.remove(sprite)

    def clear_all(self):
        """Удаляет все спрайты с Canvas."""
        for sprite in self.sprites:
            self.delete(sprite.get_tag())
        self.sprites.clear()

    def update(self, sprite, new_x, new_y):
        """Обновляет координаты спрайта на Canvas."""
        sprite.update(new_x, new_y)
