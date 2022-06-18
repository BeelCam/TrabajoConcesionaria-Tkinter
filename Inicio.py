from tkinter import *
import os

import sys
from tkinter.messagebox import askyesno
from turtle import Vec2D, title
from numpy import place
from setuptools import Command
from sklearn.preprocessing import label_binarize

def ventana_inicio():
    global ventana_principal
    colorRosa = "#F5A9BC"# Color para encabezado
   
    ventana_principal=Tk()
    ventana_principal.geometry("300x250")#DIMENSIONES DE LA VENTANA
    ventana_principal.resizable(0,0)
    ventana_principal.title("La Concesionaria")#TITULO DE LA VENTANA
    ventana_principal.iconbitmap("auto.ico")
    Label(ventana_principal, text = "Bienvenido", font=("Arial", 13)).pack()
    Label(text="").pack()
    Label(text="La Concesionario", bg= colorRosa, width="300", height="2", font=("Arial", 13))
    Label(text="").pack()
    Button(text="Acceder", height="2", width="30", command=login, borderwidth = 1).pack() #BOTÓN "Acceder"
    Label(text="").pack()
    Button(text="Registrarse", height="2", width="30", command=registro, borderwidth = 1).pack() #BOTÓN "Registrarse".
    Label(text="").pack()

    ventana_principal.mainloop()

def registro(): #REGISTRARME

    global ventana_registro

    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("Registro")
    ventana_registro.geometry("300x250")
    ventana_registro.resizable(0,0)
    ventana_registro.iconbitmap("añadirUsuario.ico")
    colorRosa = "#F5A9BC"# Color para encabezado
    colorGris="DarkGrey" #Color para boton

    global nombre_usuario
    global clave
    global entrada_nombre
    global entrada_clave
    
    nombre_usuario = StringVar() #DECLARAMOS "string" COMO TIPO DE DATO PARA "nombre_usuario"
    clave = StringVar() #DECLARAMOS "sytring" COMO TIPO DE DATO PARA "clave"
 
    Label(ventana_registro, text="Introduzca datos", bg= colorRosa, width="100", height="2",font=("Arial", 13)).pack()
    Label(ventana_registro, text="").pack()
    etiqueta_nombre = Label(ventana_registro, text="Nombre de usuario * ")
    etiqueta_nombre.pack()
    entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario) #ESPACIO PARA INTRODUCIR EL NOMBRE.
    entrada_nombre.pack()
    etiqueta_clave = Label(ventana_registro, text="Contraseña * ")
    etiqueta_clave.pack()
    entrada_clave = Entry(ventana_registro, textvariable=clave, show='*') #ESPACIO PARA INTRODUCIR LA CONTRASEÑA.
    entrada_clave.pack()
    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="Registrarse", width=10, height=1, command = registro_usuario, borderwidth = 1).pack() #BOTÓN "Registrarse"

#REGISTRO USUARIO
 
def registro_usuario():
 
    usuario_info = nombre_usuario.get()
    clave_info = clave.get()
    #LLAMAS A TU FUNCION QUE VALIDA QUE ESE USUARIO ESTA!
    file = open(usuario_info, "w") #CREACION DE ARCHIVO CON "nombre" y "clave"
    file.write(usuario_info + "\n")
    file.write(clave_info)
    file.close()
 
    entrada_nombre.delete(0, END)
    entrada_clave.delete(0, END)
 
    Label(ventana_registro, text="Registro completado con éxito", fg="green", font=("Arial", 12)).pack()

#CREAMOS VENTANA PARA LOGIN.

def login():
    colorRosa = "#F5A9BC"# Color para encabezado
 
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("350x250")
    ventana_login.resizable(0,0)
    ventana_login.iconbitmap("login.ico")
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña",bg= colorRosa, width="100", height="2", font=("Arial", 13)).pack()
    Label(ventana_login, text="").pack()
 
    global verifica_usuario
    global verifica_clave
 
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave
 
    Label(ventana_login, text="Nombre usuario * ", font=("Arial", 12)).pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="").pack()
    Label(ventana_login, text="Contraseña *" , font=("Arial", 12)).pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command = verifica_login).pack()

#VENTANA "VERIFICACION DE LOGIN".

def verifica_login():
    usuario1 = verifica_usuario.get()#tomo lo q pone
    clave1 = verifica_clave.get()#TOMO LO QUE PONE
    entrada_login_usuario.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Nombre usuario *" AL MOSTRAR NUEVA VENTANA.
    entrada_login_clave.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Contraseña *" AL MOSTRAR NUEVA VENTANA.
 
    lista_archivos = os.listdir() #GENERA LISTA DE ARCHIVOS UBICADOS EN EL DIRECTORIO.
    #SI EL NOMBRE SE ENCUENTRA EN LA LISTA DE ARCHIVOS..
    if usuario1 in lista_archivos:
        archivo1 = open(usuario1, "r") #APERTURA DE ARCHIVO EN MODO LECTURA
        verifica = archivo1.read().splitlines() #LECTURA DEL ARCHIVO QUE CONTIENE EL nombre Y contraseña.
        #SI LA CONTRASEÑA INTRODUCIDA SE ENCUENTRA EN EL ARCHIVO...
        if clave1 in verifica:
            if clave1 == "admin":
                menuAdmin() #...EJECUTAR FUNCIÓN "exito_login()"
        #SI LA CONTRASEÑA NO SE ENCUENTRA EN EL ARCHIVO....
        if clave1 in verifica:
            if clave1 == "empleado":
                menuEmpleado() #...EJECUTAR FUNCIÓN "exito_login()"
        if clave1 in verifica:
            if clave1 == "invitado":
                menuAdmin() #...EJECUTAR FUNCIÓN "exito_login()"
        else:
            no_clave() #...EJECUTAR "no_clave()"
    #SI EL NOMBRE INTRODUCIDO NO SE ENCUENTRA EN EL DIRECTORIO...
    else:
        no_usuario() #..EJECUTA "no_usuario()".


