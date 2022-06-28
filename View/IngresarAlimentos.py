from tkinter import *
from tkinter import ttk
from unittest import TestCase

class IngresarAlimentos(Frame):
    def __init__(self, inicio):
        inicio.geometry("600x690")
        super().__init__(inicio)

        back=PhotoImage(file='Images\\Botones\\botonVolver.png')
        top1=PhotoImage(file="Images\\Otras\\top1.png")
        under1=PhotoImage(file="Images\\Otras\\under1.png")
        add = PhotoImage(file="Images\\Botones\\icons8-más-2-matemáticas-30.png")

        self.place(x=0,y=0)
        self.config(width=600,height=690)
        self.config(bg="white")

        self.label1=Label(self,text="Ingrese el nuevo alimento",font=("Little Comet Bubling Demo Version",16,"bold"),bg="white",justify="left")
        self.label1.place(x=20,y=20) 

        self.label_nombre = Label(self, text="Ingrese el nombre:", bg="white", justify="center",font=("Little Comet Bubling Demo Version",10,"bold"))
        self.label_nombre.place(x=10,y=80)

        self.var_nombre = StringVar()
        self.entry_nombre = Entry(self,textvariable=self.var_nombre)
        self.entry_nombre.config(width=40)
        self.entry_nombre.place(x=10,y=105)

        self.label_caducidad = Label(self, text="", bg="white", justify="center",font=("Little Comet Bubling Demo Version",10,"bold"))
        self.label_caducidad.place(x=300,y=140)

        self.label_tipo = Label(self, text="Ingrese el tipo del alimento:", bg="white", justify="center",font=("Little Comet Bubling Demo Version",10,"bold"))
        self.label_tipo.place(x=10,y=140)

        self.var_tipo = StringVar()
        self.entry_tipo = Entry(self,textvariable=self.var_tipo)
        self.entry_tipo.config(width=40)
        self.entry_tipo.place(x=10,y=165)

        self.label_uso = Label(self, text="Ingrese el uso común:", bg="white", justify="center",font=("Little Comet Bubling Demo Version",10,"bold"))
        self.label_uso.place(x=10,y=200)

        self.text_uso = Text(self)
        self.text_uso.config(height=10,width=30)
        self.text_uso.place(x=10,y=225)

        self.label_caracteristicas = Label(self, text="Ingrese características:", bg="white", justify="center",font=("Little Comet Bubling Demo Version",10,"bold"))
        self.label_caracteristicas.place(x=300,y=200)

        self.text_caracteristicas = Text(self)
        self.text_caracteristicas.config(height=10,width=30)
        self.text_caracteristicas.place(x=300,y=225)

        self.label_props = Label(self, text="Ingrese propiedades nutricionales:", bg="white", justify="center",font=("Little Comet Bubling Demo Version",10,"bold"))
        self.label_props.place(x=10,y=410)

        self.text_props = Text(self)
        self.text_props.config(height=10,width=30)
        self.text_props.place(x=10,y=435)

        self.label_comb = Label(self, text="Organico / No organico", bg="white", justify="center",font=("Little Comet Bubling Demo Version",10,"bold"))
        self.label_comb.place(x=300,y=80)

        self.comb_box = ttk.Combobox(self, state="readonly", values=["Organico", "No organico"])
        self.comb_box.place(x=300,y=105)
        self.comb_box.bind("<<ComboboxSelected>>", self.comb_change)

        self.button_back=Button(self,borderwidth=0,image=back,command=self.back_to_Menu1)
        self.button_back.image=back
        self.button_back.place(x=450,y=20)

        self.label_image = Text(self, bg="white",font=("Little Comet Bubling Demo Version",10,"normal"), height=2,width=30)
        self.label_image.place(x=340,y=500)

        self.button_imagen=Button(self,borderwidth=5,text="Seleccionar imagen", font=("Little Comet Bubling Demo Version",12,"bold"),command=self.select_image, padx=10,bg="#E1E1E1", relief="flat")
        self.button_imagen.place(x=350,y=540)

        self.label_cant = Label(self, text="", bg="white", justify="center",font=("Little Comet Bubling Demo Version",10,"bold"))
        self.label_cant.place(x=300,y=410)

        self.button_agregar=Button(self,borderwidth=5,text="Agregar", font=("Little Comet Bubling Demo Version",12,"bold"),image=add,compound=RIGHT, padx=10,bg="#E1E1E1", relief="flat",command=self.obtain_data)
        self.button_agregar.image = add
        self.button_agregar.place(x=400,y=600)

        self.top1_label=Label(self,image=top1)
        self.top1_label.image = top1
        self.top1_label.place(x=0,y=-15)
        
        self.under1_label=Label(self,image=under1)
        self.under1_label.image=under1
        self.under1_label.place(x=0,y=670)

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def comb_change(self, event):
        self.controller.comb_change(event)

    def select_image(self):
        self.controller.select_image()

    def obtain_data(self):
        self.controller.obtain_data()

    def back_to_Menu1(self):
        self.controller.back_to_Menu1()