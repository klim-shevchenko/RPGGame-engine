from rpggame import *

root = tk.Tk()
root.geometry('400x400')

# Создание экземпляра класса Graphics, который будет взаимодействовать с окном
canvas = Graphics(root, width=1500, height=1500)
canvas.pack()

# Загрузка изображения
image1 = tk.PhotoImage(file='C:/Users/KShevchenko/PycharmProjects/RPGGame-engine/images/fon1.png')
image2 = tk.PhotoImage(file='C:/Users/KShevchenko/PycharmProjects/RPGGame-engine/images/person1.png')

# Добавление изображения на Canvas с помощью метода add_sprite
tag1 = canvas.add_sprite(image1, 100, 100)
tag2 = canvas.add_sprite(image2, 150, 100)
#tag2 = canvas.add_sprite(image2, image=image2, subset =" 100 100 200 200")
# Основной цикл обработки событий
root.mainloop()