# VENTANA "Login finalizado con exito".
 
def exito_login():
    global ventana_exito
    ventana_exito = Toplevel(ventana_login)
    ventana_exito.title("Exito")
    ventana_exito.geometry("250x100")
    ventana_exito.resizable(0,0)
    ventana_exito.iconbitmap("login.ico")
    Label(ventana_exito, text="Ingresar a concesionaria").pack()
    Button(ventana_exito, text="OK", command=menuAdmin).pack()
 
#VENTANA DE "Contraseña incorrecta".
 
def no_clave():
    global ventana_no_clave
    ventana_no_clave = Toplevel(ventana_login)
    ventana_no_clave.title("ERROR")
    ventana_no_clave.geometry("250x100")
    ventana_no_clave.resizable(0,0)
    ventana_no_clave.iconbitmap("error.ico")
    
    Label(ventana_no_clave, text="Contraseña incorrecta ").pack()
    Button(ventana_no_clave, text="OK", command=borrar_no_clave).pack() #EJECUTA "borrar_no_clave()".
 
#VENTANA DE "Usuario no encontrado".
 
def no_usuario():
    global ventana_no_usuario
    ventana_no_usuario = Toplevel(ventana_login)
    ventana_no_usuario.title("ERROR")
    ventana_no_usuario.geometry("250x100")
    ventana_no_usuario.resizable(0,0)
    ventana_no_usuario.iconbitmap("error.ico")
    Label(ventana_no_usuario, text="Usuario no encontrado").pack(side = BOTTOM)
    Button(ventana_no_usuario, text="OK", command=borrar_no_usuario).pack() #EJECUTA "borrar_no_usuario()"

#VENTANA MENU ADMIN
def menuAdmin():
    global ventanaAdmin
    
    ventanaAdmin = Toplevel(ventana_login)
    ventanaAdmin.title("Menu admin")
    ventanaAdmin.geometry("400x400")
    ventanaAdmin.resizable(0,0)
    ventanaAdmin.iconbitmap("admin.ico")
    colorRosa = "#F5A9BC"

    Label(ventanaAdmin, text="Menu administrador", bg= colorRosa, width="100", height="2", font=("Arial", 13)).pack()
    Label(text="").pack()
    
    labelAutos = Label (ventanaAdmin, text = "Autos", font=("Arial", 12))
    labelAutos.place(x=30,y=50)

    botonAgregar = Button(ventanaAdmin,text = "Agregar", command=AgregarAuto)
    botonAgregar.place(x=130, y = 50)
    botonVerTodo = Button(ventanaAdmin, text =  "Ver Todo", command=VerTodoAutos)
    botonVerTodo.place(x=200, y = 50)


    labelMotos = Label (ventanaAdmin, text = "Motos", font=("Arial", 12))
    labelMotos.place(x=30,y=100)

    botonAgregar = Button(ventanaAdmin, text = "Agregar", command = AgregarMoto)
    botonAgregar.place(x=130, y = 100)
    botonVerTodo = Button(ventanaAdmin, text =  "Ver Todo", command=VerTodoMotos)
    botonVerTodo.place(x=200, y = 100)


    labelCamionetas = Label (ventanaAdmin, text = "Camionetas", font=("Arial", 12))
    labelCamionetas.place(x=30,y=150)

    botonAgregar = Button(ventanaAdmin, text = "Agregar", command=AgregarCamioneta)
    botonAgregar.place(x=130, y = 150)
    botonVerTodo = Button(ventanaAdmin, text =  "VerTodo", command=VerTodoCamioneta)
    botonVerTodo.place(x=200, y =150)


    labelCamiones = Label (ventanaAdmin, text = "Camiones", font=("Arial", 12))
    labelCamiones.place(x=30,y=200)

    botonAgregar = Button(ventanaAdmin, text = "Agregar", command=AgregarCamion)
    botonAgregar.place(x=130, y = 200)
    botonVerTodo = Button(ventanaAdmin, text =  "Ver Todo", command=VerTodoCamion)
    botonVerTodo.place(x=200, y = 200)


    labelBicicletas = Label (ventanaAdmin, text = "Bicicletas", font=("Arial", 12))
    labelBicicletas.place(x=30,y=250)

    botonAgregar = Button(ventanaAdmin, text = "Agregar", command=AgregarBici)
    botonAgregar.place(x=130, y = 250)
    botonVerTodo = Button(ventanaAdmin, text =  "Ver Todo", command=VerTodoBici)
    botonVerTodo.place(x=200, y = 250)
    


    labelColectivos = Label (ventanaAdmin, text = "Colectivos", font=("Arial", 12))
    labelColectivos.place(x=30,y=300)

    botonAgregar = Button(ventanaAdmin, text = "Agregar", command=AgregarColectivo)
    botonAgregar.place(x=130, y = 300)
    botonVerTodo = Button(ventanaAdmin, text =  "Ver Todo", command=VerTodoColectivo)
    botonVerTodo.place(x=200, y = 300)


    labelAcoplados = Label (ventanaAdmin, text = "Acoplados", font=("Arial", 12))
    labelAcoplados.place(x=30,y=350)

    botonAgregar = Button(ventanaAdmin, text = "Agregar", command=AgregarAcoplado)
    botonAgregar.place(x=130, y = 350)
    botonVerTodo = Button(ventanaAdmin, text =  "Ver Todo", command=VerTodoAcoplado)
    botonVerTodo.place(x=200, y = 350)
    



