from rpg.game import *
from rpg.graphics import *
from rpg.game import *
from rpg.graphics import *
from rpg.sprite import *
from ruins import *
from village import *
import time
import random

class BaldursGame(Game):
    def __init__(self, canvas, window, **params):
        '''
        Класс конкретной игры для демонстрации

        :param canvas: класс графической системы
        :param window: окно на которое будет выводится игра
        '''
        super().__init__(canvas, window, **params)
        from mage import Mage
        self.add_pc_to_team(Mage(0, 0, 0))
        self.new_area('Ruins', Ruins())
        self.new_area('Village', Village())
        self.set_area('Ruins')
        #self.set_area('Village')
        self.set_team(50, 400, 100)
        #self.set_team(550, 700, 100)
        self.timer()
