from rpg.area import *
from rpg.sprite import *
from rpg.rectangle import *
from rpg.portal import Portal

class Village(Area):
    def __init__(self):
        '''
        Класс зоны Village

        '''
        super().__init__()
        self.add_sprite(Sprite('images/fon4.png'), 600, 470, 0)
        self.add_rect(Rectangle(x=0, y=0, width=Sprite('images/fon4.png').image.width(), height=Sprite('images/fon4.png').image.height()))
        p = Portal(480, 100, 200, 200, 'Ruins', 500, 300)
        self.add_object(p, p.pos_x, p.pos_y, 100)