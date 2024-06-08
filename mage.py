from rpg.sprite import *
from rpg.actor import *
from rpg.game import new_actor
"""
class Mage(Actor):
    image_2_0_0 = Sprite('images/Mage_0_0.png')
    image_2_0_1 = Sprite('images/Mage_0_1.png')
    image_2_0_2 = Sprite('images/Mage_0_2.png')
    image_2_0_3 = Sprite('images/Mage_0_3.png')
    image_2_0_4 = Sprite('images/Mage_0_4.png')
    image_2_1_0 = Sprite('images/Mage_1_0.png')
    image_2_1_1 = Sprite('images/Mage_1_1.png')
    image_2_1_2 = Sprite('images/Mage_1_2.png')
    image_2_1_3 = Sprite('images/Mage_1_3.png')
    image_2_1_4 = Sprite('images/Mage_1_4.png')
    image_2_2_0 = Sprite('images/Mage_2_0.png')
    image_2_2_1 = Sprite('images/Mage_2_1.png')
    image_2_2_2 = Sprite('images/Mage_2_2.png')
    image_2_2_3 = Sprite('images/Mage_2_3.png')
    image_2_2_4 = Sprite('images/Mage_2_4.png')
    image_2_3_0 = Sprite('images/Mage_3_0.png')
    image_2_3_1 = Sprite('images/Mage_3_1.png')
    image_2_3_2 = Sprite('images/Mage_3_2.png')
    image_2_3_3 = Sprite('images/Mage_3_3.png')
    image_2_3_4 = Sprite('images/Mage_3_4.png')
    image_2_4_0 = Sprite('images/Mage_4_0.png')
    image_2_4_1 = Sprite('images/Mage_4_1.png')
    image_2_4_2 = Sprite('images/Mage_4_2.png')
    image_2_4_3 = Sprite('images/Mage_4_3.png')
    image_2_4_4 = Sprite('images/Mage_4_4.png')
    image_2_5_0 = Sprite('images/Mage_5_0.png')
    image_2_5_1 = Sprite('images/Mage_5_1.png')
    image_2_5_2 = Sprite('images/Mage_5_2.png')
    image_2_5_3 = Sprite('images/Mage_5_3.png')
    image_2_5_4 = Sprite('images/Mage_5_4.png')
    image_2_6_0 = Sprite('images/Mage_6_0.png')
    image_2_6_1 = Sprite('images/Mage_6_1.png')
    image_2_6_2 = Sprite('images/Mage_6_2.png')
    image_2_6_3 = Sprite('images/Mage_6_3.png')
    image_2_6_4 = Sprite('images/Mage_6_4.png')
    image_2_7_0 = Sprite('images/Mage_7_0.png')
    image_2_7_1 = Sprite('images/Mage_7_1.png')
    image_2_7_2 = Sprite('images/Mage_7_2.png')
    image_2_7_3 = Sprite('images/Mage_7_3.png')
    image_2_7_4 = Sprite('images/Mage_7_4.png')

    states_0 = {'down': image_2_0_0, 'down_right': image_2_1_0, 'right': image_2_2_0, 'up_right': image_2_3_0,
                'up': image_2_4_0, 'down_left': image_2_5_0, 'left': image_2_6_0, 'up_left': image_2_7_0}
    states_3 = {'down': [image_2_0_0, image_2_0_1, image_2_0_2, image_2_0_3, image_2_0_4],
                'down_right': [image_2_1_0, image_2_1_1, image_2_1_2, image_2_1_3, image_2_1_4],
                'right': [image_2_2_0, image_2_2_1, image_2_2_2, image_2_2_3, image_2_2_4],
                'up_right': [image_2_3_0, image_2_3_1, image_2_3_2, image_2_3_3, image_2_3_4],
                'up': [image_2_4_0, image_2_4_1, image_2_4_2, image_2_4_3, image_2_4_4],
                'down_left': [image_2_5_0, image_2_5_1, image_2_5_2, image_2_5_3, image_2_5_4],
                'left': [image_2_6_0, image_2_6_1, image_2_6_2, image_2_6_3, image_2_6_4],
                'up_left': [image_2_7_0, image_2_7_1, image_2_7_2, image_2_7_3, image_2_7_4]}"""
"""
    def __init__(self, x, y, z, **params):
        '''класс Mage для работы с персонажем Волшебником'''

        #self.sprite = self.image_2_0_0
        #self.states = self.states_0
        self.sprite = Sprite('images/Mage_0_0.png')
        self.states = {'down': Sprite('images/Mage_0_0.png'), 'down_right': Sprite('images/Mage_1_0.png'), 'right': Sprite('images/Mage_2_0.png'), 'up_right': Sprite('images/Mage_3_0.png'),
                'up': Sprite('images/Mage_4_0.png'), 'down_left': Sprite('images/Mage_5_0.png'), 'left': Sprite('images/Mage_6_0.png'), 'up_left': Sprite('images/Mage_7_0.png')}
        super().__init__(x, y, z, **params)
        self.name = 'Mage'
        self.category = 'pc'
        self.strange = 5
        self.wizdom = 10
"""

Mage = new_actor('Mage', category='pc', strange=5, wizdom=10, name='Mage',
                 states = {'down': Sprite('images/Mage_0_0.png'),
                           'down_right': Sprite('images/Mage_1_0.png'),
                           'right': Sprite('images/Mage_2_0.png'),
                           'up_right': Sprite('images/Mage_3_0.png'),
                           'up': Sprite('images/Mage_4_0.png'),
                            'down_left': Sprite('images/Mage_5_0.png'),
                            'left': Sprite('images/Mage_6_0.png'),
                            'up_left': Sprite('images/Mage_7_0.png')})
