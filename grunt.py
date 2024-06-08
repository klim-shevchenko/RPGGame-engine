from rpg.sprite import *
from rpg.actor import *
from rpg.game import new_actor

"""
class Grunt(Actor):
    def __init__(self, x, y, z, **params):
        '''класс Grunt для работы с персонажем орком'''

        self.sprite = Sprite('images/Grunt_0_0.png')
        self.states = {'down': Sprite('images/Grunt_0_0.png'), 'down_right': Sprite('images/Grunt_1_0.png'), 'right': Sprite('images/Grunt_2_0.png'), 'up_right': Sprite('images/Grunt_3_0.png'),
                       'up': Sprite('images/Grunt_4_0.png'), 'down_left': Sprite('images/Grunt_5_0.png'), 'left': Sprite('images/Grunt_6_0.png'), 'up_left': Sprite('images/Grunt_7_0.png')}
        super().__init__(x, y, z, **params)
        self.name = 'Grunt'
        self.category = 'npc'
        self.strange = 17
        self.wizdom = 5
"""

Grunt = new_actor('Grunt', category='npc', strange=5, wizdom=10, name='Grunt',
                  states={'down': Animation(
                      ['images/Grunt_0_0.png', 'images/Grunt_0_1.png', 'images/Grunt_0_2.png', 'images/Grunt_0_3.png',
                       'images/Grunt_0_4.png']),
                          'down_right': Animation(['images/Grunt_1_0.png', 'images/Grunt_1_1.png', 'images/Grunt_1_2.png',
                                                   'images/Grunt_1_3.png', 'images/Grunt_1_4.png']),
                          'right': Animation(['images/Grunt_2_0.png', 'images/Grunt_2_1.png', 'images/Grunt_2_2.png',
                                              'images/Grunt_2_3.png', 'images/Grunt_2_4.png']),
                          'up_right': Animation(['images/Grunt_3_0.png', 'images/Grunt_3_1.png', 'images/Grunt_3_2.png',
                                                 'images/Grunt_3_3.png', 'images/Grunt_3_4.png']),
                          'up': Animation(['images/Grunt_4_0.png', 'images/Grunt_4_1.png', 'images/Grunt_4_2.png',
                                           'images/Grunt_4_3.png', 'images/Grunt_4_4.png']),
                          'down_left': Animation(['images/Grunt_5_0.png', 'images/Grunt_5_1.png', 'images/Grunt_5_2.png',
                                                  'images/Grunt_5_3.png', 'images/Grunt_5_4.png']),
                          'left': Animation(['images/Grunt_6_0.png', 'images/Grunt_6_1.png', 'images/Grunt_6_2.png',
                                             'images/Grunt_6_3.png', 'images/Grunt_6_4.png']),
                          'up_left': Animation(['images/Grunt_7_0.png', 'images/Grunt_7_1.png', 'images/Grunt_7_2.png',
                                                'images/Grunt_7_3.png', 'images/Grunt_7_4.png'])})