def AgregarAuto():
    global ventanaAgregarAuto
    global modelo_auto 
    global marca_auto
    global km_auto
    global precio_auto
    global detalle_auto

    ventanaAgregarAuto = Toplevel(ventanaAdmin)
    ventanaAgregarAuto.title("Agregar")
    ventanaAgregarAuto.geometry("400x300")
    ventanaAgregarAuto.iconbitmap("agregar.ico")
    
    
    detalle_auto = StringVar()
    modelo_auto = StringVar()
    marca_auto = StringVar()
    km_auto = StringVar()
    precio_auto = StringVar()

    Label(ventanaAgregarAuto, text="Agregar Autos", width="100", height="2", font=("Arial", 13)).pack()
    Label(text="").pack()

    labelMarca = Label (ventanaAgregarAuto, text = "Marca", font=("Arial", 12))
    labelMarca.place(x=30,y=40)
    entradaMarca = Entry(ventanaAgregarAuto, textvariable= marca_auto)
    entradaMarca.place(x =140, y = 45)

    labelModelo = Label (ventanaAgregarAuto, text = "Modelo", font=("Arial", 12))
    labelModelo.place(x=30,y=70)
    entradaModelo = Entry(ventanaAgregarAuto, textvariable=modelo_auto)
    entradaModelo.place(x =140, y = 75)

    labelKm = Label (ventanaAgregarAuto, text = "Kilometros", font=("Arial", 12))
    labelKm.place(x=30,y=110)
    entradaKm = Entry(ventanaAgregarAuto, textvariable=km_auto)
    entradaKm.place(x =140, y = 113)

    labelPrecio = Label (ventanaAgregarAuto, text = "Precio", font=("Arial", 12))
    labelPrecio.place(x=30,y=150)
    entradaPrecio = Entry(ventanaAgregarAuto, textvariable=precio_auto)
    entradaPrecio.place(x =140, y = 153)

    labelDetalle = Label (ventanaAgregarAuto, text = "Detalle", font=("Arial", 12))
    labelDetalle.place(x=30,y=180)
    entradaDetalle = Entry(ventanaAgregarAuto, textvariable= detalle_auto)
    entradaDetalle.place(x =140, y = 183)


    botonAceptar = Button(ventanaAgregarAuto, text = "Guardar", command = GuardarAutos)
    botonAceptar.place(x = 160, y = 220)
    botonCancelar = Button(ventanaAgregarAuto, text = "Cancelar", command =borrar_agregar_auto)
    botonCancelar.place(x = 240, y = 220)

def GuardarAutos():
    global autoModelo
    global autoMarca
    global autoKm
    global autoPrecio
    global autoDetalle
    
    autoModelo = modelo_auto.get()
    autoMarca = marca_auto.get()
    autoKm = km_auto.get()
    autoPrecio = precio_auto.get()
    autoDetalle = detalle_auto.get()
    
    file = open(autoMarca, "w")
    file.write("Marca: " + autoMarca + "\n")
    file.write("Modelo: " + autoModelo + "\n")
    file.write("Kilometros: " + autoKm + "\n")
    file.write("Precio: " + autoPrecio + "\n")
    file.write("Detalle: " + autoDetalle + "\n")
    file.close()
 
    modelo_auto.delete(0, END)
    marca_auto.delete(0, END)
    km_auto.delete(0, END)
    precio_auto.delete(0, END)
    detalle_auto.delete(0, END)


def VerTodoAutos():
    global ventanaVerTodoAuto
    global autoModelo
    global autoMarca
    global autoKm
    global autoPrecio
    global autoDetalle

    detalle_auto = StringVar()
    modelo_auto = StringVar()
    marca_auto = StringVar()
    km_auto = StringVar()
    precio_auto = StringVar()

    autoModelo = modelo_auto.get()
    autoMarca = marca_auto.get()
    autoKm = km_auto.get()
    autoPrecio = precio_auto.get()
    autoDetalle = detalle_auto.get()

    ventanaVerTodoAuto = Toplevel(ventanaAdmin)
    ventanaVerTodoAuto.title("Ver Todo")
    ventanaVerTodoAuto.geometry("500x500")
    ventanaVerTodoAuto.iconbitmap("verTodo.ico")

    listbox = Listbox(ventanaVerTodoAuto, width=70,height=20)
    listbox.place(x= 30, y = 30) 
    scrollbar = Scrollbar(ventanaVerTodoAuto, width=20) 
    scrollbar.place(x=453, y =30) 

    #autoMarca = open("FiatUno", "r") #APERTURA DE ARCHIVO EN MODO LECTURA
    #file = open(autoMarca)
    #file.write("Modelo: " + autoMarca + "\n")
    #file.write("Marca" + autoModelo + "\n")
    #file.write("Kilometros: " + autoKm + "\n")
    #file.write("Precio: " + autoPrecio + "\n")
    #file.write("Detalle: " + autoDetalle + "\n")
    

    #listaAutos = os.listdir() #GENERA LISTA DE ARCHIVOS UBICADOS EN EL DIRECTORIO.
    #SI EL NOMBRE SE ENCUENTRA EN LA LISTA DE ARCHIVOS..
    #if autoMarca in listaAutos:
     #   listaAutos = open(autoMarca, "r") #APERTURA DE ARCHIVO EN MODO LECTURA
      #  listaAutos.read().splitlines() 

    listbox.insert(0,"")

    listbox.config(yscrollcommand = scrollbar.set) 
    scrollbar.config(command = listbox.yview) 

