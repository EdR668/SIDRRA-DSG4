from tkinter import *

class Menu3_2 (Frame):
    def __init__(self, inicio):
        inicio.geometry("600x690")
        super().__init__(inicio)

        top1=PhotoImage(file="Images\\Otras\\top1.png")
        back=PhotoImage(file='Images\\Botones\\botonVolver.png')
        under1=PhotoImage(file="Images\\Otras\\under1.png")
        
        self.place(x=0,y=0)
        self.config(bg="white",width=600,height=690) 
        
        self.my_scrollbar1=Scrollbar(self,orient=VERTICAL)
        
        self.canva1=Canvas(self,width=580,height=600,bg="white",yscrollcommand=self.my_scrollbar1.set)
        
        self.my_scrollbar1.config(command=self.canva1.yview)
        self.my_scrollbar1.place(x=580,y=70,height=600)
        
        self.frame4=Frame(self.canva1)
        self.canva1.place(x=0,y=70)
        self.canva1.create_window((0,0),window=self.frame4,anchor="nw")
        
        self.label2=Label(self.frame4,font=("Little Comet Bubling Demo Version",11),bg="white",text="",justify="left")
        self.label2.pack()
        
        self.canva1.bind('<Configure>', lambda e: self.canva1.configure(scrollregion=self.canva1.bbox("all")))

        self.top1_label=Label(image=top1)
        self.top1_label.image=top1
        self.top1_label.place(x=0,y=-15)
        
        self.label1=Label(self,text="Acontinuacion se mostrara los detalles de \nlos ingredientes de las recetas selecionadas",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
        self.label1.place(x=20,y=20)    
        
        self.buttonB=Button(self, image=back,borderwidth=0,command=self.back_to_Menu3)
        self.buttonB.image = back
        self.buttonB.place(x=440,y=20)
        
        self.under1_label=Label(image=under1)
        self.under1_label.image=under1
        self.under1_label.place(x=0,y=670)

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller
        self.controller.show_recipes_ingredients()

    def back_to_Menu3(self):
        self.controller.back_to_Menu3()

    def show_recipes_ingredients(self):
        self.controller.show_recipes_ingredients()
