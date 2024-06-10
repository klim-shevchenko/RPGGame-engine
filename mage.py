from rpg.sprite import *
from rpg.adnd_actor import *
from rpg.game import new_actor

Mage = new_actor('Mage', category='pc', strange=5, wizdom=10, name='Mage',
                 states={'down': Animation(
                     ['images/Mage_0_0.png', 'images/Mage_0_1.png', 'images/Mage_0_2.png', 'images/Mage_0_3.png',
                      'images/Mage_0_4.png']),
                         'down_right': Animation(['images/Mage_1_0.png', 'images/Mage_1_1.png', 'images/Mage_1_2.png',
                                                  'images/Mage_1_3.png', 'images/Mage_1_4.png']),
                         'right': Animation(['images/Mage_2_0.png', 'images/Mage_2_1.png', 'images/Mage_2_2.png',
                                             'images/Mage_2_3.png', 'images/Mage_2_4.png']),
                         'up_right': Animation(['images/Mage_3_0.png', 'images/Mage_3_1.png', 'images/Mage_3_2.png',
                                                'images/Mage_3_3.png', 'images/Mage_3_4.png']),
                         'up': Animation(['images/Mage_4_0.png', 'images/Mage_4_1.png', 'images/Mage_4_2.png',
                                          'images/Mage_4_3.png', 'images/Mage_4_4.png']),
                         'down_left': Animation(['images/Mage_5_0.png', 'images/Mage_5_1.png', 'images/Mage_5_2.png',
                                                 'images/Mage_5_3.png', 'images/Mage_5_4.png']),
                         'left': Animation(['images/Mage_6_0.png', 'images/Mage_6_1.png', 'images/Mage_6_2.png',
                                            'images/Mage_6_3.png', 'images/Mage_6_4.png']),
                         'up_left': Animation(['images/Mage_7_0.png', 'images/Mage_7_1.png', 'images/Mage_7_2.png',
                                               'images/Mage_7_3.png', 'images/Mage_7_4.png']),
                         'death': Animation(['images/Mage_8_0.png', 'images/Mage_8_1.png', 'images/Mage_8_2.png',
                                             'images/Mage_8_3.png', 'images/Mage_8_4.png', 'images/Mage_8_5.png', 'images/Mage_8_6.png'])})
