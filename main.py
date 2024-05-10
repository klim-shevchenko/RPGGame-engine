from rpg.graphics import *
from rpg.sprite import *
from rpg.game import *
from rpg.area import *
from rpg.actor import *
import time

root = tk.Tk()
root.geometry('1500x1500')

def mouse_left_click(event):
    print("Left mouse button clicked at", event.x, event.y)

root.bind("<Button-1>", mouse_left_click)

# Создание экземпляра класса graphics, который будет взаимодействовать с окном
canvas = Graphics(root, width=1500, height=1500)

# Создание экземпляра класса game
first_game = Game(canvas)
house = Area()
meadow = Area()

# Загрузка изображения
im1_1 = Sprite('images/fon1.png')
im1_2 = Sprite('images/fon2.png')
im2_1 = Sprite('images/person1.png')
im2_2 = Sprite('images/person2.png')

'''# Добавление изображения на Canvas с помощью метода add_sprite
canvas.add_sprite(im1_1, 140, 140, 0)
canvas.add_sprite(im2_1, 200, 100, 1)'''

# actor1 = Actor("Person1", "NPC", "warrior", 1, "human", 10, 10, 10, 10,10,10, 200, 205, 1, im2_1)
# actor2 = Actor("Person2", "NPC", "warrior", 1, "human", 10, 10, 10, 10,10,10, 120, 185, 1, im2_2)

house.add_sprite(Sprite('images/fon1.png'), 140, 140, 0)
meadow.add_sprite(Sprite('images/fon2.png'), 240, 140, 0)
first_game.new_area('House', house)
Knight = first_game.new_actor('Knight', category='pc', strange=5, wizdom=10, sprite=Sprite('images/person1.png'))
k = Knight()
first_game.add_pc_to_team(k)
#house.add_object(k, 250, 250, 1)
first_game.new_area('Meadow', meadow)
Bandit = first_game.new_actor("Bandit", category="NPC", strange=12, wizdom=8, sprite=Sprite('images/person2.png'))
b = Bandit()
meadow.add_object(b, 320, 185, 1)
canvas.update()
print(first_game.team_of_pc)
print(house.list_of_actors)

# Функции, которые будут вызываться при нажатии кнопки
'''def on_button_click():
    canvas.change_sprite(im2_1, im2_2.image)
def on_button_click1():
    canvas.delete_sprite(im1_1)
def on_button_click2():
    im2_1.update(250, 100)
    #im1_1.update(140, 140)
    canvas.update()
def on_button_click3():
    canvas.clear_all()'''
def on_button_click4():
    first_game.set_area('House')
    first_game.set_team(house,400, 20, 1)
    print(house.list_of_actors)
    canvas.update()

def on_button_click5():
    first_game.set_area('Meadow')
    first_game.set_team(meadow,100, 260, 1)
    canvas.update()

# Создание кнопки
'''button = tk.Button(root, text="поменять спрайт", command=on_button_click)
button1 = tk.Button(root, text="удалить спрайт", command=on_button_click1)
button2 = tk.Button(root, text="передвинуть спрайт", command=on_button_click2)
button3 = tk.Button(root, text="очистить всё", command=on_button_click3)'''
button4 = tk.Button(root, text="установить новую зону дом", command=on_button_click4)
button5 = tk.Button(root, text="установить новую зону луг", command=on_button_click5)

# Размещение кнопки на окне
'''button.pack()
button1.pack()
button2.pack()
button3.pack()'''
button4.pack()
button5.pack()
canvas.pack()
# Основной цикл обработки событий
root.mainloop()
