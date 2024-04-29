import tkinter as tk
def __init__(self, **params):
        self.rpg_dict_of_area = ()
        self.team_of_pc = []

def new_item(self, name, **params):
    self
def new_spell(self, name, **params):
    self

def new_actor(self, name, **params):
    self
def new_area(name, area):
    name = area()

def set_area(name):
    name
def add_pc_to_team(self, pc):
    self
def remove_pc_from_team(self, pc):
    self
def start_script(script):
    script
def stop_thread(script):
    script

class Graphics(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def add_sprite(self, item, x, y, **kwargs):
        tag = self.create_image(x, y, image=item, anchor='center',  **kwargs)
        return tag
    # anchor='center'

    def change_sprite(self, tag, **kwargs):
        self.itemconfig(tag, **kwargs)

    def delete_sprite(self, tag):
        self.delete(tag)

    def clear_all(self):
        self.delete("all")