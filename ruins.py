import random
import time
from rpg.area import *
from rpg.sprite import *
from rpg.rectangle import *
from rpg.game import Game
from footman import *
from grunt import *

class Ruins(Area):
    def __init__(self):
        super().__init__()
        self.add_sprite(Sprite('images/fon3.png'), 140, 140, 0)
        self.add_rect(Rectangle(x=0, y=0, width=Sprite('images/fon3.png').image.width(), height=Sprite('images/fon3.png').image.height()))
        self.grunt = Grunt(0,0,0)
        self.add_object(Footman(0,0,0), 120, 120, 1)
        self.add_object(self.grunt, 220, 185, 1)
        Game.game.start_script(self.walk, "grunt", 50, 50)

    def walk(self, step_x, step_y):
        """Сценарий для движения рыцаря."""
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

        # Обновляем координаты рыцаря
        self.grunt.search_position(new_x, new_y)  # требуется закомментировать, если выбран вариант animate_sprite

        # Ждем 2 секунды перед выбором нового направления
        time.sleep(2)
