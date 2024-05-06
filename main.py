from rpg.graphics import *
from rpg.sprite import *
from rpg.game import *
from rpg.area import *
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
'''im2_1 = sprite(image='images/person1.png')
im2_2 = sprite(image='images/person2.png')'''

'''# Добавление изображения на Canvas с помощью метода add_sprite
canvas.add_sprite(im1_1, 140, 140, 0)
canvas.add_sprite(im2_1, 200, 100, 1)'''

house.add_sprite(im1_1, 140, 140, 0)
meadow.add_sprite(im1_2, 140, 140, 0)
first_game.new_area('House', house)
first_game.new_area('Meadow', meadow)
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
    canvas.clear_all()
    first_game.set_area('House')
    canvas.update()

def on_button_click5():
    canvas.clear_all()
    first_game.set_area('Meadow')
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
