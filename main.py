from rpg.graphics import *
from rpg.sprite import *
from rpg.game import *
from rpg.area import *
from rpg.actor import *
import datetime
from rpg.rectangle import *

def timer():
    first_game.update()
    root.after(50, timer)

root = tk.Tk()
root.geometry('1500x1500')

exit_button = tk.Button(root, text="Exit", fg="red", command=root.destroy)
#exit_button.pack()

# Создание экземпляра класса graphics, который будет взаимодействовать с окном
canvas = Graphics(root, width=1500, height=1500)

# Создание экземпляра класса game
first_game = Game(canvas, root)
house = Area()
meadow = Area()

# Загрузка изображения в зоны, добавление зон в игру

house.add_sprite(Sprite('images/fon1.png'), 140, 140, 0)
meadow.add_sprite(Sprite('images/fon2.png'), 240, 140, 0)
first_game.new_area('House', house)
Knight = first_game.new_actor('Knight', category='pc', strange=5, wizdom=10, sprite=Sprite('images/person1.png'))
k = Knight()
first_game.add_pc_to_team(k)
k.speed_x = 2
k.speed_y = 1
first_game.new_area('Meadow', meadow)
Bandit = first_game.new_actor("Bandit", category="NPC", strange=12, wizdom=8, sprite=Sprite('images/person2.png'))
b = Bandit()
meadow.add_object(b, 320, 185, 1)
canvas.update()
print(first_game.team_of_pc)
print(house.list_of_actors)

# Функции, которые будут вызываться при нажатии кнопки

first_game.set_area('House')
first_game.set_team(house,270, 120, 1)
def on_button_click4():
    first_game.set_area('House')
    first_game.set_team(house,400, 20, 1)
    print(house.list_of_actors)

def on_button_click5():
    first_game.set_area('Meadow')
    first_game.set_team(meadow,100, 260, 1)

# Создание кнопки
button4 = tk.Button(root, text="установить новую зону дом", command=on_button_click4)
button5 = tk.Button(root, text="установить новую зону луг", command=on_button_click5)

# обрабока клика мыши
def mouse_left_click(event):
    print("Left mouse button clicked at", event.x, event.y)
    if event.y <= 500 and event.x <=500:
        k.search_position(event.x, event.y)
canvas.bind("<Button-1>", mouse_left_click)


#экземпляры класса MyRectangle
rect1 = MyRectangle(0, 0, 4, 4)
rect2 = MyRectangle(1, 1, 2, 2)

if rect2.is_in(rect1):
    print("Прямоугольник rect2 находится внутри прямоугольника rect1")
else:
    print("Прямоугольник rect2 не находится внутри прямоугольника rect1")


# Размещение кнопки на окне
exit_button.place(x = 700,y = 60)
button4.pack()
button5.pack()
canvas.place(height = 1500, width =1500)
root.after(1000, timer)
# Основной цикл обработки событий
root.mainloop()
