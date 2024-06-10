from rpg.sprite import *
from rpg.graphics import *
from rpg.rectangle import Rectangle

class Object():
    def __init__(self, x, y, z, **params):
        self.pos_x = x
        self.pos_y = y
        self.pos_z = z
        self.current_state = None
        self.visible = True
        if self.states is not None:
            self.set_state(next(iter(self.states)))  # Установка первого состояния
        self.rectangle = Rectangle(x, y, 10, 10) # из спрайта

    def set_state(self, state_name):
        if self.current_state != state_name:
            self.current_state = state_name
            Graphics.canvas.change_sprite(self.sprite, self.states[state_name])
            self.sprite = self.states[state_name]

    def actor_in(self, actor):
        ''' Вызывается когда actor входит внутрь объекта '''
        pass

    def update(self):
        pass
