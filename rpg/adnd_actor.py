from rpg.actor import Actor
from rpg.animation import Animation
import random
class Adnd_actor(Actor):
    def __init__(self, x, y, z, **params):
        '''
        Класс Adnd_actor содержащий основные механики взаимодействия с другими персонажами

        :param x: координата x
        :param y: координата y
        :param z: координата z
        '''
        self.name = 'персонаж'
        self.category = 'npc'
        self.hp = 20
        self.damage = 1
        self.armor = 10
        self.alive = True
        super().__init__(x, y, z, **params)
        self.angry = False

    def attack(self, actor):
        '''
        совершает атаку по actor

        :param actor: персонаж, которого атакуют
        '''
        if actor.alive:
            dice = random.randint(1,20)
            self.angry = True
            if dice >= actor.armor:
                actor.hp -= self.damage
                print(self.name, 'попал по противнику', actor.name)
                if actor.hp <= 0:
                    self.alive = False
                    print(actor.name, 'погиб')
            else:
                print(self.name, 'промахнулся')

    def live(self):
        '''
        проверяет состояние персонажа

        '''
        if self.alive:
            self.update()
        else:
            self.set_state('death')