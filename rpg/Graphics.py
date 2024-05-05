import tkinter as tk
class Graphics(tk.Canvas):
    """Класс Canvas с дополнительными методами для работы со спрайтами."""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.sprites = []  # список спрайтов

    def add_sprite(self, sprite, x, y, z, **kwargs):
        """Добавляет спрайт на Canvas."""
        tag = self.create_image(x, y, image=sprite.image, anchor='center', **kwargs)
        sprite.set_tag(tag)
        sprite.set_z(z)  # устанавливаем z-координату спрайта
        sprite.x = x
        sprite.y = y
        self.sprites.append(sprite)
        self.sprites.sort(key=lambda sprite: sprite.z)  # сортировка спрайтов по z-координате
    def update(self):
        """Перерисовывает все спрайты."""
        for sprite in self.sprites:
            self.tag_raise(sprite.get_tag())  # перемещаем спрайт на передний план
            self.coords(sprite.get_tag(), sprite.x, sprite.y)
            self.itemconfig(sprite.get_tag(), image=sprite.image)
    def change_sprite(self, sprite, new_image):
        """Изменяет изображение спрайта."""
        self.itemconfig(sprite.get_tag(), image=new_image)
        sprite.image=new_image

    def delete_sprite(self, sprite):
        """Удаляет спрайт с Canvas."""
        self.delete(sprite.get_tag())
        self.sprites.remove(sprite)

    def clear_all(self):
        """Удаляет все спрайты с Canvas."""
        for sprite in self.sprites:
            self.delete(sprite.get_tag())
        self.sprites.clear()

    def update(self):
        """Перерисовывает все спрайты."""
        for sprite in self.sprites:
            self.tag_raise(sprite.get_tag())  # перемещаем спрайт на передний план
            self.coords(sprite.get_tag(), sprite.x, sprite.y)
            self.itemconfig(sprite.get_tag(), image=sprite.image)