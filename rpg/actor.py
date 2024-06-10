from rpg.object import *
from rpg.sprite import *
from rpg.animation import Animation
from rpg.rectangle import *

class Actor(Object):
    def __init__(self, x, y, z, **params):
        '''класс Actor для работы с персонажем'''
        self.sprite = self.states[next(iter(self.states))]
        super().__init__(x, y, z, **params)
        self.speed_x = 0 #  значение скорости x
        self.speed_y = 0 #  значение скорости y
        self.target_x = 0
        self.target_y = 0
        self.rectangle = Rectangle(self.pos_x, self.pos_y, self.sprite.image.width(), self.sprite.image.height())

    def update(self):
        '''изменяет координаты персонажа'''
        if  self.rectangle.is_point_inside(self.target_x, self.target_y):
            self.pos_x += self.speed_x
            self.pos_y += self.speed_y
            self.sprite.running = True
            if (-0.3 <= self.speed_x <= 0.3) and self.speed_y >= 0:
                self.set_state('down')
            elif (-0.3 <= self.speed_x <= 0.3) and self.speed_y < 0:
                self.set_state('up')
            elif self.speed_x >= 0 and (-0.3 <= self.speed_y <= 0.3):
                self.set_state('right')
            elif self.speed_x < 0 and (-0.3 <= self.speed_y <= 0.3):
                self.set_state('left')
            elif self.speed_x >= 0 and self.speed_y >= 0:
                self.set_state('down_right')
            elif self.speed_x >= 0 and self.speed_y < 0:
                self.set_state('up_right')
            elif self.speed_x < 0 and self.speed_y >= 0:
                self.set_state('down_left')
            elif self.speed_x < 0 and self.speed_y < 0:
                self.set_state('up_left')
            self.rectangle.x = self.pos_x
            self.rectangle.y = self.pos_y
        else:
            self.speed_x = 0
            self.speed_y = 0
            self.target_x = self.pos_x
            self.target_y = self.pos_y
            self.sprite.running = False
        self.sprite.set_coords(self.pos_x, self.pos_y)

    def search_position(self, new_x, new_y):
        '''Изменяет направление движения у персонажа'''
        if self.pos_x != new_x or self.pos_y != new_y:
            self.target_x = new_x
            self.target_y = new_y
            vec_x = new_x - self.pos_x
            vec_y = new_y - self.pos_y
            maximum = max(abs(vec_x), abs(vec_y))
            normal_x = float(vec_x/maximum)
            normal_y = float(vec_y/maximum)
            self.speed_x = normal_x
            self.speed_y = normal_y
        else:
            self.speed_x = 0
            self.speed_y = 0

    def stop_move(self):
        '''останавливает движение персонажа'''
        self.pos_x -= self.speed_x
        self.pos_y -= self.speed_y
        self.target_x = self.pos_x
        self.target_y = self.pos_y
        self.rectangle.x = self.pos_x
        self.rectangle.y = self.pos_y
        self.speed_x = 0
        self.speed_y = 0

    def read_text(self, text):
        '''вывод содержимого поля act_text экземпляра класса Actor на экран'''
        self.canvas.draw_text(text, self.pos_x, self.pos_y)

    def open_inventory(self, inventory):
        '''вывод содержимого поля act_inventory экземпляра класса Actor на экран'''

    def open_list_spells(self, spells):
        '''вывод содержимого поля act_list_spells экземпляра класса Actor на экран'''

    def target_use_spell(self, spell, target):
        ''' вызов метода cast\_spell экземпляра класса Spell'''

    def target_use_item(self, item, target):
        ''' вызов метода use\_item экземпляра класса Item'''
