from rpg.graphics import *
from rpg.sprite import *
from rpg.game import *
from rpg.area import *
from rpg.actor import *
import time
import random
from rpg.rectangle import *

#пробный скрипт
def walk(step_x, step_y):
    """Сценарий для движения рыцаря."""
    new_x = 0
    new_y = 0

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
    k2.search_position(new_x, new_y)

    # Ждем 2 секунды перед выбором нового направления
    time.sleep(2)

def walk_two(step_x, step_y):
    """Сценарий для движения рыцаря."""
    new_x = 0
    new_y = 0

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
    #b.search_position(new_x, new_y)

    # Ждем 2 секунды перед выбором нового направления
    time.sleep(2)

root = tk.Tk()
root.geometry('1500x1500')

exit_button = tk.Button(root, text="Exit", fg="red", command=root.destroy)
# Создание экземпляра класса graphics, который будет взаимодействовать с окном
canvas = Graphics(root, width=1500, height=1500)
Graphics.canvas = canvas  # Присваиваем canvas в статическое поле

# Создание экземпляра класса game
first_game = Game(canvas, root)
house = Area()
meadow = Area()

# создание спрайтов
image_0 = Sprite('images/fon3.png')
image_1 = Sprite('images/fon2.png')
image_2_0 = Sprite('images/mage_0.png')
image_2_1 = Sprite('images/mage_1.png')
image_2_2 = Sprite('images/mage_2.png')
image_2_3 = Sprite('images/mage_3.png')
image_2_4 = Sprite('images/mage_4.png')
image_2_5 = Sprite('images/mage_5.png')
image_2_6 = Sprite('images/mage_6.png')
image_2_7 = Sprite('images/mage_7.png')
image_3_0 = Sprite('images/Footman_0.png')
image_3_1 = Sprite('images/Footman_1.png')
image_3_2 = Sprite('images/Footman_2.png')
image_3_3 = Sprite('images/Footman_3.png')
image_3_4 = Sprite('images/Footman_4.png')
image_3_5 = Sprite('images/Footman_5.png')
image_3_6 = Sprite('images/Footman_6.png')
image_3_7 = Sprite('images/Footman_7.png')

# Загрузка изображения в зоны, добавление зон в игру
house.add_sprite(image_0, 140, 140, 0)
house.add_rect(Rectangle(x =0, y = 0, width=image_0.image.width(), height=image_0.image.height()))
#house.add_rect(Rectangle(x =0, y = 0, width=500, height=500))
meadow.add_sprite(image_1, 140, 140, 0)
meadow.add_rect(Rectangle(x =0, y = 0, width=500, height=500))
first_game.new_area('House', house)
states_0 = {'down': image_2_0, 'down_right': image_2_1, 'right': image_2_2, 'up_right': image_2_3, 'up': image_2_4, 'down_left': image_2_5, 'left': image_2_6, 'up_left': image_2_7}
states_1 = {'down': image_3_0, 'down_right': image_3_1, 'right': image_3_2, 'up_right': image_3_3, 'up': image_3_4, 'down_left': image_3_5, 'left': image_3_6, 'up_left': image_3_7}

Knight = first_game.new_actor('Knight', category='pc', strange=5, wizdom=10)
k = Knight(0, 0, 0, image_2_1, states_0, canvas)

#добавил нового персонажа
Knight1 = first_game.new_actor('Knight1', category='npc', strange=5, wizdom=10, sprite=image_3_0)
k2 = Knight1(0, 0, 0, image_3_0, states_1, canvas)
house.add_object(k2, 120, 120, 1)

first_game.add_pc_to_team(k)
first_game.new_area('Meadow', meadow)
Bandit = first_game.new_actor("Bandit", category="NPC", strange=12, wizdom=8, sprite=image_3_0)
#b = Bandit(0, 0, 0, image_3, {'idle': Sprite('images/npc_dr_knight_0 #176474.png'), 'move': Sprite('images/enemy_skeleton_dog_0 #333165.png')})
#house.add_object(b, 220, 185, 1)
#meadow.add_object(b, 320, 185, 1)
canvas.update()
print(meadow.list_of_actors)

# Функции, которые будут вызываться при нажатии кнопки
first_game.set_area('House')
print(house.list_of_actors)
first_game.set_team(house,200, 120, 1)
print(canvas.sprites)
def on_button_click4():
    first_game.set_area('House')
    first_game.set_team(house,120, 20, 1)
    print(house.list_of_actors)
    print(canvas.sprites)

def on_button_click5():
    first_game.set_area('Meadow')
    first_game.set_team(meadow,100, 260, 1)

def on_button_click6():
    first_game.start_script(walk, 'walk_script', 50, 50)

def on_button_click7():
    first_game.stop_script('walk_script')

def on_button_click8():
    first_game.start_script(walk_two, 'walk_two_script', 50, 50)

def on_button_click9():
    first_game.stop_script('walk_two_script')


# Функция для смены спрайта персонажа
def change_sprite(actor, new_sprite):
    actor.sprite = new_sprite

# Создание кнопки для смены спрайта
button_change_sprite = tk.Button(root, text="Сменить спрайт рыцаря", command=lambda: change_sprite(k, image_2_1))

# Размещение новой кнопки на окне
button_change_sprite.place(x = 1201, y = 210)


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
button9.place(x = 1201,y = 180)

canvas.place(height = 700, width =700)

first_game.timer()
# Основной цикл обработки событий
root.mainloop()
