from rpg.graphics import Graphics
from rpg.actor import Actor

class Area():
    def __init__(self, **params):
        '''
        Класс зоны

        '''
        self.area_zone = params # параметр определяющий особенности конкретной зоны
        self.objects = [] # список, хранящий в себе множество экземпляров классов Item
        self.sprites = [] # список фоновых спрайтов
        self.rectangles = None # список, хранящий в себе множетво прямоугольников

    def add_sprite(self, sprite, x, y, z):
        '''
        Добавляет спрайт в зону

        :param sprite: экземпляр спрайта
        :param x: коодрината x
        :param y: коодрината y
        :param z: коодрината z
        '''
        sprite.x = x
        sprite.y = y
        sprite.z = z
        self.sprites.append(sprite)

    def add_object(self, obj, x, y, z):
        '''
        Добавляет объект в зону

        :param obj: объект
        :param x: координата x
        :param y: координата y
        :param z: координата z
        '''
        obj.pos_x = x
        obj.pos_y = y
        obj.pos_z = z
        self.objects.append(obj)
        if obj.visible:
            Graphics.canvas.add_sprite(obj.sprite, x, y, z)

    def remove_object(self, obj):
        '''
        Удаляет объект из зоны

        :param obj объект
        '''
        if obj.visible:
            Graphics.canvas.delete_sprite(obj.sprite)
        self.objects.remove(obj)

    def load_sprites(self):
        '''
        Загружает все спрайты зоны

        '''
        for s in self.sprites:
            Graphics.canvas.add_sprite(s, s.x, s.y, s.z)
        for obj in self.objects:
            if obj.sprite is not None:
                Graphics.canvas.add_sprite(obj.sprite, obj.pos_x, obj.pos_y, obj.pos_z)

    def add_rect(self, rec):
        '''
        Добавляет прямоугольник в зону

        :param rec: прямоугольник
        '''
        self.rectangles = rec

    def entry_script(self):
        '''
        Запускается, когда команда входит в зону

        '''
        pass

    def exit_script(self):
        '''
        Запускается, когда команда выходит из зоны

        '''
        pass

    def update(self):
        '''
        Изменяет и проверяет изменение всех объектов в зоне

        '''
        for obj in self.objects:
            obj.update()
            if isinstance(obj, Actor):
                if not obj.rectangle.is_in(self.rectangles):
                    obj.stop_move()
                for o in self.objects:
                    if o != obj and obj.rectangle.is_in(o.rectangle):
                        o.actor_in(obj)