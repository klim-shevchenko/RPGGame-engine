from rpg.area import *
from rpg.sprite import *
from rpg.rectangle import *
from footman import *
from grunt import *

image_0 = Sprite('images/fon3.png')
f = Footman(0, 0, 0)
g = Grunt(0, 0, 0)
class Ruins(Area):
    def __init__(self):
        super().__init__()
        self.add_sprite(image_0, 140, 140, 0)
        self.add_rect(Rectangle(x=0, y=0, width=image_0.image.width(), height=image_0.image.height()))
        self.add_object(f, 120, 120, 1)
        self.add_object(g, 220, 185, 1)