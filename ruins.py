from rpg.area import *
from rpg.sprite import *
from rpg.rectangle import *
from footman import *
from grunt import *

class Ruins(Area):
    def __init__(self):
        super().__init__()
        self.add_sprite(Sprite('images/fon3.png'), 140, 140, 0)
        self.add_rect(Rectangle(x=0, y=0, width=Sprite('images/fon3.png').image.width(), height=Sprite('images/fon3.png').image.height()))
        self.add_object(Footman(0,0,0), 120, 120, 1)
        self.add_object(Grunt(0,0,0), 220, 185, 1)