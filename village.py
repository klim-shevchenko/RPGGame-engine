from rpg.area import *
from rpg.sprite import *
from rpg.rectangle import *

class Village(Area):
    def __init__(self):
        '''
        Класс зоны Village

        '''
        super().__init__()
        self.add_sprite(Sprite('images/fon4.png'), 600, 470, 0)
        self.add_rect(Rectangle(x=0, y=0, width=Sprite('images/fon4.png').image.width(), height=Sprite('images/fon4.png').image.height()))