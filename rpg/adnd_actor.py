import random
from math import sqrt
from rpg.actor import Actor
from rpg.animation import Animation
import rpg.game
import time

class Adnd_actor(Actor):

    ATTACK_RANGE = 50
    
    def __init__(self, x, y, z, **params):
        '''
        Класс Adnd_actor содержащий основные механики взаимодействия с другими персонажами

        :param x: координата x
        :param y: координата y
        :param z: координата z
        '''
        super().__init__(x, y, z, **params)
        #self.is_attack = False
        self.alive = True
        self.on_click = self.click

    def click(self):
        '''
        вызывается при клике на персонажа

        '''
        pc = rpg.game.Game.game.team_of_pc[0]
        if pc == self:
            return
        dx = pc.pos_x - self.pos_x
        dy = pc.pos_y - self.pos_y
        dist = sqrt(dx * dx + dy * dy)
        if dist <= self.ATTACK_RANGE:
            pc.is_attack = True
            pc.attack(self)
            #time.sleep(0.3)
            if self.hp <=0:
                pc.is_attack = False
        
    def attack(self, actor):
        '''
        совершает атаку по actor

        :param actor: персонаж, которого атакуют
        '''
        #dice = random.randint(1,20)
        #dice >= actor.armor:
        actor.hp -= self.damage
    def update(self):
        '''
        обновляет персонажа

        '''
        super().update()
        if self.hp <= 0:
            self.stop_move()
            self.set_state('death')
#            rpg.game.Game.game.current_area.remove_object(self)
