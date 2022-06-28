from tkinter import *
from tkinter import filedialog
from View.Menu1 import Menu1
from Model.Entidades.Organico import Organico
from Model.Entidades.Inorganico import Inorganico
from Model.Images import save_image
from Model.DB import insert_alimento, organicos_colletion, inorganicos_collection

class ControlIngresarAlimentos:
    def __init__(self, model, view, wd, other_control):
        self.model = model
        self.view = view
        self.wd = wd
        self.other_control = other_control
        self.var_caducidad = StringVar()
        self.var_day = StringVar()
        self.var_month = StringVar()
        self.var_year = StringVar()
        self.var_cant = StringVar()
        self.imagen = None

    def back_to_Menu1(self):
        self.wd.switch_frame(Menu1,self.other_control)

    def obtain_data(self):
        selection = self.view.comb_box.get()

        nombre = self.view.var_nombre.get()
        tipo = self.view.var_tipo.get()
        uso = self.view.text_uso.get(1.0,"end-1c")
        caract = self.view.text_caracteristicas.get(1.0,"end-1c")
        props = self.view.text_props.get(1.0,"end-1c")
        cant = self.var_cant.get()

        if selection == "Organico":
            caducidad = self.var_caducidad.get()
            if self.confirm(cant=cant,nombre=nombre,tipo=tipo,comb=selection,caducidad=caducidad):
                new_food = Organico(cant,nombre,tipo,uso,caract,props,save_image(self.imagen[0]),caducidad)
                insert_alimento(organicos_colletion,new_food)
                self.blank_fields()
                self.var_caducidad.set("")

        elif selection == "No organico":
            day = self.var_day.get()
            month = self.var_month.get()
            year = self.var_year.get()
            if self.confirm(cant=cant,nombre=nombre,tipo=tipo,comb=selection,day=day,month=month,year=year):
                n_food = Inorganico(cant, nombre, tipo, uso, caract, props, save_image(self.imagen[0]), str(day)+"/"+str(month)+"/"+str(year))
                insert_alimento(inorganicos_collection, n_food)
                self.blank_fields()
                self.var_day.set("")
                self.var_month.set("")
                self.var_year.set("")
    
    def blank_fields(self):
        self.view.var_nombre.set("")
        self.view.var_tipo.set("")
        self.var_cant.set("")
        self.view.text_uso.delete(1.0,"end")
        self.view.text_caracteristicas.delete(1.0,"end")
        self.view.text_props.delete(1.0,"end")
        self.imagen = None
        self.view.label_image.delete(1.0,"end")

    def confirm(self, nombre, tipo, comb, cant, caducidad=None, day=None, month=None, year=None):
        if comb == "Organico":
            return nombre != "" and tipo != "" and caducidad != "" and self.imagen != None and cant != ""
        elif comb == "No organico":
            return nombre != "" and tipo != "" and day != "" and month != "" and year != "" and self.imagen != None and cant != ""
        else:
            return False

    def comb_change(self, event):
        selection = self.view.comb_box.get()

        if selection == "Organico":
            try:
                self.destroy_not_organic_gui()
            except AttributeError:
                pass
            self.organic_gui()
        else:
            try:
                self.destroy_organic_gui()
            except AttributeError:
                pass
            self.not_organic_gui()

    def organic_gui(self):
        self.view.label_caducidad.config(text="Ingrese el tiempo de caducidad en días:")
        self.view.label_cant.config(text="Ingrese la cantidad del alimento en gramos:")

        self.entry_caducidad = Entry(self.view,textvariable=self.var_caducidad,validate='key',validatecommand=(self.view.register(self.valid_entry),"%S"))
        self.entry_caducidad.config(width=10)
        self.entry_caducidad.place(x=300,y=165)
        
        self.entry_cant = Entry(self.view,textvariable=self.var_cant,validate='key',validatecommand=(self.view.register(self.valid_entry),"%S"))
        self.entry_cant.config(width=15)
        self.entry_cant.place(x=300,y=435)

    def destroy_organic_gui(self):
        self.entry_caducidad.destroy()
        self.entry_cant.destroy()
    
    def not_organic_gui(self):
        self.view.label_caducidad.config(text="Ingrese fecha de vencimiento:")
        self.view.label_cant.config(text="Ingrese la cantidad del alimento en unidades:")

        self.label_day = Label(self.view, text="dd:", bg="white", justify="center",font=("Little Comet Bubling Demo Version",10,"bold"))
        self.label_day.place(x=300,y=165)

        self.entry_day = Entry(self.view,textvariable=self.var_day,validate='key',validatecommand=(self.view.register(self.valid_entry),"%S"))
        self.entry_day.config(width=5)
        self.entry_day.place(x=325,y=165)

        self.label_month = Label(self.view, text="/mm:", bg="white", justify="center",font=("Little Comet Bubling Demo Version",10,"bold"))
        self.label_month.place(x=360,y=165)

        self.entry_month = Entry(self.view,textvariable=self.var_month,validate='key',validatecommand=(self.view.register(self.valid_entry),"%S"))
        self.entry_month.config(width=5)
        self.entry_month.place(x=398,y=165)

        self.label_year = Label(self.view, text="/yyy:", bg="white", justify="center",font=("Little Comet Bubling Demo Version",10,"bold"))
        self.label_year.place(x=432,y=165)

        self.entry_year = Entry(self.view,validate='key',textvariable=self.var_year,validatecommand=(self.view.register(self.valid_entry),"%S"))
        self.entry_year.config(width=5)
        self.entry_year.place(x=468,y=165)

        self.entry_cant = Entry(self.view,textvariable=self.var_cant,validate='key',validatecommand=(self.view.register(self.valid_entry),"%S"))
        self.entry_cant.config(width=15)
        self.entry_cant.place(x=300,y=435)

    def destroy_not_organic_gui(self):
        self.label_day.destroy()
        self.entry_day.destroy()
        self.label_month.destroy()
        self.entry_month.destroy()
        self.label_year.destroy()
        self.entry_year.destroy()
        self.entry_cant.destroy()

    def select_image(self):
        types = (('PNG', '*.png'),("JPG", "*.jpg"))
        self.imagen = filedialog.askopenfilenames(title="Seleccione la imagen", initialdir="C:/",filetypes=types)

        self.view.label_image.insert(INSERT,str(self.imagen[0]))

    def valid_entry(self, text):
        return text.isdecimal()
