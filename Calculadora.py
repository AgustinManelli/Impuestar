from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.font as tkFont
import time, threading
import tkinter.ttk as ttk
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd
from tkinter import ttk
from configparser import ConfigParser
from configparser import SafeConfigParser
import tkinter.font as tkFont
from tkinter import *
import smtplib


############################RAIZ############################
app=Tk()

app.title('ImpuestAR 0.0.0.5 (Pre-Alpha)')

app.resizable(1,1)

app.iconbitmap('icono.ico')

app.geometry('800x500')

#app.config(bg='linen')


fuenteapp = tkFont.Font(font=("Arial", 12))
fuenteappline = tkFont.Font(font=("Arial", 12),underline=1)

######################CONFIGURACION#########################

fileconfig = 'config.ini'

config = ConfigParser()
config.read(fileconfig)

#print(config.sections())
#print(config.get('Graphics','theme'))
#print(config.getint('Graphics','font_scale'))
config.set('Graphics','font_scale','100')
with open('config.ini','w') as configfile:
    config.write(configfile)

apptheme = config.get('Graphics','theme')
#print (apptheme)


######################MENU DE VENTANA#######################

def creador():
    messagebox.showinfo(title='Creado por', message='Programa creado por agN con python 3.8')

def refresh():
    refrezcar = messagebox.askyesno(message='Quiere refrezcar la aplicacion?',title='ImpuestAR')
    if refrezcar is True:
        app.update()
        app.update_idletasks()
        #time.sleep(1)

def salirapp():
    salirr = messagebox.askyesno(message='Seguro desea salir?',title='ImpuestAR')
    if salirr is True:
        app.destroy()


def modonoche():
    app.configure(bg="grey40")
    frameingreso.configure(bg='grey40')
    ingreso.config(bg='grey60', fg='white',relief='flat')
    resultados.config(bg='grey40', fg='black',relief='flat')
    resultadoslabel.config(bg='grey40', fg='white')
    ingresolabel.config(bg='grey40', fg='white')
    ingresoimpuesto.config(bg='grey60', fg='white',relief='flat')
    botoningreso.config(bg='grey60', fg='white',activebackground="grey30",activeforeground="white",relief="flat",cursor='pirate')
    impuestolabel.config(bg='grey40', fg='white')
    impuestoerrorlabel.config(bg='grey40', fg='white')
    #presentacion.config(bg='grey40', fg='white')
    separador.config(bg='grey40',fg='white')
    horario.config(bg='grey40', fg='white')
    porcentajeingreso.config(bg='grey40', fg='white')
    pesoingreso.config(bg='grey40', fg='white')
    fotologo.config(file="logoimpnoche.png")
    check.config(bg='grey40', fg='grey60',relief='flat',cursor='hand2')
    vacio2.config(bg='grey40')
    #vacio.config(bg='grey40')
    fotologo2.config(file="logoimpnoche.png")
    #tituloars.config(bg='grey40', fg='white')
    #titulodolar.config(bg='grey40', fg='white')
    textingresoars.config(bg='grey40', fg='white')
    ingresoars.config(bg='grey60', fg='white',relief='flat')
    botoningresoars.config(bg='grey60', fg='white',relief='flat',cursor='pirate')
    #espaciadorarsdolar.config(bg='grey40', fg='white')
    textingresodolar.config(bg='grey40', fg='white')
    ingresodolar.config(bg='grey60', fg='white',relief='flat')
    botoningresodolar.config(bg='grey60', fg='white',relief='flat',cursor='pirate')
    separadorresultados.config(bg='grey40', fg='white')
    resultadoarsdolartext.config(bg='grey40', fg='white')
    resultadoarsdolar.config(bg='grey60', fg='red',relief='flat')
    resultadodolararstext.config(bg='grey40', fg='white')
    resultadodolarars.config(bg='grey60', fg='red',relief='flat')
    fuentedolar.config(bg='grey40', fg='white')
    frameingreso2.config(bg='grey40')
    dolaractualtext.config(bg='grey40', fg='white')
    dolaractual.config(bg='grey40', fg='white')
    marco1.config(bg='grey40', fg='white',relief='flat',highlightthickness=1, highlightbackground="grey60",highlightcolor='grey60')
    marco2.config(bg='grey40', fg='white',relief='flat',highlightthickness=1, highlightbackground="grey60",highlightcolor='grey60')
    s.configure('TFrame', background='grey40')


    config.set('Graphics', 'theme', 'modonoche')
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


    #advertencia = Label(frameingreso, bg='red', fg='white', text='Se cambio correctamente al modo nocturno')
    #advertencia.grid(row=10, column=0, columnspan=3)

    #def activar():
    #    tiempo = 100
    #    t = tiempo
    #    while t > 0:
    #        time.sleep(1)
    #        #progreso['value'] = ((t / tiempo) * 100 - 10)
    #        progreso = ((t / tiempo) * 100 - 10)
    #        t -= 20
    #    advertencia.destroy()
    #    #progreso.destroy()

    #th = threading.Thread(target=activar)
    #th.start()


