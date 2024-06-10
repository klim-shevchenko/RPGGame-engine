import tkinter as tk

class Graphics(tk.Canvas):
    canvas = None
    def __init__(self, master, **kwargs):
        '''
        Класс с методами для работы со спрайтами

        '''
        super().__init__(master, **kwargs)
        self.sprites = []  # список спрайтов
        Graphics.canvas = self

    def add_sprite(self, sprite, x, y, z, **kwargs):
       '''
       Добавляет спрайт на Canvas

       :param sprite: спрайт
       :param x: координата x
       :param y: координата y
       :param z: координата z
       :param kwargs: параметры относящиеся к конкретному изображению в tkinter
       '''
       tag = self.create_image(x, y, image=sprite.image, anchor='center', **kwargs)
       sprite.set_tag(tag)
       sprite.set_z(z)  # устанавливаем z-координату спрайта
       sprite.x = x
       sprite.y = y
       self.sprites.append(sprite)
       self.sprites.sort(key=lambda sprite: sprite.z)  # сортировка спрайтов по z-координате

    def update(self):
        '''
        Перерисовывает все спрайты

        '''
        for sprite in self.sprites:
            sprite.update()
            self.tag_raise(sprite.get_tag())  # перемещаем спрайт на передний план
            self.coords(sprite.get_tag(), sprite.x, sprite.y)
            self.itemconfig(sprite.get_tag(), image=sprite.image)


    def change_sprite(self, sprite, new_sprite):
        '''
        Меняет  спрайт на новый.

        :param sprite: экземпляр спрайта
        :param new_sprite: новый спрайт
        '''
        old_sprite_pos = None
        for i, s in enumerate(self.sprites):
            if s.get_tag() == sprite.get_tag():
                old_sprite_pos = i
                break

        if old_sprite_pos is not None:
            old_tag = sprite.get_tag()

            # Обновляем список спрайтов
            self.sprites[old_sprite_pos] = new_sprite
            new_sprite.set_tag(old_tag)

            # Обновляем тег нового спрайта
            new_sprite.set_tag(old_tag)
            new_sprite.set_z(sprite.z)

            # Перемещаем новый спрайт на передний план и обновляем его координаты
            self.tag_raise(old_tag)
            self.coords(old_tag, sprite.x, sprite.y)
            self.itemconfig(old_tag, image=new_sprite.image)

    def delete_sprite(self, sprite):
        '''
        Удаляет спрайт с Canvas.

        :param sprite: экземпляр спрайта
        :return:
        '''
        self.delete(sprite.get_tag())
        self.sprites.remove(sprite)

    def clear_all(self):
        '''
        Удаляет все спрайты с Canvas

        '''
        for sprite in self.sprites:
            self.delete(sprite.get_tag())
        self.sprites.clear()
