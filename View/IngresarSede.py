from tkinter import *
from tkinter import ttk
from unittest import TestCase

class IngresarSede(Frame):
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

        self.label1=Label(self,text="Ingrese la nueva sede",font=("Little Comet Bubling Demo Version",16,"bold"),bg="white",justify="left")
        self.label1.place(x=20,y=20) 

        self.label_nombre = Label(self, text="Ingrese el nombre:", bg="white", justify="center",font=("Little Comet Bubling Demo Version",10,"bold"))
        self.label_nombre.place(x=180,y=160)

        self.var_nombre = StringVar()
        self.entry_nombre = Entry(self,textvariable=self.var_nombre)
        self.entry_nombre.config(width=40)
        self.entry_nombre.place(x=180,y=185)

        self.label_ciudad = Label(self, text="Ingrese la ciudad:", bg="white", justify="center",font=("Little Comet Bubling Demo Version",10,"bold"))
        self.label_ciudad.place(x=180,y=280)

        self.var_ciudad = StringVar()
        self.entry_ciudad = Entry(self,textvariable=self.var_ciudad)
        self.entry_ciudad.config(width=40)
        self.entry_ciudad.place(x=180,y=305)

        self.label_pais = Label(self, text="Ingrese el país:", bg="white", justify="center",font=("Little Comet Bubling Demo Version",10,"bold"))
        self.label_pais.place(x=180,y=400)

        self.var_pais = StringVar()
        self.text_pais = Entry(self,textvariable=self.var_pais)
        self.text_pais.config(width=40)
        self.text_pais.place(x=180,y=425)

        self.button_back=Button(self,borderwidth=0,image=back,command=self.back_to_Menu1)
        self.button_back.image=back
        self.button_back.place(x=450,y=20)

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

    def obtain_data(self):
        self.controller.obtain_data()

    def back_to_Menu1(self):
        self.controller.back_to_Menu1()