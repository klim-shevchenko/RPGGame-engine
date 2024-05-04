from rpg.graphics import *
from rpg.sprite import *
class area():
    def __init__(self, **params):
        self.area_zone = params # параметр определяющий особенности конкретной зоны
        self.list_of_objects = () # список, хранящий в себе множество экземпляров классов Item, Actor
        self.sprite = None
    def area_add_sprite(self, sprite, x, y, z):
        ''' метод отвечающий за вызов метода add\_sprite у класса Graphics '''
        self.sprite = sprite
        self.sprite.x = x
        self.sprite.y = y
        self.sprite.z = z
        #canvas.add_sprite(sprite, x, y, z)

    def add_object(self, obj):
        ''' метод отвечающий за добавление экземпляров классов Item, Actor, в поле area\_list\_objects экземпляра класса Area '''
        self.list_of_objects.append(obj)

    def check_obj_sprite(self):
        ''' метод отвечающий за проверку пересекаются ли координаты Sprite`ов различных объектов в экземпляре класса Area '''
        self

    def set_team(self, x, y):
        ''' метод отвечающий за установку команды игровых персонажей в конкретной зоне '''
        self