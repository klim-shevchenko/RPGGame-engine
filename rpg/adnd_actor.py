import random
from math import sqrt
from rpg.actor import Actor
from rpg.animation import Animation
import rpg.game

class Adnd_actor(Actor):

    ATTACK_RANGE = 30
    
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
        '''
        вызывается при клике на персонажа

        '''
        pc = rpg.game.Game.game.team_of_pc[0]
        if pc == self:
            return
        dx = pc.pos_x - self.pos_x
        dy = pc.pos_y - self.pos_y
        if (-0.3 <= dx <= 0.3) and dy >= 0:
            pc.set_state('down_attack')
        elif (-0.3 <= dx <= 0.3) and dy < 0:
            pc.set_state('up_attack')
        elif dx >= 0 and (-0.3 <= dy <= 0.3):
            pc.set_state('right_attack')
        elif dx < 0 and (-0.3 <= dy <= 0.3):
            pc.set_state('left_attack')
        elif dx >= 0 and dy >= 0:
            pc.set_state('down_right_attack')
        elif dx >= 0 and dy < 0:
            pc.set_state('up_right_attack')
        elif dx < 0 and dy >= 0:
            pc.set_state('down_left_attack')
        elif dx < 0 and dy < 0:
            pc.set_state('up_left_attack')
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
    def update(self):
        '''
        обновляет персонажа

        '''
        super().update()
        if self.hp <= 0:
            self.stop_move()
            self.set_state('death')
#            rpg.game.Game.game.current_area.remove_object(self)