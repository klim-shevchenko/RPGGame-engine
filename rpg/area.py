from rpg.graphics import *
from rpg.sprite import *
class Area():
    def __init__(self, **params):
        self.area_zone = params # параметр определяющий особенности конкретной зоны
        self.list_of_objects = [] # список, хранящий в себе множество экземпляров классов Item, Actor
        self.sprites = []
    def add_sprite(self, sprite, x, y, z):
        '''добавляет спрайт в зону
        param sprite - экземпляр спрайта, x y z - коодринаты'''
        sprite.x = x
        sprite.y = y
        sprite.z = z
        self.sprites.append(sprite)

    def add_object(self, obj):
        ''' добавляет объект в зону '''
        self.list_of_objects.append(obj)
        self.sprites.append(obj.sprite)
        self.add_sprite(obj.sprite, obj.pos_x, obj.pos_y, obj.pos_z)

    def check_obj_sprite(self):
        ''' проверяет координаты объекта '''
        self

    def set_team(self, x, y):
        ''' устанавливает комманду '''
        self