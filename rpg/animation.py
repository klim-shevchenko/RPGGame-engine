from rpg.sprite import *
import tkinter as tk

class Animation(Sprite):
    def __init__(self, frames, cycle=True):
        '''
        Класс анимации спрайта

        :param frames: списко изображений
        '''
        super().__init__(frames[0])
        self.images = frames
        self.current_frame = 0
        self.images = [tk.PhotoImage(file=frame) for frame in frames]  # Загрузка всех кадров анимации
        self.image = self.images[0]  # Установка начального изображения
        self.speed = 0
        self.cycle = cycle
        self.running = True

    def update(self):
        '''
        Меняет текущее изображение в списке изображений

        '''
        if self.running:
            if self.speed == 3:
                self.current_frame = (self.current_frame + 1) % len(self.images)  # Циклическое переключение кадров
                self.image = self.images[self.current_frame]
                self.speed = 0
            self.speed += 1
        else:
            self.current_frame = 0
            self.image = self.images[self.current_frame]
