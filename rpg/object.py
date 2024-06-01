from rpg.sprite import *
class Object():
    def __init__(self, x, y, z, sprite, states, **params):
        self.pos_x = x
        self.pos_y = y
        self.pos_z = z
        self.sprite = sprite
        self.states = states
        self.current_state = None
        self.set_state(next(iter(self.states)))  # Установка первого состояния

    def set_state(self, state_name):
        self.current_state = state_name
        self.sprite = self.states[state_name]