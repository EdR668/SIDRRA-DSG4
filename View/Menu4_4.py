from tkinter import *

class Menu4_4(Frame):
    def __init__(self, inicio):
        inicio.geometry("600x690")
        super().__init__(inicio)

        food1=PhotoImage(file="Images\\Otras\\reducion1.png")
        food2=PhotoImage(file="Images\\Otras\\reducion2.png")
        food3=PhotoImage(file="Images\\Otras\\reducion3.png")
        food4=PhotoImage(file="Images\\Otras\\reducion4.png")
        food5=PhotoImage(file="Images\\Otras\\reducion5.png")
        food6=PhotoImage(file="Images\\Otras\\reducion6.png")
        food7=PhotoImage(file="Images\\Otras\\reducion7.png")
        food8=PhotoImage(file="Images\\Otras\\reducion8.png")
        back=PhotoImage(file='Images\\Botones\\botonVolver.png')
        top1=PhotoImage(file="Images\\Otras\\top1.png")
        under1=PhotoImage(file="Images\\Otras\\under1.png")
        
        self.place(x=0,y=0)
        self.config(bg="white",width=600,height=690)
        
        self.my_scrollbar1=Scrollbar(self,orient=VERTICAL)
        
        self.canva1=Canvas(self,width=575,height=600,bg="white",yscrollcommand=self.my_scrollbar1.set)
        
        self.my_scrollbar1.config(command=self.canva1.yview)
        self.my_scrollbar1.place(x=580,y=70,height=600)
        
        self.frame4=Frame(self.canva1,bg="white")
        self.frame4.grid(columnspan=3,rowspan=12)
        
        self.canva1.place(x=0,y=70)
        self.canva1.create_window((0,0),window=self.frame4,anchor="nw")
        
        self.label2=Label(self.frame4,font=("Little Comet Bubling Demo Version",11),bg="white",text="Acontinuacion se mostraran los mejores tips o maneras para reutilizar la comida",justify="left")
        self.label2.grid(column=1,row=0)
        
        self.food1_label=Label(self.frame4,image=food1)
        self.food1_label.image=food1
        self.food1_label.grid(column=1,row=1)
        
        self.food2_label=Label(self.frame4,image=food2)
        self.food2_label.image=food2
        self.food2_label.grid(column=1,row=2)
        
        self.food3_label=Label(self.frame4,image=food3)
        self.food3_label.image=food3
        self.food3_label.grid(column=1,row=3)
        
        self.food4_label=Label(self.frame4,image=food4)
        self.food4_label.image=food4
        self.food4_label.grid(column=1,row=4)
        
        self.food5_label=Label(self.frame4,image=food5)
        self.food5_label.image=food5
        self.food5_label.grid(column=1,row=5)
        
        self.food6_label=Label(self.frame4,image=food6)
        self.food6_label.image=food6
        self.food6_label.grid(column=1,row=6)
        
        self.food7_label=Label(self.frame4,image=food7)
        self.food7_label.image=food7
        self.food7_label.grid(column=1,row=7)
        
        self.food8_label=Label(self.frame4,image=food8)
        self.food8_label.image=food8
        self.food8_label.grid(column=1,row=8)
        
        self.canva1.bind('<Configure>', lambda e: self.canva1.configure(scrollregion=self.canva1.bbox("all")))
        
        self.label1=Label(self,text="Reutilizacion de residuos",font=("Little Comet Bubling Demo Version",28),bg="white",justify="left")
        self.label1.place(x=20,y=20)    
        
        self.buttonB=Button(self,image=back,borderwidth=0,command=self.back_to_Menu4)
        self.buttonB.image=back
        self.buttonB.place(x=480,y=25)
        
        self.top1_label=Label(image=top1)
        self.top1_label.image=top1
        self.top1_label.place(x=0,y=-15)
        
        self.under1_label=Label(image=under1)
        self.under1_label.image=under1
        self.under1_label.place(x=0,y=670)

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def back_to_Menu4(self):
        self.controller.back_to_Menu4()