#VENTANA AGREGA MOTO
def AgregarMoto():
    global ventanaAgregarMoto
    
    ventanaAgregarMoto = Toplevel(ventanaAdmin)
    ventanaAgregarMoto.title("Agregar")
    ventanaAgregarMoto.geometry("400x300")
    ventanaAgregarMoto.iconbitmap("agregar.ico")

    global modelo_moto 
    global marca_moto
    global cilin_moto
    global km_moto
    global precio_moto
    global detalle_moto
    cilin_moto = StringVar()
    detalle_moto = StringVar()
    modelo_moto = StringVar()
    marca_moto = StringVar()
    km_moto = StringVar()
    precio_moto = StringVar()

    Label(ventanaAgregarMoto, text="Agregar Moto", width="100", height="2", font=("Arial", 13)).pack()
    Label(text="").pack()

    labelMarca = Label (ventanaAgregarMoto, text = "Marca", font=("Arial", 12))
    labelMarca.place(x=30,y=40)
    entradaMarca = Entry(ventanaAgregarMoto, textvariable= marca_moto)
    entradaMarca.place(x =140, y = 45)

    labelModelo = Label (ventanaAgregarMoto, text = "Modelo", font=("Arial", 12))
    labelModelo.place(x=30,y=70)
    entradaModelo = Entry(ventanaAgregarMoto, textvariable= modelo_moto)
    entradaModelo.place(x =140, y = 75)

    labelCilin = Label (ventanaAgregarMoto, text = "Cilindrada", font=("Arial", 12))
    labelCilin.place(x=30,y=110)
    entradaCilin = Entry(ventanaAgregarMoto, textvariable= cilin_moto)
    entradaCilin.place(x =140, y = 113)

    labelKm = Label (ventanaAgregarMoto, text = "Kilometros", font=("Arial", 12))
    labelKm.place(x=30,y=150)
    entradaKm = Entry(ventanaAgregarMoto, textvariable= km_moto)
    entradaKm.place(x =140, y = 153)

    labelPrecio = Label (ventanaAgregarMoto, text = "Precio", font=("Arial", 12))
    labelPrecio.place(x=30,y=180)
    entradaPrecio = Entry(ventanaAgregarMoto, textvariable= precio_moto)
    entradaPrecio.place(x =140, y = 183)

    labelDetalle = Label (ventanaAgregarMoto, text = "Detalles", font = ("Arial", 12))
    labelDetalle.place(x=30,y=210)
    entradaDetalle = Entry(ventanaAgregarMoto, textvariable= detalle_moto)
    entradaDetalle.place(x =140, y = 213)


    botonAceptar = Button(ventanaAgregarMoto, text = "Guardar", command=GuardarMoto)
    botonAceptar.place(x = 160, y = 250)
    botonCancelar = Button(ventanaAgregarMoto, text = "Cancelar", command=borrar_agregar_moto)
    botonCancelar.place(x = 230, y = 250)

def GuardarMoto():
    global motoModelo
    global motoMarca
    global motoCilin
    global motoKm
    global motoPrecio
    global motoDetalle
    motoModelo = modelo_moto.get()
    motoMarca = marca_moto.get()
    motoCilin = cilin_moto.get()
    motoKm = km_moto.get()
    motoPrecio = precio_moto.get()
    motoDetalle = detalle_moto.get()
    
    file = open(motoMarca, "w")
    file.write("Marca: " + motoMarca + "\n")
    file.write("Modelo: " + motoModelo + "\n")
    file.write("Cilindrada: " + motoCilin + "\n")
    file.write("Kilometros: " + motoKm + "\n")
    file.write("Precio: " + motoPrecio + "\n")
    file.write("Detalle: " + motoDetalle + "\n")
    file.close()

    modelo_moto.delete(0, END)
    marca_moto.delete(0, END)
    cilin_moto.delete(0, END)
    km_moto.delete(0, END)
    precio_moto.delete(0, END)
    detalle_moto.delete(0, END)

def VerTodoMotos():
    pass


def AgregarCamion():
    global ventanaAgregarCamion
    
    ventanaAgregarCamion = Toplevel(ventanaAdmin)
    ventanaAgregarCamion.title("Agregar")
    ventanaAgregarCamion.geometry("400x300")
    ventanaAgregarCamion.iconbitmap("agregar.ico")
    global modelo_camion 
    global marca_camion
    global km_camion
    global precio_camion
    global detalle_camion
    detalle_camion = StringVar()
    modelo_camion = StringVar()
    marca_camion = StringVar()
    km_camion = StringVar()
    precio_camion = StringVar()

    Label(ventanaAgregarCamion, text="Agregar Camion", width="100", height="2", font=("Arial", 13)).pack()
    Label(text="").pack()

    labelMarca = Label (ventanaAgregarCamion, text = "Marca", font=("Arial", 12))
    labelMarca.place(x=30,y=40)
    entradaMarca = Entry(ventanaAgregarCamion, textvariable= marca_camion)
    entradaMarca.place(x =140, y = 45)

    labelModelo = Label (ventanaAgregarCamion, text = "Modelo", font=("Arial", 12))
    labelModelo.place(x=30,y=70)
    entradaModelo = Entry(ventanaAgregarCamion, textvariable= modelo_camion)
    entradaModelo.place(x =140, y = 75)

    labelKm = Label (ventanaAgregarCamion, text = "Kilometros", font=("Arial", 12))
    labelKm.place(x=30,y=110)
    entradaKm = Entry(ventanaAgregarCamion, textvariable= km_camion)
    entradaKm.place(x =140, y = 113)

    labelPrecio = Label (ventanaAgregarCamion, text = "Precio", font=("Arial", 12))
    labelPrecio.place(x=30,y=150)
    entradaPrecio = Entry(ventanaAgregarCamion, textvariable= precio_camion)
    entradaPrecio.place(x =140, y = 153)

    labelDetalle = Label (ventanaAgregarCamion, text = "Detalles", font=("Arial", 12))
    labelDetalle.place(x=30,y=180)
    entradaDetalle = Entry(ventanaAgregarCamion, textvariable= detalle_camion)
    entradaDetalle.place(x =140, y = 183)


    botonAceptar = Button(ventanaAgregarCamion, text = "Guardar", command=GuardarCamion)
    botonAceptar.place(x = 160, y = 250)
    botonCancelar = Button(ventanaAgregarCamion, text = "Cancelar", command=borrar_agregar_camion)
    botonCancelar.place(x = 230, y = 250)