def modorosa():
    app.configure(bg="thistle1")
    frameingreso.configure(bg='thistle1')
    ingreso.config(bg='white', fg='thistle4', relief='flat')
    resultados.config(bg='white', fg='thistle4', relief='flat')
    resultadoslabel.config(bg='thistle1', fg='thistle4')
    ingresolabel.config(bg='thistle1', fg='thistle4')
    ingresoimpuesto.config(bg='white', fg='thistle4', relief='flat')
    botoningreso.config(bg='white', fg='thistle4', activebackground="grey", activeforeground="thistle1", relief="flat",
                        cursor='heart')
    impuestolabel.config(bg='thistle1', fg='thistle4')
    impuestoerrorlabel.config(bg='thistle1', fg='thistle4')
    # presentacion.config(bg='grey40', fg='white')
    separador.config(bg='thistle1', fg='thistle4')
    horario.config(bg='thistle1', fg='thistle4')
    porcentajeingreso.config(bg='thistle1', fg='thistle4')
    pesoingreso.config(bg='thistle1', fg='thistle4')
    fotologo.config(file="logoimpdia.png")
    check.config(bg='thistle1', fg='thistle4', relief='flat',cursor='hand2')
    vacio2.config(bg='thistle1')
    # vacio.config(bg='grey40')
    fotologo2.config(file="logoimpdia.png")
    # tituloars.config(bg='grey40', fg='white')
    # titulodolar.config(bg='grey40', fg='white')
    textingresoars.config(bg='thistle1', fg='thistle4')
    ingresoars.config(bg='white', fg='thistle4', relief='flat')
    botoningresoars.config(bg='white', fg='thistle4', relief='flat', cursor='heart')
    # espaciadorarsdolar.config(bg='grey40', fg='white')
    textingresodolar.config(bg='thistle1', fg='thistle4')
    ingresodolar.config(bg='white', fg='thistle1', relief='flat')
    botoningresodolar.config(bg='white', fg='thistle4', relief='flat', cursor='heart')
    separadorresultados.config(bg='thistle1', fg='thistle4')
    resultadoarsdolartext.config(bg='thistle1', fg='thistle4')
    resultadoarsdolar.config(bg='white', fg='thistle4', relief='flat')
    resultadodolararstext.config(bg='thistle1', fg='thistle4')
    resultadodolarars.config(bg='white', fg='thistle4', relief='flat')
    fuentedolar.config(bg='thistle1', fg='thistle4')
    frameingreso2.config(bg='thistle1')
    dolaractualtext.config(bg='thistle1', fg='thistle4')
    dolaractual.config(bg='thistle1', fg='thistle4')
    marco1.config(bg='thistle1', fg='thistle4', relief='flat', highlightthickness=1, highlightbackground="thistle4",
                  highlightcolor='thistle4')
    marco2.config(bg='thistle1', fg='thistle4', relief='flat', highlightthickness=1, highlightbackground="thistle4",
                  highlightcolor='thistle4')
    s.configure('TFrame', background='thistle1')

    config.set('Graphics', 'theme', 'modorosa')
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


    #advertencia = Label(frameingreso, bg='red', fg='white', text='Se cambio correctamente al modo lightpink')
    #advertencia.grid(row=10, column=0, columnspan=3)

    #def activar():
    #    tiempo = 100
    #    t = tiempo
    #    while t > 0:
    #        time.sleep(1)
    #        # progreso['value'] = ((t / tiempo) * 100 - 10)
    #        progreso = ((t / tiempo) * 100 - 10)
    #        t -= 20
    #    advertencia.destroy()
    #    # progreso.destroy()

    #th = threading.Thread(target=activar)
    #th.start()


