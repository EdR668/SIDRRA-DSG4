from tkinter import *

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
        
        self.label2=Label(self,text="Acontinuacion se le pedira al usuario que ingrese ciertos datos para \npoder calcular la cantidad de calorias aproximada que necesita diariamente",font=("Little Comet Bubling Demo Version",12),bg="white",justify="left")
        self.label2.place(x=20,y=390)   
        
        self.selecion=Listbox(self,width=15,height=2,font=("Little Comet Bubling Demo Version",14))
        self.selecion.place(x=215,y=480)
        
        self.label3=Label(self,text="Por favor ingrese su sexo",font=("Little Comet Bubling Demo Version",11),bg="white",justify="left")
        self.label3.place(x=215,y=440)
        
        self.number4=Entry(self,width=20,font=("Little Comet Bubling Demo Version",12))
        self.number4.place(x=355,y=510)
                
        self.label4=Label(self,text="Por favor ingrese la cantidad de veces \nque hace ejercicio a la semana con un \nnumero entre 0 y 14",font=("Little Comet Bubling Demo Version",11),bg="white",justify="left")
        self.label4.place(x=355,y=440)
        
        self.number1=Entry(self,width=25,font=("Little Comet Bubling Demo Version",12))
        self.number1.place(x=20,y=450)
        
        self.number2=Entry(self,width=25,font=("Little Comet Bubling Demo Version",12))
        self.number2.place(x=20,y=500)
        
        self.number3=Entry(self,width=25,font=("Little Comet Bubling Demo Version",12))
        self.number3.place(x=20,y=550)
        
        
        self.button1=Button(self,image=firtsbutton,borderwidth=0)
        self.button1.image = firtsbutton
        self.button1.place(x=20,y=580)
        
        self.label4=Label(self,text="Las calorias necesarias aproximadas segun \nlos datos del usuario son : ",font=("Little Comet Bubling Demo Version",12),bg="white",justify="left")
        self.label4.place(x=180,y=580)
       
        self.image1_label=Label(self,image=image1)
        self.image1_label.image = image1
        self.image1_label.place(x=20,y=80)
    
        self.buttonB=Button(self,image=back,borderwidth=0,command=self.back_to_Menu4)
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

    def back_to_Menu4(self):
        self.controller.back_to_Menu4()