from rpg.graphics import *
from rpg.sprite import *
from rpg.game import *
from rpg.area import *
from rpg.actor import *
import time
import random
from rpg.rectangle import *

#пробный скрипт
def walk(self):
    """Сценарий для движения рыцаря."""
    new_x = 0
    new_y = 0
    while True:
        # Выбираем случайное направление
        direction = random.choice(["up", "down", "left", "right"])

        # Устанавливаем целевую точку в зависимости от направления
        if direction == "up":
            '''k2.target_y -= 100
            k2.target_x -= 0'''
            new_y -= 100
            new_x = 0
        elif direction == "down":
            '''k2.target_y += 100
            k2.target_x -= 0'''
            new_y += 100
            new_x = 0
        elif direction == "left":
            '''k2.target_x -= 100
            k2.target_y -= 0'''
            new_y = 0
            new_x -= 100
        elif direction == "right":
            '''k2.target_x += 100
            k2.target_y -= 0'''
            new_y = 0
            new_x += 100

        # Обновляем координаты рыцаря
        k2.search_position(new_x, new_y)

        # Ждем 2 секунды перед выбором нового направления
        time.sleep(2)

root = tk.Tk()
root.geometry('1500x1500')

exit_button = tk.Button(root, text="Exit", fg="red", command=root.destroy)

# Создание экземпляра класса graphics, который будет взаимодействовать с окном
canvas = Graphics(root, width=1500, height=1500)

# Создание экземпляра класса game
first_game = Game(canvas, root)
house = Area()
meadow = Area()

# Загрузка изображения в зоны, добавление зон в игру

house.add_sprite(Sprite('images/fon1.png'), 140, 140, 0)
house.add_rect(Rectangle(x =0, y = 0, width=Sprite('images/fon1.png').image.width(), height=Sprite('images/fon1.png').image.height()))
#house.add_rect(Rectangle(x =0, y = 0, width=500, height=500))
meadow.add_sprite(Sprite('images/fon2.png'), 140, 140, 0)
meadow.add_rect(Rectangle(x =0, y = 0, width=500, height=500))
first_game.new_area('House', house)
Knight = first_game.new_actor('Knight', category='pc', strange=5, wizdom=10, sprite=Sprite('images/mage_0_0.png'))
k = Knight()

#добавил нового персонажа
Knight1 = first_game.new_actor('Knight1', category='npc', strange=5, wizdom=10, sprite=Sprite('images/npc_dr_knight_0 #176474.png'))
k2 = Knight1()
house.add_object(k2, 120, 120, 1)

first_game.add_pc_to_team(k)
first_game.new_area('Meadow', meadow)
Bandit = first_game.new_actor("Bandit", category="NPC", strange=12, wizdom=8, sprite=Sprite('images/npc_dr_knight_0 #176474.png'))
b = Bandit()
meadow.add_object(b, 320, 185, 1)
canvas.update()
#print(first_game.team_of_pc)
print(meadow.list_of_actors)

# Функции, которые будут вызываться при нажатии кнопки
first_game.set_area('House')
print(house.list_of_actors)
first_game.set_team(house,200, 120, 1)
def on_button_click4():
    first_game.set_area('House')
    first_game.set_team(house,120, 20, 1)
    print(house.list_of_actors)

def on_button_click5():
    first_game.set_area('Meadow')
    first_game.set_team(meadow,100, 260, 1)

# Создание кнопки
button4 = tk.Button(root, text="установить новую зону дом", command=on_button_click4)
button5 = tk.Button(root, text="установить новую зону луг", command=on_button_click5)

# Размещение кнопки на окне
exit_button.place(x = 1201,y = 60)
button4.place(x = 1201,y = 0)
button5.place(x = 1201,y = 30)

canvas.place(height = 700, width =700)

first_game.start_script(walk)
'''root.after(1000, timer)'''
first_game.timer()
# Основной цикл обработки событий
root.mainloop()
