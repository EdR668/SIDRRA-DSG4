from tkinter import *

class Menu5(Frame):
    def __init__(self, inicio):
        inicio.geometry("600x690")
        super().__init__(inicio)
        
        self.string1=("Sidrra es un proyecto relacionado con Estructura de Datos , desarollado por:\n \n-Anderson Morales \n-Eder Jose Hernadez Buelvas \n-David Rodriguez \nLos cuales fuimos acompañados y dirigidos por el profesor Jhon Lopez Fajardo")

        self.string2=("El objetivo de del proyecto es ayudar a disminuir los residuios alimenticios junto a mejorar la salud con los habitos alimenticios  por medio de la distribución del banco de alimentos, cosas cuales se encuentran en los objetivos del buen vivir")
        self.string2+=(", todo esto atrvez de la programacion orientada a objetos .")

        self.string3=("Las metodologias usadas para esto , son : el uso de Visual Studio Code como editor , el uso de Python como el lenguaje en el cual esta escrito el programa , el uso de tkinter como libreria para el dessarrollo de la interfaz grafica")
        self.string3+=(", y el uso de variados conceptos de la Programacion de Estructura de datos tales como el colas, pilas y nodos en esta primera entrega.")

        self.string4=("Para generar un caso de prueba, se instanciaron una serie de 80 objetos de cada una de las clases para definir una situación de prueba simulando una comunidad de clientes del banco de alimentos.")
        self.string4+=("Al hacer la situación, se lograron demostrar los siguientes aspectos:")
        self.string4+=("En un contexto local que se puede considerar de mediana escala, se lograron satisfacer las necesidades individuales de todos los individuos , en cuanto al manejo de residuos, se logró generar una disminución en el uso de recursos alimenticios al mejorar la administración de los mismos; permitiendo la reducción de los residuos.")

        back=PhotoImage(file='Images\\Botones\\botonVolver.png')
        top1=PhotoImage(file="Images\\Otras\\top1.png")
        under1=PhotoImage(file="Images\\Otras\\under1.png")

        self.place(x=0,y=0)
        self.config(bg="white",width=600,height=690)

        self.label1=Label(self,text="Informacion",font=("Little Comet Bubling Demo Version",28),bg="white",justify="left")
        self.label1.place(x=20,y=20) 
            
        self.label2=Label(self,text=self.string1,font=("Little Comet Bubling Demo Version",12),bg="white",justify="left")
        self.label2.place(x=20,y=70)
        
        self.label3=Label(self,font=("Little Comet Bubling Demo Version",12),bg="white",justify="left")
        self.label3.place(x=20,y=180)
        
        self.label4=Label(self,font=("Little Comet Bubling Demo Version",12),bg="white",justify="left")
        self.label4.place(x=20,y=240)

        self.label5=Label(self,font=("Little Comet Bubling Demo Version",12),bg="white",justify="left")
        self.label5.place(x=20,y=330)
        
        self.buttonB=Button(self,image=back,borderwidth=0,command=self.back_to_Menu1)
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

    def back_to_Menu1(self):
        self.controller.back_to_Menu1()

    def configure_text(self):
        self.controller.configure_text()