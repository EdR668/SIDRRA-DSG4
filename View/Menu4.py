from tkinter import *

class Menu4(Frame):
    def __init__(self, inicio):
        inicio.geometry("600x690")
        super().__init__(inicio)
        
        string1="Acontinuacion se mostraran cuatro opciones las cuales aportaran \nal usuario mayor informacion , herramientas  y soluciones ,\ncon los cuales se podra faciliar una reducion casi al minimo de \nlos desperdicios alimenticios "

        back=PhotoImage(file='Images\\Botones\\botonVolver.png')
        cat1=PhotoImage(file="Images\\Otras\\elegirOpcion.png")
        firtsbutton=PhotoImage(file='Images\\Botones\\boton1Menu4.png')
        secondbutton=PhotoImage(file='Images\\Botones\\boton2Menu4.png')
        fourthbutton=PhotoImage(file='Images\\Botones\\boton4Menu4.png')
        top1=PhotoImage(file="Images\\Otras\\top1.png")
        under1=PhotoImage(file="Images\\Otras\\under1.png")

        self.place(x=0,y=0)
        self.config(bg="white",width=600,height=690)
        
        self.label1=Label(self,text="Utilidades",font=("Little Comet Bubling Demo Version",32),bg="white")
        self.label1.place(x=220,y=40)

        self.label2=Label(self,text=string1,font=("Little Comet Bubling Demo Version",16),bg="white",justify="left")
        self.label2.place(x=30,y=90)
        
        self.button6=Button(self,image=back,borderwidth=0,command=self.back_to_Menu1)
        self.button6.image = back
        self.button6.place(x=480,y=25)
        
        self.cat1_label=Label(image=cat1)
        self.cat1_label.image = cat1
        self.cat1_label.place(x=80,y=220)
        
        self.button1=Button(self,image=firtsbutton,borderwidth=0,command=self.go_to_Menu4_1)
        self.button1.image = firtsbutton
        self.button1.place(x=60,y=490)
        
        self.button2=Button(self,image=secondbutton,borderwidth=0)
        self.button2.image = secondbutton
        self.button2.place(x=60,y=570)
        
        self.button4=Button(self,image=fourthbutton,borderwidth=0,command=self.go_to_Menu4_4)
        self.button4.image = fourthbutton
        self.button4.place(x=350,y=570)
        
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

    def go_to_Menu4_1(self):
        self.controller.go_to_Menu4_1()

    def go_to_Menu4_4(self):
        self.controller.go_to_Menu4_4()