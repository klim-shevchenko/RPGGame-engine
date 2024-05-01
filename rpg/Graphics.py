import tkinter as tk
class Graphics(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def add_sprite(self, item, x, y, **kwargs):
        tag = self.create_image(x, y, image=item, anchor='center',  **kwargs)
        return tag
    # anchor='center'

    def change_sprite(self, tag, new_image):
        self.itemconfig(tag, image=new_image)

    def delete_sprite(self, tag):
        self.delete(tag)

    def clear_all(self):
        self.delete("all")

    def update(self, tag, new_x, new_y):
        self.coords(tag, new_x, new_y)
class Sprite():
    def __init__(self, image):
        self.spr_image = tk.PhotoImage(file=image)