def GuardarCamion():
    global camionModelo
    global camionMarca
    global camionKm
    global camionPrecio
    global camionDetalle
    camionModelo = modelo_camion.get()
    camionMarca = marca_camion.get()
    camionKm = km_camion.get()
    camionPrecio = precio_camion.get()
    camionDetalle = detalle_camion.get()
    
    file = open(camionMarca, "w")
    file.write("Marca: " + camionMarca + "\n")
    file.write("Modelo: " + camionModelo + "\n")
    file.write("Kilometros: " + camionKm + "\n")
    file.write("Precio: " + camionPrecio + "\n")
    file.write("Detalle: " + camionDetalle + "\n")
    file.close()

    modelo_camion.delete(0, END)
    marca_camion.delete(0, END)
    km_camion.delete(0, END)
    precio_camion.delete(0, END)
    detalle_camion.delete(0, END)

def VerTodoCamion():
    pass


def AgregarColectivo():
    global ventanaAgregarColectivo
    
    ventanaAgregarColectivo = Toplevel(ventanaAdmin)
    ventanaAgregarColectivo.title("Agregar")
    ventanaAgregarColectivo.geometry("400x300")
    ventanaAgregarColectivo.iconbitmap("agregar.ico")
    global modelo_colectivo 
    global marca_colectivo
    global km_colectivo
    global precio_colectivo
    global detalle_colectivo
    detalle_colectivo = StringVar()
    modelo_colectivo = StringVar()
    marca_colectivo = StringVar()
    km_colectivo = StringVar()
    precio_colectivo = StringVar()

    Label(ventanaAgregarColectivo, text="Agregar Camion", width="100", height="2", font=("Arial", 13)).pack()
    Label(text="").pack()

    labelMarca = Label (ventanaAgregarColectivo, text = "Marca", font=("Arial", 12))
    labelMarca.place(x=30,y=40)
    entradaMarca = Entry(ventanaAgregarColectivo, textvariable= marca_colectivo)
    entradaMarca.place(x =140, y = 45)

    labelModelo = Label (ventanaAgregarColectivo, text = "Modelo", font=("Arial", 12))
    labelModelo.place(x=30,y=70)
    entradaModelo = Entry(ventanaAgregarColectivo, textvariable= modelo_colectivo)
    entradaModelo.place(x =140, y = 75)

    labelKm = Label (ventanaAgregarColectivo, text = "Kilometros", font=("Arial", 12))
    labelKm.place(x=30,y=110)
    entradaKm = Entry(ventanaAgregarColectivo, textvariable= km_colectivo)
    entradaKm.place(x =140, y = 113)

    labelPrecio = Label (ventanaAgregarColectivo, text = "Precio", font=("Arial", 12))
    labelPrecio.place(x=30,y=150)
    entradaPrecio = Entry(ventanaAgregarColectivo, textvariable= precio_colectivo)
    entradaPrecio.place(x =140, y = 153)

    labelDetalle = Label (ventanaAgregarColectivo, text = "Detalles", font=("Arial", 12))
    labelDetalle.place(x=30,y=180)
    entradaDetalle = Entry(ventanaAgregarColectivo, textvariable= detalle_colectivo)
    entradaDetalle.place(x =140, y = 183)


    botonAceptar = Button(ventanaAgregarColectivo, text = "Guardar", command=GuardarColectivo)
    botonAceptar.place(x = 160, y = 250)
    botonCancelar = Button(ventanaAgregarColectivo, text = "Cancelar", command=borrar_agregar_colectivo)
    botonCancelar.place(x = 230, y = 250)

def GuardarColectivo():
    global colectivoModelo
    global colectivoMarca
    global colectivoKm
    global colectivoPrecio
    global colectivoDetalle
    colectivoModelo = modelo_colectivo.get()
    colectivoMarca = marca_colectivo.get()
    colectivoKm = km_colectivo.get()
    colectivoPrecio = precio_colectivo.get()
    colectivoDetalle = detalle_colectivo.get()
    
    file = open(colectivoMarca, "w")
    file.write("Marca: " + colectivoMarca + "\n")
    file.write("Modelo: " + colectivoModelo + "\n")
    file.write("Kilometros: " + colectivoKm + "\n")
    file.write("Precio: " + colectivoPrecio + "\n")
    file.write("Detalle: " + colectivoDetalle + "\n")
    file.close()

    modelo_colectivo.delete(0, END)
    marca_colectivo.delete(0, END)
    km_colectivo.delete(0, END)
    precio_colectivo.delete(0, END)
    detalle_colectivo.delete(0, END)

def VerTodoColectivo():
    pass



