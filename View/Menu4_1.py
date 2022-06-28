from tkinter import *

class Menu4_1(Frame):
    def __init__(self, inicio):
        inicio.geometry("600x690")
        super().__init__(inicio)

        self.string2="Primera mente partamos por recordar la piramide alimenticia la cual esta dividia en 5 niveles , el nivel mas bajo contiene a las harinas , cereales , patatas y legumbres, el nivel 4 contiene a las frutas y verduras , el nivel 3"
        self.string2+="contiene los lacteos ,a los huevos junto a las carnes blancas y magras el 2 escalon contiene a las carnes rojas procesados y embutidos , y finalmenete el primer nivel contien a los dulces , chucherias y untables"
        self.string3="La piramide alimenticia nos permite delimitar las diferentes clases de alimentos , esto nos ayuda bastante ya que podemos trazar un plan alimentcio basado en porciones y  escalas de la piramide nutricional"
        self.string3+=", por lo tanto una dieta saludable debe constar de : 3 porciones diarias entre harina y cereales , 6-7 porciones diarias entre frutas y verduras , 1-2 porciones diarias de lacteos , 3-5 raciones entre carne blanca, pescado y huevos a la semana , y esporadicamente una racion de carne roja"
        self.string4="Aproximadamente 60 porciento del peso corporal es agua , y cada uno de los sistemas humanos depende de ella , por lo qu estar bien hidratado es un es un factor muy importante en cuanto se trata a la salud"
        self.string4+=", aunque la cantidad de agua necesaria por persona varia por varios factores se recomienda que los hombres tomen alrededor de 13 taza y en el caso de las mujeres seria de 9 tazas "
        self.string5="Para mantener una dieta y cuerpo sano hay que realizar cierta actividad fisica tanto los hombres como las mujeres , lo mas recomendado es realizar al menos 150 minutos de actividad aerobica"
        self.string5+="moderada o 75 de actividad intensa , a su vez se deberian realizar al menos dos seciones de fortalezimiento muscular a la semana para los grupos musculares principales"

        image1=PhotoImage(file="Images\\Otras\\dietasana.png")
        image2=PhotoImage(file="Images\\Otras\\piramide.png")
        image3=PhotoImage(file="Images\\Otras\\porciones.png")
        image4=PhotoImage(file="Images\\Otras\\cuantaAgua.png")
        image5=PhotoImage(file="Images\\Otras\\ejercicio.png")
        back=PhotoImage(file='Images\\Botones\\botonVolver.png')
        top1=PhotoImage(file="Images\\Otras\\top1.png")
        under1=PhotoImage(file="Images\\Otras\\under1.png")
        
        self.place(x=0,y=0)
        self.config(bg ="white",width=600,height=690)
        
        self.my_scrollbar1=Scrollbar(self,orient=VERTICAL)
        
        self.canva1=Canvas(self,width=575,height=600,bg="white",yscrollcommand=self.my_scrollbar1.set)
        
        self.my_scrollbar1.config(command=self.canva1.yview)
        self.my_scrollbar1.place(x=580,y=70,height=600)
        
        self.frame4=Frame(self.canva1,bg="white")
        self.frame4.grid(columnspan=4,rowspan=5)
        
        self.canva1.place(x=0,y=70)
        self.canva1.create_window((0,0),window=self.frame4,anchor="nw")
        
        self.image1_label=Label(self.frame4,image=image1)
        self.image1_label.image=image1
        self.image1_label.grid(column=0,row=0)
        
        self.label2=Label(self.frame4,font=("Little Comet Bubling Demo Version",11),bg="white",text="Para llevar una dieta y una vida saludable no \nes necesario ser excesivos ni extremistas ,\nbasta mayormente con ciertos habitos \ny practicas muy basicas",justify="left")
        self.label2.grid(column=1,row=0)
        
        self.image2_label=Label(self.frame4,image=image2)
        self.image2_label.image=image2
        self.image2_label.grid(column=1,row=1)
         
        self.label3=Label(self.frame4,font=("Little Comet Bubling Demo Version",11),bg="white",justify="left")
        self.label3.grid(column=0,row=1)
        
        self.image3_label=Label(self.frame4,image=image3)
        self.image3_label.image=image3
        self.image3_label.grid(column=0,row=2)
         
        self.label4=Label(self.frame4,font=("Little Comet Bubling Demo Version",11),bg="white",justify="left")
        self.label4.grid(column=1,row=2)
        
        self.image4_label=Label(self.frame4,image=image4)
        self.image4_label.image=image4
        self.image4_label.grid(column=1,row=3)
        
        self.label5=Label(self.frame4,font=("Little Comet Bubling Demo Version",11),bg="white",justify="left")
        self.label5.grid(column=0,row=3)
        
        self.image5_label=Label(self.frame4,image=image5)
        self.image5_label.image=image5
        self.image5_label.grid(column=0,row=4)
        
        self.label6=Label(self.frame4,font=("Little Comet Bubling Demo Version",11),bg="white",justify="left")
        self.label6.grid(column=1,row=4)
        
        self.canva1.bind('<Configure>', lambda e: self.canva1.configure(scrollregion=self.canva1.bbox("all")))
        
        self.label1=Label(self,text="Piramide Alimenticia",font=("Little Comet Bubling Demo Version",28),bg="white",justify="left")
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
        self.configure_text()

    def configure_text(self):
        self.controller.configure_text()

    def back_to_Menu4(self):
        self.controller.back_to_Menu4()