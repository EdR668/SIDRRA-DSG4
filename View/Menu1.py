from tkinter import *


class Menu1(Frame):
    def __init__(self, inicio):
        inicio.geometry("445x690")
        super().__init__(inicio)
        
        self.place(x=0,y=0,width=445,height=690)
        self.config(bg="white")

        img=PhotoImage(file="Images\\Fondos\\fondo2.png")
        firtsbutton = PhotoImage(file='Images\\Botones\\boton1.png')
        secondbutton=PhotoImage(file='Images\\Botones\\boton2.png')
        thirdbutton=PhotoImage(file='Images\\Botones\\boton3.png')
        fourthbutton=PhotoImage(file='Images\\Botones\\boton4.png')
        zero=PhotoImage(file="Images\\Fondos\\banco3.png")
        see = PhotoImage(file='Images\\Botones\\icons8-almuerzo-48.png')
        add = PhotoImage(file='Images\\Botones\\icons8-más-2-matemáticas-30.png')

        self.img_label=Label(self,image=img)
        self.img_label.image= img
        self.img_label.place(x=0,y=-10)
        self.img_label.pack()

        self.button1=Button(self,image=firtsbutton,command=self.go_to_Menu2,borderwidth=0)
        self.button1.image=firtsbutton
        self.button1.place(x=113,y=305)
        

        self.button2=Button(self,image=secondbutton,command=self.go_to_Menu3,borderwidth=0)
        self.button2.image=secondbutton
        self.button2.place(x=113,y=402)

        self.button3=Button(self,image=thirdbutton,command=self.go_to_Menu4,borderwidth=0)
        self.button3.image=thirdbutton
        self.button3.place(x=113,y=502)

        self.button4=Button(self,image=fourthbutton,command=self.go_to_Menu5,borderwidth=0)
        self.button4.image=fourthbutton
        self.button4.place(x=112,y=592)

        self.ver_alimentos=Button(self,image=see,borderwidth=0,command=self.go_to_Mostrar_menu)
        self.ver_alimentos.image = see
        self.ver_alimentos.place(x=370,y=510)

        self.ingresar_alimentos=Button(self,image=add,borderwidth=0,command=self.go_to_Mostrar_ingreso)
        self.ingresar_alimentos.image = add
        self.ingresar_alimentos.place(x=380,y=580)
        
        self.zero_label=Label(self,image=zero, bg="white")
        self.zero_label.image=zero
        self.zero_label.place(x=320,y=100,width=120,height=120)

        self.controller = None
    
    def set_controller(self, controller):
        self.controller = controller
    
    def go_to_Menu2(self):
        self.controller.go_to_Menu2()
    
    def go_to_Menu3(self):
        self.controller.go_to_Menu3()
    
    def go_to_Menu4(self):
        self.controller.go_to_Menu4()
    
    def go_to_Menu5(self):
        self.controller.go_to_Menu5()
    
    def go_to_Mostrar_menu(self):
        self.controller.go_to_Mostrar_menu()

    def go_to_Mostrar_ingreso(self):
        self.controller.go_to_Mostrar_ingreso()


        