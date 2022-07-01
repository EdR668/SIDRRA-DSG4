from tkinter import *
from time import *
class Menu4_2(Frame):
    def __init__(self, inicio):
        
        inicio.geometry("600x690")
        super().__init__(inicio)

        firtsbutton=PhotoImage(file='Images\\Botones\\boton1Menu2.png')
        image1=PhotoImage(file="Images\\Otras\\preguntacalorias.png")
        top1=PhotoImage(file="Images\\Otras\\top1.png")
        under1=PhotoImage(file="Images\\Otras\\under1.png")
        back=PhotoImage(file='Images\\Botones\\botonVolver.png')

        self.place(x=0,y=0)
        self.config(bg="white",width=600,height=690)

        self.label1=Label(self,text="Calculadora de calorias",font=("Little Comet Bubling Demo Version",28),bg="white",justify="left")
        self.label1.place(x=20,y=20)   
              
        self.label4=Label(self,text="Por favor ingrese los ingrediantes uno a uno  y  \n presione seleccionar",font=("Little Comet Bubling Demo Version",11),bg="white",justify="left")
        self.label4.place(x=285,y=440)
        
        self.ingrediente= StringVar()

        self.number1=Entry(self,width=25,font=("Little Comet Bubling Demo Version",12),textvariable=self.ingrediente)
        self.number1.place(x=20,y=450)
        
        self.button1=Button(self,image=firtsbutton,borderwidth=0,command=self.boton)
        self.button1.image = firtsbutton
        self.button1.place(x=20,y=580)
        
        self.label4=Label(self,text="Las calorias por gramo aproximadas segun \nlos datos del usuario son: ",font=("Little Comet Bubling Demo Version",12),bg="white",justify="left")
        self.label4.place(x=180,y=580)
       
        self.image1_label=Label(self,image=image1)
        self.image1_label.image = image1
        self.image1_label.place(x=20,y=80)
    
        self.buttonB=Button(self,image=back,borderwidth=0,command=self.back_to_Menu1)
        self.buttonB.image = back
        self.buttonB.place(x=480,y=25)
        
        self.top1_label=Label(image=top1)
        self.top1_label.image = top1
        self.top1_label.place(x=0,y=-15)
        
        self.under1_label=Label(image=under1)
        self.under1_label.image = under1
        self.under1_label.place(x=0,y=670)
        
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def back_to_Menu1(self):
        self.controller.back_to_Menu1()
        
    def boton(self):
        self.controller.boton()