from ast import And
from cProfile import label
from ctypes import alignment
from email.mime import image
from re import M
from tkinter import *
from tkinter import font
from turtle import bgcolor, left, width
import PIL.Image
import PIL.ImageTk
from Comida import *
from Lacteos import *
from VerdurasYFtutas import *
from receta import *
from funcionesN import *
from funcionesGui import *
from EstructurasLineales import pila
from EstructurasLineales import cola
inicio =Tk()
def menu5():
    inicio.geometry("600x690")
    frame3=Frame(inicio,bg='white')
    frame3.place(x=0,y=0,width=600,height=690)

    label1=Label(frame3,text="Informacion",font=("Little Comet Bubling Demo Version",28),bg="white",justify="left")
    label1.place(x=20,y=20)

    string1=("Sidrra es un proyecto relacionado con Estructura de Datos , desarollado por:\n \n-Anderson Morales \n-Eder Jose Hernadez Buelvas \n-David Rodriguez \nLos cuales fuimos acompañados y dirigidos por el profesor Jhon Lopez Fajardo")
    label2=Label(frame3,text=string1,font=("Little Comet Bubling Demo Version",12),bg="white",justify="left")
    label2.place(x=20,y=70)

    def returnmenu4():
        menu1()

    string2=("El objetivo de del proyecto es ayudar a disminuir los residuios alimenticios junto a mejorar la salud con los habitos alimenticios  por medio de la distribución del banco de alimentos, cosas cuales se encuentran en los objetivos del buen vivir")
    string2+=(", todo esto atrvez de la programacion orientada a objetos .")

    label3=Label(frame3,text=arreglaString(string2,90),font=("Little Comet Bubling Demo Version",12),bg="white",justify="left")
    label3.place(x=20,y=180)

    string3=("Las metodologias usadas para esto , son : el uso de Visual Studio Code como editor , el uso de Python como el lenguaje en el cual esta escrito el programa , el uso de tkinter como libreria para el dessarrollo de la interfaz grafica")
    string3+=(", y el uso de variados conceptos de la Programacion de Estructura de datos tales como el colas, pilas y nodos en esta primera entrega.")

    label4=Label(frame3,text=arreglaString(string3,90),font=("Little Comet Bubling Demo Version",12),bg="white",justify="left")
    label4.place(x=20,y=240)

    string4=("Para generar un caso de prueba, se instanciaron una serie de 80 objetos de cada una de las clases para definir una situación de prueba simulando una comunidad de clientes del banco de alimentos.")
    string4+=("Al hacer la situación, se lograron demostrar los siguientes aspectos:")
    string4+=("En un contexto local que se puede considerar de mediana escala, se lograron satisfacer las necesidades individuales de todos los individuos , en cuanto al manejo de residuos, se logró generar una disminución en el uso de recursos alimenticios al mejorar la administración de los mismos; permitiendo la reducción de los residuos.")

    label5=Label(frame3,text=arreglaString(string4,90),font=("Little Comet Bubling Demo Version",12),bg="white",justify="left")
    label5.place(x=20,y=330)

    back=PhotoImage(file='botonVolver.png')
    buttonB=Button(frame3,command=returnmenu4,image=back,borderwidth=0)
    buttonB.image=back
    buttonB.place(x=480,y=25)

    top1=PhotoImage(file="top1.png")
    top1_label=Label(image=top1)
    top1_label.image=top1
    top1_label.place(x=0,y=-15)

    under1=PhotoImage(file="under1.png")
    under1_label=Label(image=under1)
    under1_label.image=under1
    under1_label.place(x=0,y=670)

    frame3.mainloop()