def mododia():
    app.configure(bg="white")
    frameingreso.configure(bg='white')
    ingreso.config(bg='grey90', fg='grey30', relief='flat')
    resultados.config(bg='grey90', fg='grey30', relief='flat')
    resultadoslabel.config(bg='white', fg='grey30')
    ingresolabel.config(bg='white', fg='grey30')
    ingresoimpuesto.config(bg='grey90', fg='grey30', relief='flat')
    botoningreso.config(bg='grey90', fg='grey30', activebackground="grey60", activeforeground="grey30", relief="flat",
                        cursor='hand2')
    impuestolabel.config(bg='white', fg='grey30')
    impuestoerrorlabel.config(bg='white', fg='grey30')
    # presentacion.config(bg='grey40', fg='white')
    separador.config(bg='white', fg='grey30')
    horario.config(bg='white', fg='grey30')
    porcentajeingreso.config(bg='white', fg='grey30')
    pesoingreso.config(bg='white', fg='grey30')
    fotologo.config(file="logoimpdia1.png")
    check.config(bg='white', fg='grey30', relief='flat',cursor='hand2')
    vacio2.config(bg='white')
    # vacio.config(bg='grey40')
    fotologo2.config(file="logoimpdia1.png")
    # tituloars.config(bg='grey40', fg='white')
    # titulodolar.config(bg='grey40', fg='white')
    textingresoars.config(bg='white', fg='grey30')
    ingresoars.config(bg='grey90', fg='grey30', relief='flat')
    botoningresoars.config(bg='grey90', fg='grey30', relief='flat', cursor='hand2')
    # espaciadorarsdolar.config(bg='grey40', fg='white')
    textingresodolar.config(bg='white', fg='grey30')
    ingresodolar.config(bg='grey90', fg='grey30', relief='flat')
    botoningresodolar.config(bg='grey90', fg='grey30', relief='flat', cursor='hand2')
    separadorresultados.config(bg='white', fg='grey30')
    resultadoarsdolartext.config(bg='white', fg='grey30')
    resultadoarsdolar.config(bg='grey90', fg='grey30', relief='flat')
    resultadodolararstext.config(bg='white', fg='grey30')
    resultadodolarars.config(bg='grey90', fg='grey30', relief='flat')
    fuentedolar.config(bg='white', fg='grey30')
    frameingreso2.config(bg='white')
    dolaractualtext.config(bg='white', fg='grey30')
    dolaractual.config(bg='white', fg='grey30')
    marco1.config(bg='white', fg='grey30', relief='flat', highlightthickness=1, highlightbackground="grey30",
                  highlightcolor='grey30')
    marco2.config(bg='white', fg='grey30', relief='flat', highlightthickness=1, highlightbackground="grey30",
                  highlightcolor='grey30')
    s.configure('TFrame', background='white')

    config.set('Graphics', 'theme', 'mododia')
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


    #advertencia = Label(frameingreso, bg='red', fg='white', text='Se cambio correctamente al modo dia')
    #advertencia.grid(row=10, column=0, columnspan=3)

    #def activar():
    #    tiempo = 100
    #    t = tiempo
    #    while t > 0:
    #        time.sleep(1)
    #        # progreso['value'] = ((t / tiempo) * 100 - 10)
    #        progreso = ((t / tiempo) * 100 - 10)
    #        t -= 20
    #    advertencia.destroy()
    #    # progreso.destroy()

    #th = threading.Thread(target=activar)
    #th.start()


def tamano1():
    app.geometry('500x300')
    advertencia = Label(frameingreso, bg='red', fg='white', text='Se cambio correctamente su resolucion')
    advertencia.grid(row=10, column=0, columnspan=3)


    ######################TEMPORIZADOR############################

    #progreso = ttk.Progressbar(frameingreso)
    #progreso.grid(row=11, column=0, columnspan=3)
    #progreso['value'] = 100
    progreso = 100

    def activar():
        tiempo = 100
        t = tiempo
        while t > 0:
            time.sleep(1)
            #progreso['value'] = ((t / tiempo) * 100 - 10)
            progreso = ((t / tiempo) * 100 - 10)
            t -= 20
        advertencia.destroy()
        #progreso.destroy()

    th = threading.Thread(target=activar)
    th.start()
    ###############################################################


def tamano2():
    app.geometry('1000x600')
    advertencia = Label(frameingreso, bg='red', fg='white', text='Se cambio correctamente su resolucion')
    advertencia.grid(row=10, column=0, columnspan=3)


    ######################TEMPORIZADOR############################

    #progreso = ttk.Progressbar(frameingreso)
    #progreso.grid(row=11, column=0, columnspan=3)
    #progreso['value'] = 100
    progreso = 100

    def activar():
        tiempo = 100
        t = tiempo
        while t > 0:
            time.sleep(1)
            #progreso['value'] = ((t / tiempo) * 100 - 10)
            progreso = ((t / tiempo) * 100 - 10)
            t -= 20
        advertencia.destroy()
        #progreso.destroy()

    th = threading.Thread(target=activar)
    th.start()
###############################################################


def version():
    messagebox.showinfo(title='Version', message='ImpuestAR-0.0.0.5 (Pre-Alpha)')


def tamanofuentemas():
    fontsize1=fuenteapp['size']
    fuenteapp.configure(size= fontsize1 + 2)

    fontsize2 = fuenteappline['size']
    fuenteappline.configure(size=fontsize2 + 2)



def tamanofuentemenos():
    fontsize1=fuenteapp['size']
    fuenteapp.configure(size=fontsize1 - 2)

    fontsize2 = fuenteappline['size']
    fuenteappline.configure(size=fontsize2 + 2)


