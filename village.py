from rpg.area import *
from rpg.sprite import *
from rpg.rectangle import *

image_0 = Sprite('images/fon4.png')
class Village(Area):
    def __init__(self):
        super().__init__()
        self.add_sprite(image_0, 140, 140, 0)
        self.add_rect(Rectangle(x=0, y=0, width=image_0.image.width(), height=image_0.image.height()))