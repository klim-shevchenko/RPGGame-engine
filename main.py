from rpg.graphics import *
from rpg.sprite import *
from rpg.game import *
from rpg.area import *
from rpg.actor import *
import time
import random
from rpg.rectangle import *
from bggame import *

root = tk.Tk()
root.geometry('1500x1500')

exit_button = tk.Button(root, text="Exit", fg="red", command=root.destroy)
# Создание экземпляра класса graphics, который будет взаимодействовать с окном
canvas = Graphics(root, width=1500, height=1500)
Graphics.canvas = canvas  # Присваиваем canvas в статическое поле

# создание новой игры
BaldursGame(canvas, root)

canvas.place(height = 1500, width =1500)
BaldursGame.timer

# Основной цикл обработки событий
root.mainloop()