def AgregarCamioneta():
    global ventanaAgregarCamioneta
    
    ventanaAgregarCamioneta = Toplevel(ventanaAdmin)
    ventanaAgregarCamioneta.title("Agregar")
    ventanaAgregarCamioneta.geometry("400x300")
    ventanaAgregarCamioneta.iconbitmap("agregar.ico")
    global modelo_camioneta 
    global marca_camioneta
    global km_camioneta
    global precio_camioneta
    global detalle_camioneta
    detalle_camioneta = StringVar()
    modelo_camioneta = StringVar()
    marca_camioneta = StringVar()
    km_camioneta = StringVar()
    precio_camioneta = StringVar()

    Label(ventanaAgregarCamioneta, text="Agregar Camioneta", width="100", height="2", font=("Arial", 13)).pack()
    Label(text="").pack()

    labelMarca = Label (ventanaAgregarCamioneta, text = "Marca", font=("Arial", 12))
    labelMarca.place(x=30,y=40)
    entradaMarca = Entry(ventanaAgregarCamioneta, textvariable= marca_camioneta)
    entradaMarca.place(x =140, y = 45)

    labelModelo = Label (ventanaAgregarCamioneta, text = "Modelo", font=("Arial", 12))
    labelModelo.place(x=30,y=70)
    entradaModelo = Entry(ventanaAgregarCamioneta, textvariable= modelo_camioneta)
    entradaModelo.place(x =140, y = 75)

    labelKm = Label (ventanaAgregarCamioneta, text = "Kilometros", font=("Arial", 12))
    labelKm.place(x=30,y=110)
    entradaKm = Entry(ventanaAgregarCamioneta, textvariable= km_camioneta)
    entradaKm.place(x =140, y = 113)

    labelPrecio = Label (ventanaAgregarCamioneta, text = "Precio", font=("Arial", 12))
    labelPrecio.place(x=30,y=150)
    entradaPrecio = Entry(ventanaAgregarCamioneta, textvariable= km_camioneta)
    entradaPrecio.place(x =140, y = 153)

    labelDetalle = Label (ventanaAgregarCamioneta, text = "Detalles", font=("Arial", 12))
    labelDetalle.place(x=30,y=180)
    entradaDetalle = Entry(ventanaAgregarCamioneta, textvariable= precio_camioneta)
    entradaDetalle.place(x =140, y = 183)


    botonAceptar = Button(ventanaAgregarCamioneta, text = "Guardar", command=GuardarCamioneta)
    botonAceptar.place(x = 160, y = 250)
    botonCancelar = Button(ventanaAgregarCamioneta, text = "Cancelar", command=borrar_agregar_camioneta)
    botonCancelar.place(x = 230, y = 250)

def GuardarCamioneta():
    global camionetaModelo
    global camionetaMarca
    global camionetaKm
    global camionetaPrecio
    global camionetaDetalle
    camionetaModelo = modelo_camioneta.get()
    camionetaMarca = marca_camioneta.get()
    camionetaKm = km_camioneta.get()
    camionetaPrecio = precio_camioneta.get()
    camionetaDetalle = detalle_camioneta.get()
    
    file = open(camionetaMarca, "w")
    file.write("Marca: " + camionetaMarca + "\n")
    file.write("Modelo: " + camionetaModelo + "\n")
    file.write("Kilometros: " + camionetaKm + "\n")
    file.write("Precio: " + camionetaPrecio + "\n")
    file.write("Detalle: " + camionetaDetalle + "\n")
    file.close()

    modelo_camioneta.delete(0, END)
    marca_camioneta.delete(0, END)
    km_camioneta.delete(0, END)
    precio_camioneta.delete(0, END)
    detalle_camioneta.delete(0, END)

def VerTodoCamioneta():
    pass



def AgregarColectivo():
    global ventanaAgregarColectivo
    
    ventanaAgregarColectivo = Toplevel(ventanaAdmin)
    ventanaAgregarColectivo.title("Agregar")
    ventanaAgregarColectivo.geometry("400x300")
    ventanaAgregarColectivo.iconbitmap("agregar.ico")
    global modelo_colectivo 
    global marca_colectivo
    global km_colectivo
    global precio_colectivo
    global detalle_colectivo
    detalle_colectivo = StringVar()
    modelo_colectivo = StringVar()
    marca_colectivo = StringVar()
    km_colectivo = StringVar()
    precio_colectivo = StringVar()

    Label(ventanaAgregarColectivo, text="Agregar Colectivo", width="100", height="2", font=("Arial", 13)).pack()
    Label(text="").pack()

    labelMarca = Label (ventanaAgregarColectivo, text = "Marca", font=("Arial", 12))
    labelMarca.place(x=30,y=40)
    entradaMarca = Entry(ventanaAgregarColectivo, textvariable= marca_colectivo)
    entradaMarca.place(x =140, y = 45)

    labelModelo = Label (ventanaAgregarColectivo, text = "Modelo", font=("Arial", 12))
    labelModelo.place(x=30,y=70)
    entradaModelo = Entry(ventanaAgregarColectivo, textvariable= modelo_colectivo)
    entradaModelo.place(x =140, y = 75)

    labelKm = Label (ventanaAgregarColectivo, text = "Kilometros", font=("Arial", 12))
    labelKm.place(x=30,y=110)
    entradaKm = Entry(ventanaAgregarColectivo, textvariable= km_colectivo)
    entradaKm.place(x =140, y = 113)

    labelPrecio = Label (ventanaAgregarColectivo, text = "Precio", font=("Arial", 12))
    labelPrecio.place(x=30,y=150)
    entradaPrecio = Entry(ventanaAgregarColectivo, textvariable= precio_colectivo)
    entradaPrecio.place(x =140, y = 153)

    labelDetalle = Label (ventanaAgregarColectivo, text = "Detalles", font=("Arial", 12))
    labelDetalle.place(x=30,y=180)
    entradaDetalle = Entry(ventanaAgregarColectivo, textvariable= detalle_colectivo)
    entradaDetalle.place(x =140, y = 183)


    botonAceptar = Button(ventanaAgregarColectivo, text = "Guardar", command=GuardarColectivo)
    botonAceptar.place(x = 160, y = 250)
    botonCancelar = Button(ventanaAgregarColectivo, text = "Cancelar", command=borrar_agregar_colectivo)
    botonCancelar.place(x = 230, y = 250)

