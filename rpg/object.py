from rpg.sprite import *
from rpg.graphics import *
class Object():
    def __init__(self, x, y, z, sprite, states, **params):
        self.pos_x = x
        self.pos_y = y
        self.pos_z = z
        self.sprite = sprite
        self.states = states
        self.current_state = None # требуется закомментировать, если выбран вариант animate_sprite
        #self.current_state = 'right' # требуется раскомментировать, если выбран вариант animate_sprite
        self.set_state(next(iter(self.states)))  # Установка первого состояния # требуется закомментировать, если выбран вариант animate_sprite
        self.i = 0

    # требуется закомментировать, если выбран вариант animate_sprite
    def set_state(self, state_name):
        if self.current_state != state_name:
            self.current_state = state_name
            Graphics.canvas.change_sprite(self.sprite, self.states[state_name])
            self.sprite = self.states[state_name]
            print(self.current_state)

    def animate_sprite(self, state_name):
        self.current_state = state_name
        if self.i != 5:
            this_sprite = self.states[state_name][self.i]
            Graphics.canvas.change_sprite(self.sprite, this_sprite)
            self.sprite = self.states[state_name][self.i]
            self.i += 1
        else: self.i = 0
        print(self.i)