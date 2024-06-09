from rpg.sprite import *
from rpg.graphics import *
class Object():
    def __init__(self, x, y, z, **params):
        self.pos_x = x
        self.pos_y = y
        self.pos_z = z
        self.current_state = None
        if self.states is not None:
            self.set_state(next(iter(self.states)))  # Установка первого состояния


    def set_state(self, state_name):
        if self.current_state != state_name:
            self.current_state = state_name
            Graphics.canvas.change_sprite(self.sprite, self.states[state_name])
            self.sprite = self.states[state_name]