def soporte():

    appsoporte = Tk()
    appsoporte.title('Soporte')
    appsoporte.resizable(0,0)
    appsoporte.iconbitmap('icono.ico')
    appsoporte.geometry('450x400')

    fuenteapp2 = tkFont.Font(font=("Arial", 8))

    ###################################

    def enviar():
        fromaddr = 'anon.imort3@gmail.com'
        toaddrs = 'sragustin01@hotmail.com'
        casillatexto = ingresosoporte.get(1.0,'end-1c')
        casillaemail = ingresomailsop.get()
        subjet='ImpuestAR soporte'

        msg = ('Subject: {}\n\nEnviado por: {}, dice: {}'.format(subjet, casillaemail, casillatexto))
        # Datos
        username = 'anon.imort3@gmail.com'
        password = 'SimpleAnonimo21'

        # Enviando el correo
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()

        advertencia = Label(Framesoportegral, bg='red', fg='white', text='Su email se envio correctamente, nos pondremos en contacto.')
        advertencia.grid(row=2, column=0)

        def activar():
           tiempo = 100
           t = tiempo
           while t > 0:
               time.sleep(1)
               #progreso['value'] = ((t / tiempo) * 100 - 10)
               progreso = ((t / tiempo) * 100 - 10)
               t -= 20
           advertencia.destroy()
           appsoporte.destroy()

        th = threading.Thread(target=activar)
        th.start()

    ###################################

    Framesoportegral = Frame(appsoporte, width=350, height=400)
    Framesoportegral.config(bg='white')
    Framesoportegral.pack()

    soportelf = LabelFrame(Framesoportegral, text='Contacto')
    soportelf.grid(row=0, column=0)
    soportelf.config(bg='white', fg='grey20')
    #soportelf.pack()

    ingresomailsop = Entry(soportelf)
    ingresomailsop.grid(row=1,column=0,padx=130)
    ingresotextsop = Label(soportelf, text='Ingrese su email:')
    ingresotextsop.grid(row=1,column=0,sticky='w')

    textosop = Label(soportelf, text='Envianos tu problema')
    textosop.grid(row=0,column=0)
    ingresosoporte = Text(soportelf,height=15,width=40)
    ingresosoporte.grid(row=2,column=0,pady=20)

    botonsoporte = Button(soportelf,text='Enviar',command=enviar)
    botonsoporte.grid(row=3,column=0)

    ###################################
    appsoporte.mainloop()



############################################################
s = ttk.Style()
#s.theme_use('default')
#s.configure('TNotebook.Tab', background="grey60",foreground='grey20')
#s.map("TNotebook", background= [("selected", "grey60")])
#s.configure('TNotebook', background='black')
s.configure('TFrame', background='black')
pestanas = ttk.Notebook(app, style='TNotebook')
pesimpuestos=ttk.Frame(pestanas)
pesdolar=ttk.Frame(pestanas)
pestanas.add(pesimpuestos,text='Impuestos')
pestanas.add(pesdolar,text='Dolar Hoy')
pestanas.pack(fill='both',expand='yes')
############################################################


topmenu=Menu(app)
menuarchivo=Menu(topmenu,tearoff=0)
#menuarchivo.add_command(label='Copiar',command=salirapp)
#menuarchivo.add_command(label='Pegar',command=salirapp)
#menuarchivo.add_separator()
menuarchivo.add_command(label='Actualizar',command=refresh)
menuarchivo.add_command(label='Salir',command=salirapp)
topmenu.add_cascade(label='Archivo',menu=menuarchivo)


menumodo=Menu(topmenu,tearoff=0)
topmenu.add_cascade(label='Configuracion',menu=menumodo)
temass = Menu(menumodo,tearoff=0)
temass.add_command(label='Dia',command=mododia)
temass.add_command(label='Noche',command=modonoche)
temass.add_command(label='Light Pink',command=modorosa)
menumodo.add_cascade(label='Temas', menu=temass)
#subres=Menu(menumodo,tearoff=0)
#subres.add_command(label='500x300',command=tamano1)
#subres.add_command(label='1000x600',command=tamano2)
#menumodo.add_cascade(label='Resoluciones', menu=subres)
fuente = Menu(menumodo, tearoff=0)
fuente.add_command(label='Aumentar',command=tamanofuentemas)
fuente.add_command(label='Reducir',command=tamanofuentemenos)
menumodo.add_cascade(label='Tamano de fuente', menu=fuente)


menuacerca=Menu(topmenu,tearoff=0)
menuacerca.add_command(label='Acerca de...',command=creador)
menuacerca.add_command(label='Version',command=version)
menuacerca.add_command(label='Soporte',command=soporte)
topmenu.add_cascade(label='Ayuda',menu=menuacerca)


app.config(menu=topmenu)
############################################################