def GuardarColectivo():
    global colectivoModelo
    global colectivoMarca
    global colectivoKm
    global colectivoPrecio
    global colectivoDetalle
    colectivoModelo = modelo_colectivo.get()
    colectivoMarca = marca_colectivo.get()
    colectivoKm = km_colectivo.get()
    colectivoPrecio = precio_colectivo.get()
    colectivoDetalle = detalle_colectivo.get()
    
    file = open(colectivoMarca, "w")
    file.write("Marca: " + colectivoMarca + "\n")
    file.write("Modelo: " + colectivoModelo + "\n")
    file.write("Kilometros: " + colectivoKm + "\n")
    file.write("Precio: " + colectivoPrecio + "\n")
    file.write("Detalle: " + colectivoDetalle + "\n")
    file.close()

    modelo_colectivo.delete(0, END)
    marca_colectivo.delete(0, END)
    km_colectivo.delete(0, END)
    precio_colectivo.delete(0, END)
    detalle_colectivo.delete(0, END)

def VerTodoColectivo():
    pass



def AgregarBici():
    global ventanaAgregarBici
    
    ventanaAgregarBici = Toplevel(ventanaAdmin)
    ventanaAgregarBici.title("Agregar")
    ventanaAgregarBici.geometry("400x300")
    ventanaAgregarBici.iconbitmap("agregar.ico")
    global marca_bici
    global color_bici
    global rodado_bici
    global precio_bici
    global detalle_bici
    detalle_bici = StringVar()
    color_bici = StringVar()
    marca_bici = StringVar()
    rodado_bici = StringVar()
    precio_bici = StringVar()

    Label(ventanaAgregarBici, text="Agregar Bicicletas", width="100", height="2", font=("Arial", 13)).pack()
    Label(text="").pack()

    labelMarca = Label (ventanaAgregarBici, text = "Marca", font=("Arial", 12))
    labelMarca.place(x=30,y=40)
    entradaMarca = Entry(ventanaAgregarBici, textvariable= marca_bici)
    entradaMarca.place(x =140, y = 45)

    labelColor = Label (ventanaAgregarBici, text = "Color", font=("Arial", 12))
    labelColor.place(x=30,y=70)
    entradaColor = Entry(ventanaAgregarBici, textvariable= color_bici)
    entradaColor.place(x =140, y = 75)

    labelRodado = Label (ventanaAgregarBici, text = "Rodado", font=("Arial", 12))
    labelRodado.place(x=30,y=110)
    entradaRodado = Entry(ventanaAgregarBici, textvariable= rodado_bici)
    entradaRodado.place(x =140, y = 113)

    labelPrecio = Label (ventanaAgregarBici, text = "Precio", font=("Arial", 12))
    labelPrecio.place(x=30,y=150)
    entradaPrecio = Entry(ventanaAgregarBici, textvariable= precio_bici)
    entradaPrecio.place(x =140, y = 153)

    labelDetalle = Label (ventanaAgregarBici, text = "Detalles", font=("Arial", 12))
    labelDetalle.place(x=30,y=180)
    entradaDetalle = Entry(ventanaAgregarBici, textvariable= detalle_bici)
    entradaDetalle.place(x =140, y = 183)


    botonAceptar = Button(ventanaAgregarBici, text = "Guardar", command=GuardarBici)
    botonAceptar.place(x = 160, y = 250)
    botonCancelar = Button(ventanaAgregarBici, text = "Cancelar", command=borrar_agregar_bici)
    botonCancelar.place(x = 230, y = 250)

def GuardarBici():
    global biciRodado
    global biciMarca
    global biciColor
    global biciPrecio
    global biciDetalle
    global biciRodado
    biciRodado = rodado_bici.get()
    biciMarca = marca_bici.get()
    biciColor = color_bici.get()
    biciPrecio = precio_bici.get()
    biciDetalle = detalle_bici.get()
    
    file = open(biciMarca, "w")
    file.write("Marca: " + biciMarca + "\n")
    file.write("Rodado: " + biciRodado + "\n")
    file.write("Color: " + biciColor + "\n")
    file.write("Precio: " + biciPrecio + "\n")
    file.write("Detalle: " + biciDetalle + "\n")
    file.close()

    rodado_bici.delete(0, END)
    marca_bici.delete(0, END)
    color_bici.delete(0, END)
    precio_bici.delete(0, END)
    detalle_bici.delete(0, END)

def VerTodoBici():
    pass


def AgregarAcoplado():
    global ventanaAgregarAcoplado
    
    ventanaAgregarAcoplado = Toplevel(ventanaAdmin)
    ventanaAgregarAcoplado.title("Agregar")
    ventanaAgregarAcoplado.geometry("400x300")
    ventanaAgregarAcoplado.iconbitmap("agregar.ico")
    global marca_acoplado
    global tamaño_acoplado
    global peso_acoplado
    global precio_acoplado
    global detalle_acoplado
    tamaño_acoplado = StringVar()
    marca_acoplado = StringVar()
    peso_acoplado = StringVar()
    precio_acoplado = StringVar()
    detalle_acoplado = StringVar()

    Label(ventanaAgregarAcoplado, text="Agregar Acoplados", width="100", height="2", font=("Arial", 13)).pack()
    Label(text="").pack()

    labelMarca = Label (ventanaAgregarAcoplado, text = "Marca", font=("Arial", 12))
    labelMarca.place(x=30,y=40)
    entradaMarca = Entry(ventanaAgregarAcoplado, textvariable= marca_acoplado)
    entradaMarca.place(x =140, y = 45)

    labelTamaño = Label (ventanaAgregarAcoplado, text = "Tamaño", font=("Arial", 12))
    labelTamaño.place(x=30,y=70)
    entradaTamaño = Entry(ventanaAgregarAcoplado, textvariable= tamaño_acoplado)
    entradaTamaño.place(x =140, y = 75)

    labelPeso = Label (ventanaAgregarAcoplado, text = "Peso", font=("Arial", 12))
    labelPeso.place(x=30,y=110)
    entradaPeso = Entry(ventanaAgregarAcoplado, textvariable= peso_acoplado)
    entradaPeso.place(x =140, y = 113)

    labelPrecio = Label (ventanaAgregarAcoplado, text = "Precio", font=("Arial", 12))
    labelPrecio.place(x=30,y=150)
    entradaPrecio = Entry(ventanaAgregarAcoplado, textvariable= precio_acoplado)
    entradaPrecio.place(x =140, y = 153)

    labelDetalle = Label (ventanaAgregarAcoplado, text = "Detalles", font=("Arial", 12))
    labelDetalle.place(x=30,y=180)
    entradaDetalle = Entry(ventanaAgregarAcoplado, textvariable= detalle_acoplado)
    entradaDetalle.place(x =140, y = 183)


    botonAceptar = Button(ventanaAgregarAcoplado, text = "Guardar", command=GuardarAcoplado)
    botonAceptar.place(x = 160, y = 250)
    botonCancelar = Button(ventanaAgregarAcoplado, text = "Cancelar", command=borrar_agregar_acoplado)
    botonCancelar.place(x = 230, y = 250)