def menu4():
    inicio.geometry("600x690")
    frame2=Frame(inicio,bg='white')
    frame2.place(x=0,y=0,width=600,height=690)

    label1=Label(frame2,text="Utilidades",font=("Little Comet Bubling Demo Version",32),bg="white")
    label1.place(x=220,y=40)
    string1="Acontinuacion se mostraran cuatro opciones las cuales aportaran \nal usuario mayor informacion , herramientas  y soluciones ,\ncon los cuales se podra faciliar una reducion casi al minimo de \nlos desperdicios alimenticios "
    label2=Label(frame2,text=string1,font=("Little Comet Bubling Demo Version",16),bg="white",justify="left")
    label2.place(x=30,y=90)

    def menu4_1():
        inicio.geometry("600x690")
        frame3=Frame(inicio,bg='white')
        frame3.place(x=0,y=0,width=600,height=690)
        my_scrollbar1=Scrollbar(frame3,orient=VERTICAL)

        canva1=Canvas(frame3,width=575,height=600,bg="white",yscrollcommand=my_scrollbar1.set)

        my_scrollbar1.config(command=canva1.yview)
        my_scrollbar1.place(x=580,y=70,height=600)

        frame4=Frame(canva1,bg="white")
        frame4.grid(columnspan=4,rowspan=5)
        canva1.place(x=0,y=70)
        canva1.create_window((0,0),window=frame4,anchor="nw")

        image1=PhotoImage(file="dietasana.png")
        image1_label=Label(frame4,image=image1)
        image1_label.image=image1
        image1_label.grid(column=0,row=0)

        label2=Label(frame4,font=("Little Comet Bubling Demo Version",11),bg="white",text="Para llevar una dieta y una vida saludable no \nes necesario ser excesivos ni extremistas ,\nbasta mayormente con ciertos habitos \ny practicas muy basicas",justify="left")
        label2.grid(column=1,row=0)

        image2=PhotoImage(file="piramide.png")
        image2_label=Label(frame4,image=image2)
        image2_label.image=image2
        image2_label.grid(column=1,row=1)
        string2="Primera mente partamos por recordar la piramide alimenticia la cual esta dividia en 5 niveles , el nivel mas bajo contiene a las harinas , cereales , patatas y legumbres, el nivel 4 contiene a las frutas y verduras , el nivel 3"
        string2+="contiene los lacteos ,a los huevos junto a las carnes blancas y magras el 2 escalon contiene a las carnes rojas procesados y embutidos , y finalmenete el primer nivel contien a los dulces , chucherias y untables"
        label3=Label(frame4,font=("Little Comet Bubling Demo Version",11),bg="white",text=arreglaString(string2,45),justify="left")
        label3.grid(column=0,row=1)

        image3=PhotoImage(file="porciones.png")
        image3_label=Label(frame4,image=image3)
        image3_label.image=image3
        image3_label.grid(column=0,row=2)
        string3="La piramide alimenticia nos permite delimitar las diferentes clases de alimentos , esto nos ayuda bastante ya que podemos trazar un plan alimentcio basado en porciones y  escalas de la piramide nutricional"
        string3+=", por lo tanto una dieta saludable debe constar de : 3 porciones diarias entre harina y cereales , 6-7 porciones diarias entre frutas y verduras , 1-2 porciones diarias de lacteos , 3-5 raciones entre carne blanca, pescado y huevos a la semana , y esporadicamente una racion de carne roja"
        label4=Label(frame4,font=("Little Comet Bubling Demo Version",11),bg="white",text=arreglaString(string3,40),justify="left")
        label4.grid(column=1,row=2)

        image4=PhotoImage(file="cuantaAgua.png")
        image4_label=Label(frame4,image=image4)
        image4_label.image=image4
        image4_label.grid(column=1,row=3)
        string4="Aproximadamente 60 porciento del peso corporal es agua , y cada uno de los sistemas humanos depende de ella , por lo qu estar bien hidratado es un es un factor muy importante en cuanto se trata a la salud"
        string4+=", aunque la cantidad de agua necesaria por persona varia por varios factores se recomienda que los hombres tomen alrededor de 13 taza y en el caso de las mujeres seria de 9 tazas "
        label5=Label(frame4,font=("Little Comet Bubling Demo Version",11),bg="white",text=arreglaString(string4,40),justify="left")
        label5.grid(column=0,row=3)

        image5=PhotoImage(file="ejercicio.png")
        image5_label=Label(frame4,image=image5)
        image5_label.image=image5
        image5_label.grid(column=0,row=4)
        string5="Para mantener una dieta y cuerpo sano hay que realizar cierta actividad fisica tanto los hombres como las mujeres , lo mas recomendado es realizar al menos 150 minutos de actividad aerobica"
        string5+="moderada o 75 de actividad intensa , a su vez se deberian realizar al menos dos seciones de fortalezimiento muscular a la semana para los grupos musculares principales"
        label6=Label(frame4,font=("Little Comet Bubling Demo Version",11),bg="white",text=arreglaString(string5,40),justify="left")
        label6.grid(column=1,row=4)

        frame2.update()
        canva1.config(scrollregion=canva1.bbox("all"))


        def returnmenu4():
            menu4()

        label1=Label(frame3,text="Piramide Alimenticia",font=("Little Comet Bubling Demo Version",28),bg="white",justify="left")
        label1.place(x=20,y=20)

        back=PhotoImage(file='botonVolver.png')
        buttonB=Button(frame3,command=returnmenu4,image=back,borderwidth=0)
        buttonB.image=back
        buttonB.place(x=480,y=25)

        top1=PhotoImage(file="top1.png")
        top1_label=Label(image=top1)
        top1_label.image=top1
        top1_label.place(x=0,y=-15)

        under1=PhotoImage(file="under1.png")
        under1_label=Label(image=under1)
        under1_label.image=under1
        under1_label.place(x=0,y=670)

    def menu4_2():
        inicio.geometry("600x690")
        frame3=Frame(inicio,bg='white')
        frame3.place(x=0,y=0,width=600,height=690)

        label1=Label(frame3,text="Calculadora de calorias",font=("Little Comet Bubling Demo Version",28),bg="white",justify="left")
        label1.place(x=20,y=20)

        label2=Label(frame3,text="Acontinuacion se le pedira al usuario que ingrese ciertos datos para \npoder calcular la cantidad de calorias aproximada que necesita diariamente",font=("Little Comet Bubling Demo Version",12),bg="white",justify="left")
        label2.place(x=20,y=390)

        selecion=Listbox(frame3,width=15,height=2,font=("Little Comet Bubling Demo Version",14))
        selecion.place(x=215,y=480)
        selecion.insert(END,"Hombre")
        selecion.insert(END,"Mujer")

        label3=Label(frame3,text="Por favor ingrese su sexo",font=("Little Comet Bubling Demo Version",11),bg="white",justify="left")
        label3.place(x=215,y=440)

        number4=Entry(frame3,width=20,font=("Little Comet Bubling Demo Version",12))
        number4.place(x=355,y=510)
        number4.insert(0,"numero del 0 al 14")

        label4=Label(frame3,text="Por favor ingrese la cantidad de veces \nque hace ejercicio a la semana con un \nnumero entre 0 y 14",font=("Little Comet Bubling Demo Version",11),bg="white",justify="left")
        label4.place(x=355,y=440)

        number1=Entry(frame3,width=25,font=("Little Comet Bubling Demo Version",12))
        number1.place(x=20,y=450)
        number1.insert(0,"Ingrese su peso en kg")

        number2=Entry(frame3,width=25,font=("Little Comet Bubling Demo Version",12))
        number2.place(x=20,y=500)
        number2.insert(0,"Ingrese su edad en años")

        number3=Entry(frame3,width=25,font=("Little Comet Bubling Demo Version",12))
        number3.place(x=20,y=550)
        number3.insert(0,"Ingrese su estatura en cm")



        def selectall():
            numeroCal=0
            string1=selecion.get(ANCHOR)
            int1=int(number4.get())
            float1=0.0
            if(int1==0):
                float1=1.2
            if(int1>1 and int1<4):
                float1=1.38
            if(int1>3 and int1<6):
                float1=1.55
            if(int1>5 and int1<8):
                float1=1.73
            if(int1>7):
                float1=1.90
            string2="Las calorias necesarias aproximadas segun \nlos datos del usuario son : "
            if string1=="Hombre":
                numeroCal=(655+9*(int(number1.get())))+(1*int(number3.get()))-(4*int(number2.get()))
                numero2=int(numeroCal*float1)
                string2+=str(numero2)
            if string1=="Mujer":
                numeroCal=(66+13*(int(number1.get())))+(5*int(number3.get()))-(6*int(number2.get()))
                numero2=int(numeroCal*float1)
                string2+=str(numero2)
            print(numeroCal)
            print(string1)
            print(float1)
            label4.config(text=string2)

        firtsbutton=PhotoImage(file='boton1Menu2.png')
        button1=Button(frame3,image=firtsbutton,command=selectall,borderwidth=0)
        button1.image=firtsbutton
        button1.place(x=20,y=580)

        label4=Label(frame3,text="Las calorias necesarias aproximadas segun \nlos datos del usuario son : ",font=("Little Comet Bubling Demo Version",12),bg="white",justify="left")
        label4.place(x=180,y=580)



        image1=PhotoImage(file="preguntacalorias.png")
        image1_label=Label(frame3,image=image1)
        image1_label.image=image1
        image1_label.place(x=20,y=80)

        def returnmenu4():
            menu4()

        back=PhotoImage(file='botonVolver.png')
        buttonB=Button(frame3,command=returnmenu4,image=back,borderwidth=0)
        buttonB.image=back
        buttonB.place(x=480,y=25)

        top1=PhotoImage(file="top1.png")
        top1_label=Label(image=top1)
        top1_label.image=top1
        top1_label.place(x=0,y=-15)

        under1=PhotoImage(file="under1.png")
        under1_label=Label(image=under1)
        under1_label.image=under1
        under1_label.place(x=0,y=670)

        frame3.mainloop()

    def menu4_3():
        string1=""


    def menu4_4():
        inicio.geometry("600x690")
        frame3=Frame(inicio,bg='white')
        frame3.place(x=0,y=0,width=600,height=690)
        my_scrollbar1=Scrollbar(frame3,orient=VERTICAL)

        canva1=Canvas(frame3,width=575,height=600,bg="white",yscrollcommand=my_scrollbar1.set)

        my_scrollbar1.config(command=canva1.yview)
        my_scrollbar1.place(x=580,y=70,height=600)

        frame4=Frame(canva1,bg="white")
        frame4.grid(columnspan=3,rowspan=12)
        canva1.place(x=0,y=70)
        canva1.create_window((0,0),window=frame4,anchor="nw")

        label2=Label(frame4,font=("Little Comet Bubling Demo Version",11),bg="white",text="Acontinuacion se mostraran los mejores tips o maneras para reutilizar la comida",justify="left")
        label2.grid(column=1,row=0)

        food1=PhotoImage(file="reducion1.png")
        food1_label=Label(frame4,image=food1)
        food1_label.image=food1
        food1_label.grid(column=1,row=1)

        food2=PhotoImage(file="reducion2.png")
        food2_label=Label(frame4,image=food2)
        food2_label.image=food2
        food2_label.grid(column=1,row=2)

        food3=PhotoImage(file="reducion3.png")
        food3_label=Label(frame4,image=food3)
        food3_label.image=food3
        food3_label.grid(column=1,row=3)

        food4=PhotoImage(file="reducion4.png")
        food4_label=Label(frame4,image=food4)
        food4_label.image=food4
        food4_label.grid(column=1,row=4)

        food5=PhotoImage(file="reducion5.png")
        food5_label=Label(frame4,image=food5)
        food5_label.image=food5
        food5_label.grid(column=1,row=5)

        food6=PhotoImage(file="reducion6.png")
        food6_label=Label(frame4,image=food6)
        food6_label.image=food6
        food6_label.grid(column=1,row=6)

        food7=PhotoImage(file="reducion7.png")
        food7_label=Label(frame4,image=food7)
        food7_label.image=food7
        food7_label.grid(column=1,row=7)

        food8=PhotoImage(file="reducion8.png")
        food8_label=Label(frame4,image=food8)
        food8_label.image=food8
        food8_label.grid(column=1,row=8)

        frame2.update()
        canva1.config(scrollregion=canva1.bbox("all"))


        def returnmenu4():
            menu4()

        label1=Label(frame3,text="Reutilizacion de residuos",font=("Little Comet Bubling Demo Version",28),bg="white",justify="left")
        label1.place(x=20,y=20)

        back=PhotoImage(file='botonVolver.png')
        buttonB=Button(frame3,command=returnmenu4,image=back,borderwidth=0)
        buttonB.image=back
        buttonB.place(x=480,y=25)

        top1=PhotoImage(file="top1.png")
        top1_label=Label(image=top1)
        top1_label.image=top1
        top1_label.place(x=0,y=-15)

        under1=PhotoImage(file="under1.png")
        under1_label=Label(image=under1)
        under1_label.image=under1
        under1_label.place(x=0,y=670)

    def returnmenu1():
        menu1()
    back=PhotoImage(file='botonVolver.png')
    button6=Button(frame2,command=returnmenu1,image=back,borderwidth=0)
    button6.image=back
    button6.place(x=480,y=25)

    cat1=PhotoImage(file="elegirOpcion.png")
    cat1_label=Label(image=cat1)
    cat1_label.image=cat1
    cat1_label.place(x=80,y=220)

    firtsbutton=PhotoImage(file='boton1Menu4.png')
    button1=Button(frame2,image=firtsbutton,command=menu4_1,borderwidth=0)
    button1.image=firtsbutton
    button1.place(x=60,y=490)

    secondbutton=PhotoImage(file='boton2Menu4.png')
    button2=Button(frame2,image=secondbutton,command=menu4_3,borderwidth=0)
    button2.image=secondbutton
    button2.place(x=60,y=570)

    thirdbutton=PhotoImage(file='boton3Menu4.png')
    button3=Button(frame2,image=thirdbutton,command=menu4_2,borderwidth=0)
    button3.image=thirdbutton
    button3.place(x=350,y=490)

    fourthbutton=PhotoImage(file='boton4Menu4.png')
    button4=Button(inicio,image=fourthbutton,command=menu4_4,borderwidth=0)
    button4.image=fourthbutton
    button4.place(x=350,y=570)

    top1=PhotoImage(file="top1.png")
    top1_label=Label(image=top1)
    top1_label.image=top1
    top1_label.place(x=0,y=-15)

    under1=PhotoImage(file="under1.png")
    under1_label=Label(image=under1)
    under1_label.image=under1
    under1_label.place(x=0,y=670)