#boton1=Frame()
#boton1.config(cursor='hand2')
#boton1.config(width='50',height='40')
#boton1.place(x=50,y=50)
#boton1.pack()



#barra = Frame()
#agregando anchor='s' or 'w' (puntos cardinales)
#barra.config(bd=x) (ancho del borde)
#barra.config(relief=x) (Tipo de borde: groove, sunken)
#barra.config(cursor='hand2') (Tipo de cursor: pirate y otros tipos)
##barra.config(bg='thistle1')
##barra.config(width=700, height=50)
##barra.pack(side='top', fill='x')

##########################PRESENTACION##########################
##boton1=Label(barra, text='ImpuestAR, la calculadora de impuestos',bg='thistle1', fg='thistle4')
##boton1.place(x=190, y=15)
################################################################

#fondo = Frame()
#agregando anchor='s' or 'w' (puntos cardinales)
#fondo.config(bg='light grey')
#fondo.config(width=500, height=700)
#fondo.pack(fill='y', expand='True')


#############################FUNCIONES################################
def funcioncheck():
    if check1.get() == 1:
        ingresoimpuesto.config(state='readonly')
    if check1.get() == 0:
        ingresoimpuesto.config(state='normal')


def funcion1():
    numeroingreso = ingreso.get()
    numeroimpuesto = ingresoimpuesto.get()
    if numeroingreso == '':
        messagebox.showwarning(message='Su ingreso no puede ser nulo', title='Error')
    elif numeroingreso.isdigit():
        if (check1.get()==1):
            resultadofuncion1 = (int(numeroingreso) * (67)) / 100
            result = (resultadofuncion1 + int(numeroingreso))
            pantallaimpuesto.set(67)
        elif numeroimpuesto == '':
            #resultadofuncion1 = (int(numeroingreso) * (67))/100
            #result = (resultadofuncion1+int(numeroingreso))
            #pantallaimpuesto.set(67)
            if (check1.get()==0):
                messagebox.showwarning(message='No puede dejar el impuesto vacio, tilde la opcion de impuestos automaticos.', title='Error')
        elif numeroimpuesto.isdigit():
            resultadofuncion1 = (int(numeroingreso) * int(numeroimpuesto))/100
            result = (resultadofuncion1+int(numeroingreso))
        elif numeroimpuesto.replace('.', '1').isdigit():
            resultadofuncion1 = (int(numeroingreso) * float(numeroimpuesto))/100
            result = (resultadofuncion1+int(numeroingreso))
        elif numeroimpuesto.replace(',', '1').isdigit():
            resultadofuncion1 = (int(numeroingreso) * float(numeroimpuesto.replace(',','.'))) / 100
            result = (resultadofuncion1 + int(numeroingreso))
        elif numeroimpuesto.lstrip('-').replace('.', '1').isdigit():
            resultadofuncion1 = (int(numeroingreso) * float(numeroimpuesto))/100
            result = (resultadofuncion1+int(numeroingreso))
        else:
            messagebox.showwarning(message='Debe ingresar un impuesto valido', title='Error')
    elif numeroingreso.replace('.','1').isdigit():
        if (check1.get()==1):
            resultadofuncion1 = (float(numeroingreso) * (67)) / 100
            result = (resultadofuncion1 + float(numeroingreso))
            pantallaimpuesto.set(67)
        elif numeroimpuesto == '':
            #resultadofuncion1 = (float(numeroingreso) * (67))/100
            #result = (resultadofuncion1+float(numeroingreso))
            #pantallaimpuesto.set(67)
            if (check1.get()==0):
                messagebox.showwarning(message='No puede dejar el impuesto vacio, tilde la opcion de impuestos automaticos.', title='Error')
        elif numeroimpuesto.isdigit():
            resultadofuncion1 = (float(numeroingreso) * int(numeroimpuesto))/100
            result = (resultadofuncion1+float(numeroingreso))
        elif numeroimpuesto.replace('.', '1').isdigit():
            resultadofuncion1 = (float(numeroingreso) * float(numeroimpuesto))/100
            result = (resultadofuncion1+float(numeroingreso))
        elif numeroimpuesto.replace(',', '1').isdigit():
            numeroimpuesto.replace(',','.')
            resultadofuncion1 = (float(numeroingreso) * float(numeroimpuesto.replace(',','.'))) / 100
            result = (resultadofuncion1 + float(numeroingreso))
        elif numeroimpuesto.lstrip('-').replace('.', '1').isdigit():
            resultadofuncion1 = (float(numeroingreso) * float(numeroimpuesto))/100
            result = (resultadofuncion1+float(numeroingreso))
        else:
            messagebox.showwarning(message='Debe ingresar un impuesto valido', title='Error')
    elif numeroingreso.replace(',', '1').isdigit():
        if (check1.get() == 1):
            resultadofuncion1 = (float(numeroingreso.replace(',', '.')) * (67)) / 100
            result = (resultadofuncion1 + float(numeroingreso.replace(',', '.')))
            pantallaimpuesto.set(67)
        elif numeroimpuesto == '':
            #resultadofuncion1 = (float(numeroingreso.replace(',','.')) * (67))/100
            #result = (resultadofuncion1+float(numeroingreso.replace(',','.')))
            #pantallaimpuesto.set(67)
            if (check1.get() == 0):
                messagebox.showwarning(message='No puede dejar el impuesto vacio, tilde la opcion de impuestos automaticos.',title='Error')
        elif numeroimpuesto.isdigit():
            resultadofuncion1 = (float(numeroingreso.replace(',','.')) * int(numeroimpuesto))/100
            result = (resultadofuncion1+float(numeroingreso.replace(',','.')))
        elif numeroimpuesto.replace('.', '1').isdigit():
            numeroimpuesto.replace(',','.')
            resultadofuncion1 = (float(numeroingreso.replace(',','.')) * float(numeroimpuesto))/100
            result = (float(resultadofuncion1)+float(numeroingreso.replace(',','.')))
        elif numeroimpuesto.replace(',', '1').isdigit():
            resultadofuncion1 = (float(numeroingreso.replace(',','.')) * float(numeroimpuesto.replace(',','.'))) / 100
            result = (resultadofuncion1 + float(numeroingreso.replace(',','.')))
        elif numeroimpuesto.lstrip('-').replace('.', '1').isdigit():
            resultadofuncion1 = (float(numeroingreso) * float(numeroimpuesto))/100
            result = (resultadofuncion1+float(numeroingreso))
        else:
            messagebox.showwarning(message='Debe ingresar un impuesto valido', title='Error')
    elif numeroingreso.lstrip('-').replace('.','1').isdigit():
        messagebox.showwarning(message='Debe ingresar un monto positivo', title='Error')
        #if numeroimpuesto == '':
        #    resultadofuncion1 = float(numeroingreso) * (0.67)
        #    result = (resultadofuncion1+float(numeroingreso))
        #    pantallaimpuesto.set(0.67)
        #elif numeroimpuesto.isdigit():
        #    resultadofuncion1 = (float(numeroingreso) * int(numeroimpuesto))/100
        #    result = (resultadofuncion1+float(numeroingreso))
        #elif numeroimpuesto.replace('.', '1').isdigit():
        #    resultadofuncion1 = (float(numeroingreso) * float(numeroimpuesto))/100
        #    result = (resultadofuncion1+float(numeroingreso))
        #elif numeroimpuesto.lstrip('-').replace('.', '1').isdigit():
        #    resultadofuncion1 = (float(numeroingreso) * float(numeroimpuesto))/100
        #    result = (resultadofuncion1+float(numeroingreso))
        #else:
        #    messagebox.askyesno(message='Debe ingresar un impuesto valido', title='Error')
    else:
        messagebox.showwarning(message='Debe ingresar un numero valido', title='Error')
    numeroresultado.set("%.2f" % result + 'AR$')

