from rpg.game import *
from rpg.graphics import *
from rpg.sprite import *
from mage import *
from grunt import *
from footman import *
from ruins import *
from village import *
import time
import random

area_0 = Ruins()
area_1 = Village()
m = Mage(0, 0, 0)
class BaldursGame(Game):
    def __init__(self, canvas, window, **params):
        super().__init__(canvas, window, **params)
        self.new_area('Ruins', area_0)
        self.new_area('Village', area_1)
        self.set_team(area_0, 200, 120, 1)
        self.set_area('Ruin')
        self.timer()

    def walk(step_x, step_y):
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
        f.search_position(new_x, new_y)  # требуется закомментировать, если выбран вариант animate_sprite

        # Ждем 2 секунды перед выбором нового направления
        time.sleep(2)

    def walk_two(step_x, step_y):
        """Сценарий для движения рыцаря."""
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
        g.search_position(new_x, new_y)  # требуется закомментировать, если выбран вариант animate_sprite

        # Ждем 2 секунды перед выбором нового направления
        time.sleep(2)