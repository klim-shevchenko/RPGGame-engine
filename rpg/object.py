from rpg.sprite import *
class Object():
    def __init__(self, x, y, z, sprite, states, canvas, **params):
        self.pos_x = x
        self.pos_y = y
        self.pos_z = z
        self.sprite = sprite
        self.states = states
        self.canvas = canvas
        self.current_state = None
        self.set_state(next(iter(self.states)))  # Установка первого состояния

    def set_state(self, state_name):
        if self.current_state != state_name:
            self.current_state = state_name
            self.states[state_name].x = self.pos_x
            self.states[state_name].y = self.pos_y
            self.states[state_name].z = self.pos_z
            self.sprite = self.states[state_name]
            self.canvas.change_sprite(self.sprite, self.states[state_name])
            print(self.current_state)