######################################################################
frameingreso=Frame(pesimpuestos, width=500, height=700)
frameingreso.config(bg='white')
#frameingreso.grid(row=0,column=0)
frameingreso.pack()
ingreso = Entry(frameingreso, font=fuenteapp)
ingreso.grid(row=3,column=1,sticky='e')
ingreso.config(justify='center',bg='white',fg='grey20')
pesoingreso=Label(frameingreso, text='$',bg='white',fg='grey20',font=fuenteapp)
pesoingreso.grid(row=3,column=2,sticky='w')
porcentajeingreso=Label(frameingreso, text='%',bg='white',fg='grey20',font=fuenteapp)
porcentajeingreso.grid(row=4,column=2,sticky='w')
numeroresultado = StringVar()
pantallaimpuesto = StringVar()
check1=IntVar()

resultados = Entry(frameingreso,state='readonly', textvariable=numeroresultado, font=fuenteapp)
resultados.grid(row=6, column=1,sticky='e')
resultados.config(justify='center',bg='white',fg='grey20')



#presentacion=Label(frameingreso, text='ImpuestAR, la calculadora de impuestos',bg='thistle1', fg='thistle4',font=fuenteapp)#font=fuenteapp
#presentacion.grid(row=0,column=0,columnspan=3)


separador=Label(frameingreso, text='_____________________________________________________________________________________________________',bg='white', fg='grey20')
separador.grid(row=1,column=0,columnspan=3)


resultadoslabel=Label(frameingreso, text='Resultado:',bg='white',fg='grey20',font=fuenteapp)
resultadoslabel.grid(row=6,column=0, sticky='e')


ingresolabel=Label(frameingreso, text='Ingrese el monto:',bg='white',fg='grey20',font=fuenteapp)
ingresolabel.grid(row=3,column=0,sticky='e')


