from rpg.sprite import *
from rpg.graphics import *
class Object():
    def __init__(self, x, y, z, **params):
        """класс объекта"""
        self.pos_x = x
        self.pos_y = y
        self.pos_z = z
        self.sprite = None
        #self.states = states
        self.current_state = None
        if self.states is not None:
            self.set_state(next(iter(self.states)))

    def set_state(self, state_name):
        """ устанавливает новое состояние"""
        if self.current_state != state_name:
            self.current_state = state_name
            Graphics.canvas.change_sprite(self.sprite, self.states[state_name])
            self.sprite = self.states[state_name]

    def animate_sprite(self, state_name):
        self.current_state = state_name
        if self.i != 5:
            this_sprite = self.states[state_name][self.i]
            Graphics.canvas.change_sprite(self.sprite, this_sprite)
            self.sprite = self.states[state_name][self.i]
            self.i += 1
        else: self.i = 0