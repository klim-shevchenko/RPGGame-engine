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
        self.sprites.append(sprite)
        self.sprites.sort(key=lambda sprite: sprite.z)  # сортировка спрайтов по z-координате
    # anchor='center'

    def change_sprite(self, sprite, new_image):
        """Изменяет изображение спрайта."""
        #self.sprites.remove(sprite)
        self.itemconfig(sprite.get_tag(), image=new_image)
        sprite.image=new_image
        #self.sprites.append(sprite)

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
            self.coords(sprite.get_tag(), sprite.tag.x, sprite.tag.y)
            #sprite.update(self, x,y)
            self.itemconfig(sprite.get_tag(), image=sprite.image)