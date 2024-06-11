from rpg.sprite import *
from rpg.actor import *
from rpg.game import new_actor

Footman = new_actor('Footman', category='npc', hp=10, strange=5, wizdom=10, name='Footman',
                    states={'down': Animation(
                        ['images/Footman_0_0.png', 'images/Footman_0_1.png', 'images/Footman_0_2.png', 'images/Footman_0_3.png',
                         'images/Footman_0_4.png']),
                            'down_right': Animation(
                                ['images/Footman_1_0.png', 'images/Footman_1_1.png', 'images/Footman_1_2.png',
                                 'images/Footman_1_3.png', 'images/Footman_1_4.png']),
                            'right': Animation(['images/Footman_2_0.png', 'images/Footman_2_1.png', 'images/Footman_2_2.png',
                                                'images/Footman_2_3.png', 'images/Footman_2_4.png']),
                            'up_right': Animation(['images/Footman_3_0.png', 'images/Footman_3_1.png', 'images/Footman_3_2.png',
                                                   'images/Footman_3_3.png', 'images/Footman_3_4.png']),
                            'up': Animation(['images/Footman_4_0.png', 'images/Footman_4_1.png', 'images/Footman_4_2.png',
                                             'images/Footman_4_3.png', 'images/Footman_4_4.png']),
                            'down_left': Animation(['images/Footman_5_0.png', 'images/Footman_5_1.png', 'images/Footman_5_2.png',
                                                    'images/Footman_5_3.png', 'images/Footman_5_4.png']),
                            'left': Animation(['images/Footman_6_0.png', 'images/Footman_6_1.png', 'images/Footman_6_2.png',
                                               'images/Footman_6_3.png', 'images/Footman_6_4.png']),
                            'up_left': Animation(['images/Footman_7_0.png', 'images/Footman_7_1.png', 'images/Footman_7_2.png',
                                                  'images/Footman_7_3.png', 'images/Footman_7_4.png'],),
                            'death': Animation(['images/Footman_8_0.png', 'images/Footman_8_1.png', 'images/Footman_8_2.png',
                                            'images/Footman_8_3.png', 'images/Footman_8_4.png', 'images/Footman_8_5.png'])})
