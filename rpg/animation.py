from rpg.sprite import *
import tkinter as tk

class Animation(Sprite):
    def __init__(self, frames):
        super().__init__(frames[0])
        self.images = frames
        self.current_frame = 0
        self.images = [tk.PhotoImage(file=frame) for frame in frames]  # Загрузка всех кадров анимации
        self.image = self.images[0]  # Установка начального изображения
        self.speed = 0
        self.running = True

    def update(self):
        """меняет текущий спрайт в списке"""
        if self.running:
            if self.speed == 3:
                self.current_frame = (self.current_frame + 1) % len(self.images)  # Циклическое переключение кадров
                self.image = self.images[self.current_frame]
                self.speed = 0
            self.speed += 1
        else:
            self.current_frame = 0
            self.image = self.images[self.current_frame]