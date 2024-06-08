from rpg.game import *
from rpg.graphics import *
from rpg.game import *
from rpg.graphics import *
from rpg.sprite import *
#from grunt import *
#from footman import *
from ruins import *
from village import *
import time
import random

class BaldursGame(Game):
    def __init__(self, canvas, window, **params):
        super().__init__(canvas, window, **params)
        self.new_area('Ruins', Ruins())
        self.new_area('Village', Village())
        from mage import Mage
        self.add_pc_to_team(Mage(0, 0, 0))
        self.set_area('Ruins')
        print(self.current_area)
        self.set_team('Ruins', 200, 120, 1)
        print(self.current_area.list_of_actors)
        self.timer()