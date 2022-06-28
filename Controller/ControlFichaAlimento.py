from tkinter import *
from PIL import Image, ImageTk

class ControlFichaAlimento:
    def __init__(self, model, view, wd, other_control, food_stuff):
        self.model = model
        self.view = view
        self.wd = wd
        self.other_control = other_control
        self.food_stuff = food_stuff

    def modify_ficha(self):
        img = Image.open("Images\\Image_alimentos\\"+(self.food_stuff.imagen))
        img = ImageTk.PhotoImage(img)
        # img=PhotoImage(file="Images\\Image_alimentos\\carne_res.jpg")
        self.view.l1.config(text=self.food_stuff.nombre)
        self.view.l2.config(text=str(self.food_stuff.tiempoCaducidad) + " días")
        self.view.image_lab.config(image=img)
        self.view.image_lab.image = img