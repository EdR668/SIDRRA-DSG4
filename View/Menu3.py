from distutils.command.build_scripts import first_line_re
from tkinter import *

class Menu3(Frame):
    def __init__(self, inicio):
        inicio.geometry("600x690")
        super().__init__(inicio)

        firtsbutton=PhotoImage(file='Images\\Botones\\boton1Menu2.png')
        secondbutton=PhotoImage(file='Images\\Botones\\boton2Menu2.png')
        thirdbutton=PhotoImage(file='Images\\Botones\\boton1Menu3.png')
        fourthbutton=PhotoImage(file='Images\\Botones\\boton2Menu3.png')
        back=PhotoImage(file='Images\\Botones\\botonVolver.png')
        top1=PhotoImage(file="Images\\Otras\\top1.png")
        cat1=PhotoImage(file="Images\\Otras\\queIngredientes.png")
        under1=PhotoImage(file="Images\\Otras\\under1.png")

        self.place(x=0,y=0)
        self.config(bg="white",width=600,height=690)
        
        self.my_scrollbar=Scrollbar(self,orient=VERTICAL)
        
        self.label2=Label(self,text="Acontinuacion se mostrara la lista de todos las recetas ",font=("Little Comet Bubling Demo Version",14),bg="white")
        self.label2.place(x=20,y=20)
        
        self.selecion=Listbox(self,width=30,yscrollcommand=self.my_scrollbar.set,height=10,selectmode=MULTIPLE,font=("Little Comet Bubling Demo Version",14))
        self.selecion.place(x=300,y=70)
        
        self.my_scrollbar.config(command=self.selecion.yview)
        self.my_scrollbar.place(x=542,y=70,height=224)
        
        self.label1=Label(self, text='Las recetas selecionadas son : ',font=("Little Comet Bubling Demo Version",14),bg="white")
        self.label1.place(x=25,y=325)
        
        self.button1=Button(self,image=firtsbutton,borderwidth=0, command=self.select_all)
        self.button1.image=firtsbutton
        self.button1.place(x=50,y=120)
        
        self.button2=Button(self,image=secondbutton,borderwidth=0,command=self.delete_all)
        self.button2.image=secondbutton
        self.button2.place(x=50,y=200)
        
        self.button3=Button(self,image=thirdbutton,borderwidth=0,command=self.go_to_Menu3_1)
        self.button3.image=thirdbutton
        self.button3.place(x=360,y=490)
        
        self.button4=Button(self,image=fourthbutton,borderwidth=0,command=self.go_to_Menu3_2)
        self.button4.image=fourthbutton
        self.button4.place(x=360,y=570)
        
        self.button6=Button(self,image=back,borderwidth=0,command=self.back_to_Menu1)
        self.button6.image=back
        self.button6.place(x=450,y=20)
        
        self.top1_label=Label(image=top1)
        self.top1_label.image=top1
        self.top1_label.place(x=0,y=-15)
        
        self.cat1_label=Label(image=cat1)
        self.cat1_label.image=cat1
        self.cat1_label.place(x=20,y=450)
        
        self.under1_label=Label(image=under1)
        self.under1_label.image=under1
        self.under1_label.place(x=0,y=670)

        self.controller = None
    
    def set_controller(self, controller):
        self.controller = controller
        self.fill_recipes()

    def fill_recipes(self):
        self.controller.fill_recipes()

    def select_all(self):
        self.controller.select_all()

    def delete_all(self):
        self.controller.delete_all()
        
    def back_to_Menu1(self):
        self.controller.back_to_Menu1()
    
    def go_to_Menu3_1(self):
        self.controller.go_to_Menu3_1()

    def go_to_Menu3_2(self):
        self.controller.go_to_Menu3_2()