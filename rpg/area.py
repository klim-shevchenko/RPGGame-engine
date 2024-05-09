class Area():
    def __init__(self, **params):
        self.area_zone = params # параметр определяющий особенности конкретной зоны
        self.list_of_objects = [] # список, хранящий в себе множество экземпляров классов Item, Actor
        self.sprites = [] # список, хранящий в себе множество экземпляров класов Sprite
    def add_sprite(self, sprite, x, y, z):
        '''добавляет спрайт в зону
        param sprite - экземпляр спрайта, x y z - коодринаты'''
        sprite.x = x
        sprite.y = y
        sprite.z = z
        self.sprites.append(sprite)

    def add_object(self, obj, x, y, z):
        ''' добавляет объект в зону
        param obj - объект, x y z - коодринаты'''
        obj.pos_x = x
        obj.pos_x = y
        obj.pos_x = z
        self.list_of_objects.append(obj)
        self.add_sprite(obj.sprite, x, y, z)

    def check_obj_sprite(self):
        ''' проверяет координаты объекта '''
        self

    def set_team(self, x, y):
        ''' устанавливает комманду. '''
        self