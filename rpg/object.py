from rpg.sprite import *
class Object():
    def __init__(self, x, y, z, sprite, states, canvas, **params):
        self.pos_x = x
        self.pos_y = y
        self.pos_z = z
        self.sprite = sprite
        self.states = states
        self.canvas = canvas
        self.current_state = None # требуется закомментировать, если выбран вариант animate_sprite
        """self.current_state = 'right'""" # требуется раскомментировать, если выбран вариант animate_sprite
        self.set_state(next(iter(self.states)))  # Установка первого состояния # требуется закомментировать, если выбран вариант animate_sprite
        self.i = 0

    # требуется закомментировать, если выбран вариант animate_sprite
    def set_state(self, state_name):
        if self.current_state != state_name:
            self.current_state = state_name
            self.states[state_name].x = self.pos_x
            self.states[state_name].y = self.pos_y
            self.states[state_name].z = self.pos_z
            self.canvas.change_sprite(self.sprite, self.states[state_name])
            self.sprite = self.states[state_name]
            print(self.current_state)

    # требуется раскомментировать, если выбран вариант animate_sprite
'''    def animate_sprite(self, state_name):
        self.current_state = state_name
        if self.i != 5:
            this_sprite = self.states[state_name][self.i]
            self.canvas.change_sprite(self.sprite, this_sprite)
            self.sprite = self.states[state_name][self.i]
            self.i += 1
        else: self.i = 0
        print(self.i)'''