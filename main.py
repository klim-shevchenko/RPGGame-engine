from rpg.graphics import *
from rpg.sprite import *

root = tk.Tk()
root.geometry('1500x1500')

# Создание экземпляра класса Graphics, который будет взаимодействовать с окном
canvas = Graphics(root, width=1500, height=1500)

# Загрузка изображения
im1_1 = Sprite(image='images/fon1.png')
im2_1 = Sprite(image='images/person1.png')
im2_2 = Sprite(image='images/person2.png')

# Добавление изображения на Canvas с помощью метода add_sprite
canvas.add_sprite(im1_1, 140, 140, 1)
canvas.add_sprite(im2_1, 200, 100, 0)

#canvas.update()

# Функции, которые будут вызываться при нажатии кнопки
def on_button_click():
    canvas.change_sprite(im2_1, im2_2.image)
def on_button_click1():
    canvas.delete_sprite(im1_1)
def on_button_click2():
    im2_1.update(canvas, 250, 100)
    im1_1.update(canvas, 140, 140)
    canvas.update()
def on_button_click3():
    canvas.clear_all()

# Создание кнопки
button = tk.Button(root, text="поменять спрайт", command=on_button_click)
button1 = tk.Button(root, text="удалить спрайт", command=on_button_click1)
button2 = tk.Button(root, text="передвинуть спрайт", command=on_button_click2)
button3 = tk.Button(root, text="очистить всё", command=on_button_click3)

# Размещение кнопки на окне
button.pack()
button1.pack()
button2.pack()
button3.pack()
canvas.pack()
# Основной цикл обработки событий
root.mainloop()
