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
        self.speed = 3
        self.counter = self.speed
        self.cycle = cycle
        self.running = True

    def update(self):
        '''
        Меняет текущее изображение в списке изображений

        '''
        if self.running:
            self.counter -= 1  # Уменьшаем счетчик кадров
            if self.counter == 0:
                self.counter = self.speed
                if self.cycle:
                    # Циклическое переключение кадров
                    self.current_frame = (self.current_frame + 1) % len(self.images)
                else:
                    # Переключение кадров только если не достигнут последний кадр
                    if self.current_frame < len(self.images) - 1:
                        self.current_frame += 1
                    else:
                        # Остановка анимации, если это не циклическая анимация
                        self.running = False
                self.image = self.images[self.current_frame]
        else:
            if self.cycle:
                self.current_frame = 0
                self.image = self.images[self.current_frame]