def menu3():
    inicio.geometry("600x690")
    frame2=Frame(inicio,bg='white')
    frame2.place(x=0,y=0,width=600,height=690)
    my_scrollbar=Scrollbar(frame2,orient=VERTICAL)

    label2=Label(frame2,text="Acontinuacion se mostrara la lista de todos las recetas ",font=("Little Comet Bubling Demo Version",14),bg="white")
    label2.place(x=20,y=20)

    selecion=Listbox(frame2,width=30,yscrollcommand=my_scrollbar.set,height=10,selectmode=MULTIPLE,font=("Little Comet Bubling Demo Version",14))
    selecion.place(x=300,y=70)
    selecion_opciones=prepareElementsforboxRecetas()
    lista_aux=pila()

    my_scrollbar.config(command=selecion.yview)
    my_scrollbar.place(x=542,y=70,height=224)

    label1=Label(inicio, text='Las recetas selecionadas son : ',font=("Little Comet Bubling Demo Version",14),bg="white")
    label1.place(x=25,y=325)

    for item in selecion_opciones:
        selecion.insert(END,item)

    def selectall():
        for i in selecion.curselection():
            lista_aux.stack(selecion.get(i))
        label1.config(text=(sayElementsSelectedReceta(lista_aux)))
    def deleteall():

        lista_aux.pop()
        label1.config(text=(sayElementsSelectedReceta(lista_aux)))
    def menu3_1():
        inicio.geometry("600x690")
        frame3=Frame(inicio,bg='white')
        frame3.place(x=0,y=0,width=600,height=690)
        my_scrollbar1=Scrollbar(frame3,orient=VERTICAL)

        canva1=Canvas(frame3,width=580,height=600,bg="white",yscrollcommand=my_scrollbar1.set)

        my_scrollbar1.config(command=canva1.yview)
        my_scrollbar1.place(x=580,y=70,height=600)

        frame4=Frame(canva1)
        canva1.place(x=0,y=70)
        canva1.create_window((0,0),window=frame4,anchor="nw")

        label2=Label(frame4,font=("Little Comet Bubling Demo Version",11),bg="white",text="",justify="left")
        label2.config(text=mostrarDescripcionRecetas(lista_aux))
        label2.pack()

        frame2.update()
        canva1.config(scrollregion=canva1.bbox("all"))
        top1=PhotoImage(file="top1.png")
        top1_label=Label(image=top1)
        top1_label.image=top1
        top1_label.place(x=0,y=-15)

        def returnmenu3():
            menu3()

        label1=Label(frame3,text="Acontinuacion se mostrara la lista de las recetas \ndisponibles con los ingredientes selecionados ",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
        label1.place(x=20,y=20)

        back=PhotoImage(file='botonVolver.png')
        buttonB=Button(frame3,command=returnmenu3,image=back,borderwidth=0)
        buttonB.image=back
        buttonB.place(x=440,y=20)

        under1=PhotoImage(file="under1.png")
        under1_label=Label(image=under1)
        under1_label.image=under1
        under1_label.place(x=0,y=670)

    def menu3_2():
        inicio.geometry("600x690")
        frame3=Frame(inicio,bg='white')
        frame3.place(x=0,y=0,width=600,height=690)
        my_scrollbar1=Scrollbar(frame3,orient=VERTICAL)

        canva1=Canvas(frame3,width=580,height=600,bg="white",yscrollcommand=my_scrollbar1.set)

        my_scrollbar1.config(command=canva1.yview)
        my_scrollbar1.place(x=580,y=70,height=600)

        frame4=Frame(canva1)
        canva1.place(x=0,y=70)
        canva1.create_window((0,0),window=frame4,anchor="nw")

        label2=Label(frame4,font=("Little Comet Bubling Demo Version",11),bg="white",text="",justify="left")
        label2.config(text=mostrarDescripcionRecetasIngredientes(lista_aux))
        label2.pack()

        frame2.update()
        canva1.config(scrollregion=canva1.bbox("all"))
        top1=PhotoImage(file="top1.png")
        top1_label=Label(image=top1)
        top1_label.image=top1
        top1_label.place(x=0,y=-15)

        def returnmenu3():
            menu3()

        label1=Label(frame3,text="Acontinuacion se mostrara los detalles de \nlos ingredientes de las recetas selecionadas",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
        label1.place(x=20,y=20)

        back=PhotoImage(file='botonVolver.png')
        buttonB=Button(frame3,command=returnmenu3,image=back,borderwidth=0)
        buttonB.image=back
        buttonB.place(x=440,y=20)

        under1=PhotoImage(file="under1.png")
        under1_label=Label(image=under1)
        under1_label.image=under1
        under1_label.place(x=0,y=670)


    firtsbutton=PhotoImage(file='boton1Menu2.png')
    button1=Button(frame2,image=firtsbutton,command=selectall,borderwidth=0)
    button1.image=firtsbutton
    button1.place(x=50,y=120)

    secondbutton=PhotoImage(file='boton2Menu2.png')
    button2=Button(frame2,image=secondbutton,command=deleteall,borderwidth=0)
    button2.image=secondbutton
    button2.place(x=50,y=200)

    thirdbutton=PhotoImage(file='boton1Menu3.png')
    button3=Button(frame2,image=thirdbutton,command=menu3_1,borderwidth=0)
    button3.image=thirdbutton
    button3.place(x=360,y=490)

    fourthbutton=PhotoImage(file='boton2Menu3.png')
    button4=Button(inicio,image=fourthbutton,command=menu3_2,borderwidth=0)
    button4.image=fourthbutton
    button4.place(x=360,y=570)

    def returnmenu1():
        menu1()
    back=PhotoImage(file='botonVolver.png')
    button6=Button(frame2,command=returnmenu1,image=back,borderwidth=0)
    button6.image=back
    button6.place(x=450,y=20)

    top1=PhotoImage(file="top1.png")
    top1_label=Label(image=top1)
    top1_label.image=top1
    top1_label.place(x=0,y=-15)

    cat1=PhotoImage(file="queIngredientes.png")
    cat1_label=Label(image=cat1)
    cat1_label.image=cat1
    cat1_label.place(x=20,y=450)

    under1=PhotoImage(file="under1.png")
    under1_label=Label(image=under1)
    under1_label.image=under1
    under1_label.place(x=0,y=670)

    inicio.mainloop()

def menu2():
    inicio.geometry("600x690")
    frame2=Frame(inicio,bg='white')
    frame2.place(x=0,y=0,width=600,height=690)
    my_scrollbar=Scrollbar(frame2,orient=VERTICAL)

    label2=Label(frame2,text="Acontinuacion se mostrara la lista de todos los ingredintes ",font=("Little Comet Bubling Demo Version",14),bg="white")
    label2.place(x=20,y=20)

    selecion=Listbox(frame2,width=30,yscrollcommand=my_scrollbar.set,height=10,selectmode=MULTIPLE,font=("Little Comet Bubling Demo Version",14))
    selecion.place(x=25,y=70)
    selecion_opciones=prepareElementsforboxIngredientes()
    lista_aux=cola()

    my_scrollbar.config(command=selecion.yview)
    my_scrollbar.place(x=268,y=70,height=224)

    label1=Label(inicio, text='Los ingredientes selecionados son : ',font=("Little Comet Bubling Demo Version",14),bg="white")
    label1.place(x=25,y=325)

    for item in selecion_opciones:
        selecion.insert(END,item)

    def selectall():
        for i in selecion.curselection():
            lista_aux.queue(selecion.get(i))

        label1.config(text=(sayElementsSelectedIngrediente(lista_aux)))
    def deleteall():
        for i in range(lista_aux.longitud):
            lista_aux.dequeue()
        label1.config(text=(sayElementsSelectedIngrediente(lista_aux)))
    def menu2_1():
        inicio.geometry("600x690")
        frame3=Frame(inicio,bg='white')
        frame3.place(x=0,y=0,width=600,height=690)
        my_scrollbar1=Scrollbar(frame3,orient=VERTICAL)

        canva1=Canvas(frame3,width=580,height=600,bg="white",yscrollcommand=my_scrollbar1.set)

        my_scrollbar1.config(command=canva1.yview)
        my_scrollbar1.place(x=580,y=70,height=600)

        frame4=Frame(canva1)
        canva1.place(x=0,y=70)
        canva1.create_window((0,0),window=frame4,anchor="nw")

        label2=Label(frame4,font=("Little Comet Bubling Demo Version",11),bg="white",text="",justify="left")
        label2.config(text=showBestRecipes(lista_aux))
        label2.pack()

        frame2.update()
        canva1.config(scrollregion=canva1.bbox("all"))
        top1=PhotoImage(file="top1.png")
        top1_label=Label(image=top1)
        top1_label.image=top1
        top1_label.place(x=0,y=-15)

        def returnmenu2():
            menu2()

        label1=Label(frame3,text="Acontinuacion se mostrara la lista de las recetas \ndisponibles con los ingredientes selecionados ",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
        label1.place(x=20,y=20)

        back=PhotoImage(file='botonVolver.png')
        buttonB=Button(frame3,command=returnmenu2,image=back,borderwidth=0)
        buttonB.image=back
        buttonB.place(x=440,y=20)

        under1=PhotoImage(file="under1.png")
        under1_label=Label(image=under1)
        under1_label.image=under1
        under1_label.place(x=0,y=670)

    def menu2_2():
        inicio.geometry("600x690")
        frame3=Frame(inicio,bg='white')
        frame3.place(x=0,y=0,width=600,height=690)
        my_scrollbar1=Scrollbar(frame3,orient=VERTICAL)

        canva1=Canvas(frame3,width=580,height=600,bg="white",yscrollcommand=my_scrollbar1.set)

        my_scrollbar1.config(command=canva1.yview)
        my_scrollbar1.place(x=580,y=70,height=600)

        frame4=Frame(canva1,bg="white")
        canva1.place(x=0,y=70)
        canva1.create_window((0,0),window=frame4,anchor="nw")

        label2=Label(frame4,font=("Little Comet Bubling Demo Version",11),bg="white",text="",justify="left")
        label2.config(text=mostrarDescripcionIngredientes(lista_aux))
        label2.pack()


        frame2.update()
        canva1.config(scrollregion=canva1.bbox("all"))
        top1=PhotoImage(file="top1.png")
        top1_label=Label(image=top1)
        top1_label.image=top1
        top1_label.place(x=0,y=-15)

        def returnmenu2():
            menu2()

        label1=Label(frame3,text="Acontinuacion se mostrara los detalles de \nlos ingredientes selecionados ",font=("Little Comet Bubling Demo Version",14),bg="white",justify="left")
        label1.place(x=20,y=20)

        back=PhotoImage(file='botonVolver.png')
        buttonB=Button(frame3,command=returnmenu2,image=back,borderwidth=0)
        buttonB.image=back
        buttonB.place(x=440,y=20)

        under1=PhotoImage(file="under1.png")
        under1_label=Label(image=under1)
        under1_label.image=under1
        under1_label.place(x=0,y=670)


    firtsbutton=PhotoImage(file='boton1Menu2.png')
    button1=Button(frame2,image=firtsbutton,command=selectall,borderwidth=0)
    button1.image=firtsbutton
    button1.place(x=400,y=120)
    secondbutton=PhotoImage(file='boton2Menu2.png')
    button2=Button(frame2,image=secondbutton,command=deleteall,borderwidth=0)
    button2.image=secondbutton
    button2.place(x=400,y=200)

    thirdbutton=PhotoImage(file='boton3Menu2.png')
    button3=Button(frame2,image=thirdbutton,command=menu2_1,borderwidth=0)
    button3.image=thirdbutton
    button3.place(x=360,y=490)

    fourthbutton=PhotoImage(file='boton4Menu2.png')
    button4=Button(inicio,image=fourthbutton,command=menu2_2,borderwidth=0)
    button4.image=fourthbutton
    button4.place(x=360,y=570)

    def returnmenu1():
        menu1()
    back=PhotoImage(file='botonVolver.png')
    button6=Button(frame2,command=returnmenu1,image=back,borderwidth=0)
    button6.image=back
    button6.place(x=450,y=20)

    top1=PhotoImage(file="top1.png")
    top1_label=Label(image=top1)
    top1_label.image=top1
    top1_label.place(x=0,y=-15)

    cat1=PhotoImage(file="gatoPregunta1.png")
    cat1_label=Label(image=cat1)
    cat1_label.image=cat1
    cat1_label.place(x=20,y=450)

    under1=PhotoImage(file="under1.png")
    under1_label=Label(image=under1)
    under1_label.image=under1
    under1_label.place(x=0,y=670)

    inicio.mainloop()

def menu1():
    inicio.geometry("445x690")
    frame1=Frame(bg="white")
    frame1.place(x=0,y=0,width=445,height=690)

    img=PhotoImage(file="Fondo2.png")
    img_label=Label(image=img)
    img_label.image= img
    img_label.place(x=0,y=-10)



    firtsbutton=PhotoImage(file='boton1.png')
    button1=Button(inicio,image=firtsbutton,command=menu2,borderwidth=0)
    button1.image=firtsbutton
    button1.place(x=113,y=305)

    secondbutton=PhotoImage(file='boton2.png')
    button2=Button(inicio,image=secondbutton,command=menu3,borderwidth=0)
    button2.image=secondbutton
    button2.place(x=113,y=402)

    thirdbutton=PhotoImage(file='boton3.png')
    button3=Button(inicio,image=thirdbutton,command=menu4,borderwidth=0)
    button3.image=thirdbutton
    button3.place(x=113,y=502)

    fourthbutton=PhotoImage(file='boton4.png')
    button4=Button(inicio,image=fourthbutton,command=menu5,borderwidth=0)
    button4.image=fourthbutton
    button4.place(x=112,y=592)
    zero=PhotoImage(file="banco3.png")
    zero_label=Label(image=zero)
    zero_label.image=zero
    zero_label.place(x=320,y=100,width=120,height=120)

menu1()

inicio.mainloop()