ingresoimpuesto = Entry(frameingreso, textvariable=pantallaimpuesto,font=fuenteapp)
ingresoimpuesto.grid(row=4,column=1,sticky='e')
ingresoimpuesto.config(justify='center',bg='white',fg='grey20')


botoningreso = Button(frameingreso, text='Calcular',command=funcion1,bg='white',fg='grey20', font=fuenteapp,activebackground="grey60")
botoningreso.grid(row=6, column=2)
botoningreso.config(cursor='hand2')


impuestolabel=Label(frameingreso, text='Ingrese impuesto:',bg='white',fg='grey20',font=fuenteapp)
impuestolabel.grid(row=4,column=0,sticky='e')
impuestoerrorlabel=Label(frameingreso, text='(Si no ingresa un impuesto personalizado, el programa asignara uno automaticamente)',bg='white',fg='grey20',font=fuenteapp)
impuestoerrorlabel.grid(row=8,column=0,padx=0, columnspan=3)
#impuestoerrorlabel2=Label(frameingreso, text='(Es importante que coloque los numeros enteros sin comas ni puntos)',bg='thistle1',fg='thistle4',font=fuenteapp)
#impuestoerrorlabel2.grid(row=6,column=0,padx=0, columnspan=3)

check=Checkbutton(frameingreso, text='Impuesto Automático',bg='white',fg='grey20',font=fuenteapp,variable=check1,onvalue=1,offvalue=0,command=funcioncheck)
check.grid(row=4,column=2)

fotologo=PhotoImage(file="logoimpdia1.png")
Label(frameingreso, image=fotologo).grid(row=0,column=0,columnspan=3)

#vacio=Frame(frameingreso,width=500, height=400)
#vacio.grid(row=10,column=0,columnspan=3)
#vacio.config(bg='thistle1')
vacio2=Label(frameingreso,text='',bg='white')
vacio2.grid(row=2,column=0)


###########################RELOJ##############################
INTERVALO_REFRESCO_RELOJ = 300  #MS

def obtener_hora_actual():
    return datetime.now().strftime("%H:%M:%S")

def refrescar_reloj():
    variable_hora_actual.set(obtener_hora_actual())
    frameingreso.after(INTERVALO_REFRESCO_RELOJ, refrescar_reloj)

variable_hora_actual = StringVar(frameingreso, value=obtener_hora_actual())

horario =Label(frameingreso, textvariable=variable_hora_actual, font=fuenteapp,bg='white',fg='grey20')
horario.grid(row=9,column=0,columnspan=3)

refrescar_reloj()
###################OBTENCION DE DATOS DOLAR#####################

url = 'https://www.cronista.com/MercadosOnline/moneda.html?id=ARSSOL'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
dolar= soup.find_all('div',class_='sell-value')
dolar1= list()

for i in dolar:
    dolar1.append(i.text)
dolar2 = (dolar1[0].replace('$',''))
dolar3 = dolar2.replace(',','.')

################################################################

frameingreso2=Frame(pesdolar, width=500, height=700)
frameingreso2.config(bg='white')
frameingreso2.pack()
arsingreso = StringVar()
dolaringreso = StringVar()
arsresultado = StringVar ()
dolarresultado = StringVar()

###########################FUNCIONES############################[2]
def funcionars():
    numeroingresoars = ingresoars.get()
    numeroingresoars.replace(',','.')
    if numeroingresoars == '':
        resultadofuncionars = (1/float(dolar3))
    elif numeroingresoars.isdigit():
        resultadofuncionars = (int(numeroingresoars) / float(dolar3))
    elif numeroingresoars.replace('.', '1').isdigit():
        resultadofuncionars = (float(numeroingresoars) / float(dolar3))
    elif numeroingresoars.replace(',', '1').isdigit():
        numeroingresoars.replace(',','.')
        resultadofuncionars = (float(numeroingresoars.replace(',','.')) / float(dolar3))
    elif numeroingresoars.lstrip('-').replace('.', '1').isdigit():
        messagebox.showwarning(message='Debe ingresar un monto positivo', title='Error')
    else:
        messagebox.showwarning(message='Debe ingresar un numero valido', title='Error')
    arsresultado.set(str("%.2f" % resultadofuncionars) + str(' U$D'))


def funciondolar():
    numeroingresodolar = ingresodolar.get()
    numeroingresodolar.replace(',', '.')
    if numeroingresodolar == '':
        resultadofunciodolar = (float(dolar3) * 1)
    elif numeroingresodolar.isdigit():
        resultadofunciodolar = (float(dolar3) * int(numeroingresodolar))
    elif numeroingresodolar.replace('.', '1').isdigit():
        resultadofunciodolar = (float(numeroingresodolar) * float(dolar3))
    elif numeroingresodolar.replace(',', '1').isdigit():
        numeroingresodolar.replace(',', '.')
        resultadofunciodolar = (float(numeroingresodolar.replace(',', '.')) * float(dolar3))
    elif numeroingresodolar.lstrip('-').replace('.', '1').isdigit():
        messagebox.showwarning(message='Debe ingresar un monto positivo', title='Error')
    else:
        messagebox.showwarning(message='Debe ingresar un numero valido', title='Error')
    dolarresultado.set(str("%.2f" % resultadofunciodolar) + str(' AR$'))

