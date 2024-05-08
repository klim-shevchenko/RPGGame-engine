from rpg.graphics import *
from rpg.sprite import *
from rpg.game import *
from rpg.area import *
from rpg.actor import *
import time

root = tk.Tk()
root.geometry('1500x1500')

# Создание экземпляра класса graphics, который будет взаимодействовать с окном
canvas = Graphics(root, width=1500, height=1500)

# Создание экземпляра класса game
first_game = Game(canvas)
house = Area()
meadow = Area()

# Загрузка изображения
im1_1 = Sprite(image='images/fon1.png')
im1_2 = Sprite(image='images/fon2.png')
im2_1 = Sprite(image='images/person1.png')
im2_2 = Sprite(image='images/person2.png')

'''# Добавление изображения на Canvas с помощью метода add_sprite
canvas.add_sprite(im1_1, 140, 140, 0)
canvas.add_sprite(im2_1, 200, 100, 1)'''

#actor1 = Actor("Person1", "NPC", "warrior", 1, "human", 10, 10, 10, 10,10,10, 200, 205, 1, im2_1)
#actor2 = Actor("Person2", "NPC", "warrior", 1, "human", 10, 10, 10, 10,10,10, 120, 185, 1, im2_2)

house.add_sprite(im1_1, 140, 140, 0)
meadow.add_sprite(im1_2, 140, 140, 0)
first_game.new_area('House', house)
knight = first_game.new_actor('Person1', 'NPC',200, 205, 1, im2_1)
house.add_object(knight)
first_game.new_area('Meadow', meadow)
bandit = first_game.new_actor("Person2", "NPC", 120, 185, 1, im2_2)
meadow.add_object(bandit)
canvas.update()

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

def on_button_click5():
    first_game.set_area('Meadow')

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