def GuardarAcoplado():
    global acopladoTamaño
    global acopladoMarca
    global acopladoPeso
    global acopladoPrecio
    global acopladoDetalle
    acopladoMarca = marca_acoplado.get()
    acopladoTamaño = tamaño_acoplado.get()
    acopladoPeso = peso_acoplado.get()
    acopladoPrecio = precio_acoplado.get()
    acopladoDetalle = detalle_acoplado.get()
    
    file = open(acopladoMarca, "w")
    file.write("Marca: " + acopladoMarca + "\n")
    file.write("Tamaño: " + acopladoTamaño + "\n")
    file.write("Peso: " + acopladoPeso + "\n")
    file.write("Precio: " + acopladoPrecio + "\n")
    file.write("Detalle: " + acopladoDetalle + "\n")
    file.close()

    marca_acoplado.delete(0, END)
    tamaño_acoplado.delete(0, END)
    peso_acoplado.delete(0, END)
    precio_acoplado.delete(0, END)
    detalle_acoplado.delete(0, END)

def VerTodoAcoplado():
    pass

def menuEmpleado():
    global ventanaEmpleado
    
    ventanaEmpleado = Toplevel(ventana_login)
    ventanaEmpleado.title("Menu admin")
    ventanaEmpleado.geometry("250x400")
    ventanaEmpleado.resizable(0,0)
    ventanaEmpleado.iconbitmap("admin.ico")
    colorRosa = "#F5A9BC"

    Label(ventanaEmpleado, text="Menu empleado", bg= colorRosa, width="100", height="2", font=("Arial", 13)).pack()
    Label(text="").pack()

    labelAutos = Label (ventanaEmpleado, text = "Autos", font=("Arial", 12))
    labelAutos.place(x=30,y=50)
    botonVerTodo = Button(ventanaEmpleado, text =  "Ver Todo", command=VerTodoAutos)
    botonVerTodo.place(x=130, y = 50)


    labelMotos = Label (ventanaEmpleado, text = "Motos", font=("Arial", 12))
    labelMotos.place(x=30,y=100)
    botonVerTodo = Button(ventanaEmpleado, text = "Ver Todo", command =VerTodoMotos)
    botonVerTodo.place(x=130, y = 100)


    labelCamionetas = Label (ventanaEmpleado, text = "Camionetas", font=("Arial", 12))
    labelCamionetas.place(x=30,y=150)
    botonVerTodo = Button(ventanaEmpleado, text = "Ver Todo", command=VerTodoCamioneta)
    botonVerTodo.place(x=130, y = 150)


    labelCamiones = Label (ventanaEmpleado, text = "Camiones", font=("Arial", 12))
    labelCamiones.place(x=30,y=200)
    botonVerTodo = Button(ventanaEmpleado, text = "Ver Todo", command=VerTodoCamion)
    botonVerTodo.place(x=130, y = 200)


    labelBicicletas = Label (ventanaEmpleado, text = "Bicicletas", font=("Arial", 12))
    labelBicicletas.place(x=30,y=250)
    botonVerTodo = Button(ventanaEmpleado, text = "VerTodo", command=VerTodoBici)
    botonVerTodo.place(x=130, y = 250)


    labelColectivos = Label (ventanaEmpleado, text = "Colectivos", font=("Arial", 12))
    labelColectivos.place(x=30,y=300)
    botonVerTodo = Button(ventanaEmpleado, text = "Ver Todo", command=VerTodoColectivo)
    botonVerTodo.place(x=130, y = 300)


    labelAcoplados = Label (ventanaEmpleado, text = "Acoplados", font=("Arial", 12))
    labelAcoplados.place(x=30,y=350)
    botonVerTodo = Button(ventanaEmpleado, text = "Ve rTodo", command=VerTodoAcoplado)
    botonVerTodo.place(x=130, y = 350)


#CERRADO DE VENTANAS
def borrar_agregar_bici():
    ventanaAgregarBici.destroy()

def borrar_agregar_acoplado():
    ventanaAgregarAcoplado.destroy()

def borrar_agregar_camion():
    ventanaAgregarCamion.destroy()

def borrar_agregar_camioneta():
    ventanaAgregarCamioneta.destroy()

def borrar_agregar_colectivo():
    ventanaAgregarColectivo.destroy()

def borrar_agregar_moto():
    ventanaAgregarMoto.destroy()

def borrar_agregar_auto():
    ventanaAgregarAuto.destroy()

def borrar_menu_admin():
    ventanaAdmin.destroy()

def borrar_exito_login():
    ventana_exito.destroy()

def borrar_no_clave():
    ventana_no_clave.destroy()

def borrar_no_usuario():
    ventana_no_usuario.destroy()

def borrarMenuAdmin():
    ventanaAdmin.destroy()

ventana_inicio() 