################################################################

marco1=LabelFrame(frameingreso2,text='Pesos Argentinos a Dolar solidario',font=fuenteapp)
marco1.grid(row=1,column=0,columnspan=1,sticky='e')
marco1.config(bg='white',fg='grey20')

marco2=LabelFrame(frameingreso2,text='Dolar solidario a Pesos Argentinos',font=fuenteapp)
marco2.grid(row=1,column=3,columnspan=1,sticky='e')
marco2.config(bg='white',fg='grey20')
################################################################

fotologo2=PhotoImage(file="logoimpdia1.png")
Label(frameingreso2, image=fotologo2).grid(row=0,column=0,pady=20,columnspan=5)


#tituloars= Label(frameingreso2,text='AR$ a dolar solidario',font=fuenteapp,bg='white',fg='grey20')
#tituloars.grid(row=1,column=0,columnspan='2')

#titulodolar= Label(frameingreso2,text='Dolar a AR$',font=fuenteapp,bg='white',fg='grey20')
#titulodolar.grid(row=1,column=3,columnspan='2')


textingresoars= Label(marco1,text='Ingrese AR$: ',font=fuenteapp,bg='white',fg='grey20')
textingresoars.grid(row=2,column=0)
ingresoars = Entry(marco1, font=fuenteapp,bg='white',fg='grey20',textvariable=arsingreso)
ingresoars.grid(row=2,column=1,padx=10,pady=10,sticky='w')
botoningresoars = Button(marco1, text='Calcular',command=funcionars,bg='white',fg='grey20', font=fuenteapp)
botoningresoars.grid(row=6, column=1,pady=10,ipadx=40)
botoningresoars.config(cursor='hand2')


#espaciadorarsdolar= Label(frameingreso2,text='      |      ',font=fuenteapp,bg='white',fg='grey20')
#espaciadorarsdolar.grid(row=2,column=2)


textingresodolar= Label(marco2,text='Ingrese dolar: ',font=fuenteapp,bg='white',fg='grey20')
textingresodolar.grid(row=2,column=3)
ingresodolar = Entry(marco2, font=fuenteapp,bg='white',fg='grey20',textvariable=dolaringreso)
ingresodolar.grid(row=2,column=4,padx=10,pady=10,sticky='w')

botoningresodolar = Button(marco2, text='Calcular',command=funciondolar,bg='white',fg='grey20', font=fuenteapp)
botoningresodolar.grid(row=6, column=4,pady=10,ipadx=40)
botoningresodolar.config(cursor='hand2')


separadorresultados = Label(frameingreso2,text='_____________________________________________________________________________________________',font=fuenteapp,bg='white',fg='grey20')
separadorresultados.grid(row=7, column=0, columnspan=5)


resultadoarsdolartext = Label(marco1,font=fuenteappline,bg='white',fg='grey20',text='Resultado')
resultadoarsdolartext.grid(row=4,column=1)
resultadoarsdolar = Entry(marco1,font=fuenteapp,bg='white',fg='red',state='readonly',textvariable=arsresultado)
resultadoarsdolar.grid(row=5,column=1,padx=10,sticky='w')

resultadodolararstext = Label(marco2,font=fuenteappline,bg='white',fg='grey20',text='Resultado')
resultadodolararstext.grid(row=4,column=4)
resultadodolarars = Entry(marco2,font=fuenteapp,bg='white',fg='red',state='readonly',textvariable=dolarresultado)
resultadodolarars.grid(row=5,column=4,padx=10,sticky='w')
fuentedolar= Label(frameingreso2,font=fuenteappline,bg='white',fg='grey20',text='Datos tomados de cronista.com')
fuentedolar.grid(row=8,column=0,columnspan=5,pady=10)


dolaractualtext=Label(frameingreso2,text='Valor del dolar solidario:',font=fuenteapp,bg='white',fg='grey20')
dolaractualtext.grid(row=9,column=0,columnspan=5)
dolaractual=Label(frameingreso2,text=dolar2,font=fuenteapp,bg='white',fg='grey20')
dolaractual.grid(row=10,column=0,columnspan=5)

################CONFIGURACION DE APLICACION#####################

if apptheme == 'modonoche':
    modonoche()
if apptheme == 'modorosa':
    modorosa()
if apptheme == 'mododia':
    mododia()

################################################################


app.mainloop()