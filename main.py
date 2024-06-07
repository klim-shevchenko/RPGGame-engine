from rpg.graphics import *
from rpg.sprite import *
from rpg.game import *
from rpg.area import *
from rpg.actor import *
import time
import random
from rpg.rectangle import *
from bggame import *

#пробный скрипт
'''def walk(step_x, step_y):
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
    k2.search_position(new_x, new_y) # требуется закомментировать, если выбран вариант animate_sprite

    #Ждем 2 секунды перед выбором нового направления
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
    b.search_position(new_x, new_y) # требуется закомментировать, если выбран вариант animate_sprite

    # Ждем 2 секунды перед выбором нового направления
    time.sleep(2)'''

root = tk.Tk()
root.geometry('1500x1500')

exit_button = tk.Button(root, text="Exit", fg="red", command=root.destroy)
# Создание экземпляра класса graphics, который будет взаимодействовать с окном
canvas = Graphics(root, width=1500, height=1500)
Graphics.canvas = canvas  # Присваиваем canvas в статическое поле

# создание новой игры
BaldursGame(canvas, root)

# Создание экземпляра класса game
"""first_game = Game(canvas, root)
house = Area()
meadow = Area()

# создание спрайтов
image_0 = Sprite('images/fon3.png')
image_1 = Sprite('images/fon2.png')
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
image_3_0_0 = Sprite('images/Footman_0_0.png')
image_3_1_0 = Sprite('images/Footman_1_0.png')
image_3_2_0 = Sprite('images/Footman_2_0.png')
image_3_3_0 = Sprite('images/Footman_3_0.png')
image_3_4_0 = Sprite('images/Footman_4_0.png')
image_3_5_0 = Sprite('images/Footman_5_0.png')
image_3_6_0 = Sprite('images/Footman_6_0.png')
image_3_7_0 = Sprite('images/Footman_7_0.png')
image_4_0_0 = Sprite('images/Grunt_0_0.png')
image_4_1_0 = Sprite('images/Grunt_1_0.png')
image_4_2_0 = Sprite('images/Grunt_2_0.png')
image_4_3_0 = Sprite('images/Grunt_3_0.png')
image_4_4_0 = Sprite('images/Grunt_4_0.png')
image_4_5_0 = Sprite('images/Grunt_5_0.png')
image_4_6_0 = Sprite('images/Grunt_6_0.png')
image_4_7_0 = Sprite('images/Grunt_7_0.png')

# Загрузка изображения в зоны, добавление зон в игру
house.add_sprite(image_0, 140, 140, 0)
house.add_rect(Rectangle(x =0, y = 0, width=image_0.image.width(), height=image_0.image.height()))
#house.add_rect(Rectangle(x =0, y = 0, width=500, height=500))
meadow.add_sprite(image_1, 140, 140, 0)
meadow.add_rect(Rectangle(x =0, y = 0, width=500, height=500))
first_game.new_area('House', house)
states_0 = {'down': image_2_0_0, 'down_right': image_2_1_0, 'right': image_2_2_0, 'up_right': image_2_3_0, 'up': image_2_4_0, 'down_left': image_2_5_0, 'left': image_2_6_0, 'up_left': image_2_7_0}
states_1 = {'down': image_3_0_0, 'down_right': image_3_1_0, 'right': image_3_2_0, 'up_right': image_3_3_0, 'up': image_3_4_0, 'down_left': image_3_5_0, 'left': image_3_6_0, 'up_left': image_3_7_0}
states_2 = {'down': image_4_0_0, 'down_right': image_4_1_0, 'right': image_4_2_0, 'up_right': image_4_3_0, 'up': image_4_4_0, 'down_left': image_4_5_0, 'left': image_4_6_0, 'up_left': image_4_7_0}
states_3 = {'down': [image_2_0_0, image_2_0_1, image_2_0_2, image_2_0_3, image_2_0_4],'down_right': [image_2_1_0, image_2_1_1, image_2_1_2, image_2_1_3, image_2_1_4],
            'right': [image_2_2_0, image_2_2_1, image_2_2_2, image_2_2_3, image_2_2_4],'up_right': [image_2_3_0, image_2_3_1, image_2_3_2, image_2_3_3, image_2_3_4],
            'up': [image_2_4_0, image_2_4_1, image_2_4_2, image_2_4_3, image_2_4_4],'down_left': [image_2_5_0, image_2_5_1, image_2_5_2, image_2_5_3, image_2_5_4],
            'left': [image_2_6_0, image_2_6_1, image_2_6_2, image_2_6_3, image_2_6_4],'up_left': [image_2_7_0, image_2_7_1, image_2_7_2, image_2_7_3, image_2_7_4]}

Mage = first_game.new_actor('Mage', category='pc', strange=5, wizdom=10)
m = Mage(0, 0, 0, image_2_0_0, states_0) # требуется закомментировать, если выбран вариант animate_sprite
'''m = Mage(0, 0, 0, image_2_2_0, states_3, canvas)''' # требуется раскомментировать, если выбран вариант animate_sprite

#добавил нового персонажа
Knight1 = first_game.new_actor('Knight1', category='npc', strange=5, wizdom=10, sprite=image_3_0_0) # требуется закомментировать, если выбран вариант animate_sprite
k2 = Knight1(0, 0, 0, image_3_0_0, states_1) # требуется закомментировать, если выбран вариант animate_sprite
house.add_object(k2, 120, 120, 1) # требуется закомментировать, если выбран вариант animate_sprite

first_game.add_pc_to_team(m)
first_game.new_area('Meadow', meadow)
Bandit = first_game.new_actor("Bandit", category="NPC", strange=12, wizdom=8, sprite=image_4_0_0) # требуется закомментировать, если выбран вариант animate_sprite
b = Bandit(0, 0, 0, image_4_0_0, states_2) # требуется закомментировать, если выбран вариант animate_sprite
house.add_object(b, 220, 185, 1) # требуется закомментировать, если выбран вариант animate_sprite
meadow.add_object(b, 320, 185, 1)

#установка первой зоны и команды персонажей
first_game.set_area('House')
print(house.list_of_actors)
first_game.set_team(house,200, 120, 1)

# Функции, которые будут вызываться при нажатии кнопки

print(canvas.sprites)"""
"""def on_button_click4():
    first_game.set_area('House')
    first_game.set_team(house,120, 20, 1)
    print(house.list_of_actors)
    print(canvas.sprites)

def on_button_click5():
    first_game.set_area('Meadow')
    first_game.set_team(meadow,100, 260, 1)
    print(canvas.sprites)

def on_button_click6():
    first_game.start_script("walk", 'walk_script', 50, 50)

def on_button_click7():
    first_game.stop_script('walk_script')

def on_button_click8():
    first_game.start_script("walk_two", 'walk_two_script', 50, 50)

def on_button_click9():
    first_game.stop_script('walk_two_script')

# Создание кнопки
button4 = tk.Button(root, text="установить новую зону дом", command=on_button_click4)
button5 = tk.Button(root, text="установить новую зону луг", command=on_button_click5)
button6 = tk.Button(root, text="запустить скрипт", command=on_button_click6)
button7 = tk.Button(root, text="остановить скрипт", command=on_button_click7)
button8 = tk.Button(root, text="запустить скрипт_2", command=on_button_click8)
button9 = tk.Button(root, text="остановить скрипт_2", command=on_button_click9)

# Размещение кнопки на окне
exit_button.place(x = 1201,y = 60)
button4.place(x = 1201,y = 0)
button5.place(x = 1201,y = 30)
button6.place(x = 1201,y = 90)
button7.place(x = 1201,y = 120)
button8.place(x = 1201,y = 150)
button9.place(x = 1201,y = 180)"""

canvas.place(height = 700, width =700)
BaldursGame.timer
'''first_game.timer()''' # в конструкторе бг
# Основной цикл обработки событий
root.mainloop()
