import random
from math import sqrt
import time
from rpg.area import *
from rpg.sprite import *
from rpg.rectangle import *
from rpg.game import Game
from rpg.portal import Portal

class Ruins(Area):
    def __init__(self):
        '''
        Класс игровой зоны Ruins

        '''
        super().__init__()
        self.add_sprite(Sprite('images/fon3.png'), 590, 400, 0)
        self.add_rect(Rectangle(x=0, y=0, width=Sprite('images/fon3.png').image.width(), height=Sprite('images/fon3.png').image.height()))
        from grunt import Grunt
        self.grunt = Grunt(0,0,0)
        from footman import Footman
        self.footman = Footman(0,0,0)
        self.add_object(self.footman, 120, 120, 1)
        self.add_object(self.grunt, 220, 185, 1)
        p = Portal(400, 400, 200, 200, 'Village', 480, 100)
        self.add_object(p, p.pos_x, p.pos_y, 100)
        #Game.game.start_script(self.walk, "grunt", 50, 50)
        Game.game.start_script(self.ai, "ai", self.grunt)
        Game.game.start_script(self.walk_two, "footman", 50, 50)


    def walk(self, step_x, step_y):
        '''
        Сценарий для движения бугая

        :param step_x: шаг движения x
        :param step_y: шаг движения y
        '''
        if self.grunt.hp <= 0:
            Game.game.stop_script("grunt")
        new_x = 200
        new_y = 200

        # Выбираем случайное направление
        direction = random.choice(["up", "down", "left", "right"])

        # Устанавливаем целевую точку в зависимости от направления
        if direction == "up":
            new_y -= step_y
            new_x = step_x
        elif direction == "down":
            new_y += step_y
            new_x = step_x
        elif direction == "left":
            new_y = step_y
            new_x -= step_x
        elif direction == "right":
            new_y = step_y
            new_x += step_x

        # Обновляем координаты бугая
        self.grunt.search_position(new_x, new_y)  # требуется закомментировать, если выбран вариант animate_sprite

        # Ждем 2 секунды перед выбором нового направления
        time.sleep(2)

    def walk_two(self, step_x, step_y):
        '''
        Сценарий для движения hswfhz

        :param step_x: шаг движения x
        :param step_y: шаг движения y
        '''
        new_x = 100
        new_y = 100

        # Выбираем случайное направление
        direction = random.choice(["up", "down", "left", "right"])

        # Устанавливаем целевую точку в зависимости от направления
        if direction == "up":
            new_y -= step_y
            new_x = step_x
        elif direction == "down":
            new_y += step_y
            new_x = step_x
        elif direction == "left":
            new_y = step_y
            new_x -= step_x
        elif direction == "right":
            new_y = step_y
            new_x += step_x

        # Обновляем координаты рыцаря
        self.footman.search_position(new_x, new_y)  # требуется закомментировать, если выбран вариант animate_sprite

        # Ждем 2 секунды перед выбором нового направления
        time.sleep(2)

    def ai(self, actor):
        '''
        скрипт противников

        :param step_x: размер шага x до персонажа игрока
        :param step_y: размер шага x до персонажа игрока
        :param actor: персонаж противник
        '''
        if actor.hp <= 0:
            Game.game.stop_script("ai")
        import rpg.game
        pc = rpg.game.Game.game.team_of_pc[0]
        new_x = pc.pos_x
        new_y = pc.pos_y

        # Обновляем координаты рыцаря
        actor.search_position(new_x, new_y)  # требуется закомментировать, если выбран вариант animate_sprite
        dx = pc.pos_x - actor.pos_x
        dy = pc.pos_y - actor.pos_y
        dist = sqrt(dx * dx + dy * dy)
        if dist <= actor.ATTACK_RANGE:
            actor.attack(pc)
            if pc.hp <=0:
                Game.game.stop_script("ai")
        # Ждем 2 секунды перед выбором нового направления
        time.sleep(2)