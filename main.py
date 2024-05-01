from rpg.Graphics import *

root = tk.Tk()
root.geometry('1500x1500')

# Создание экземпляра класса Graphics, который будет взаимодействовать с окном
canvas = Graphics(root, width=1500, height=1500)

# Загрузка изображения
im1 = Sprite(image='images/fon1.png')
im2 = Sprite(image='images/person1.png')

# Добавление изображения на Canvas с помощью метода add_sprite
tag1 = canvas.add_sprite(im1.spr_image, 140, 140)
tag2 = canvas.add_sprite(im2.spr_image, 200, 100)

# Функции, которые будут вызываться при нажатии кнопки
def on_button_click():
    canvas.change_sprite(tag1, im2.spr_image)
def on_button_click1():
    canvas.delete_sprite(tag1)
def on_button_click2():
    canvas.update(tag2, 210, 100)
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
