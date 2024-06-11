import random
from math import sqrt

from rpg.actor import Actor
from rpg.animation import Animation
import rpg.game

class Adnd_actor(Actor):

    ATTACK_RANGE = 1230
    
    def __init__(self, x, y, z, **params):
        '''
        Класс Adnd_actor содержащий основные механики взаимодействия с другими персонажами

        :param x: координата x
        :param y: координата y
        :param z: координата z
        '''
        super().__init__(x, y, z, **params)
        self.angry = False
        self.alive = True
        self.on_click = self.click

    def click(self):
        pc = rpg.game.Game.game.team_of_pc[0]
        if pc == self:
            return
        dx = pc.pos_x - self.pos_x
        dy = pc.pos_y - self.pos_y
        dist = sqrt(dx * dx + dy * dy)
        if dist <= self.ATTACK_RANGE:
            pc.attack(self)
        
    def attack(self, actor):
        '''
        совершает атаку по actor

        :param actor: персонаж, которого атакуют
        '''
        #dice = random.randint(1,20)
        #dice >= actor.armor:
        actor.hp -= self.damage
#                print(self.name, 'попал по противнику', actor.name)
 #                   print(actor.name, 'погиб')
   #         else:
  #              print(self.name, 'промахнулся')

    def update(self):
        super().update()
        if self.hp <= 0:
            self.stop_move()
            self.set_state('death')
#            rpg.game.Game.game.current_area.remove_object(self)

    def live(self):
        '''
        проверяет состояние персонажа

        '''
        if self.alive:
            self.update()
        else:
            self.set_state('death')
