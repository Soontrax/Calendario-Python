import calendar, time
from tkinter import *
import calendar
import datetime
import sqlite3
from tkinter import messagebox

def login():
    # Es conecta amb la base de dades i es crea un cursor que ens permetrÃ  cercar, escriure,...
    db = sqlite3.connect("loginregla.db")
    c = db.cursor()
    # Es llegeixen l'usuari i la contrasenya introduÃ¯des
    user = caixa1.get()
    passw = caixa2.get()
    # Es consula amb el cursor dins la BBDD si l'usuari i la contrasenya sÃ³n correctes
    c.execute("SELECT * FROM login WHERE user = ? AND passw = ?", (user, passw))
    if c.fetchall():
        # Es realitza l'acciÃ³ de login correcta
        correcto()
    else:
        # Es mostra un missage de login incorrecte
        messagebox.showerror(title = "Login incorrecto", message = "Usuario y contraseña incorrectos")
    # Es tanca la connexiÃ³
    c.close()

def calend():
    # Es mostra el missagte de login correcte
    messagebox.showinfo(title="Login correcte", message="Usuari i contrasenya correctes")
    # Es tanca la finestra de login
    ventana1.destroy()
    # Es crea la finestra del calendari
    global ventana2
    ventana2 = Tk()
    ventana2.title("Calendario")
    ventana2.geometry("250x270")
    # Generem un menÃº
    menubar = Menu(ventana2, background="#F5A9A9")
    Arxiu = Menu(menubar)
    menubar.add_cascade(label="Periode", menu=Arxiu, background="#F5A9A9")

    Arxiu.add_command(label="Regla", command=lambda:regla())
    Arxiu.add_command(label="No regla", command=lambda:noregla())

    ventana2.config(menu=menubar)


def introdato(fil,col,day):
    print("El botón en la posición: ", fil-1, ", ", col+1, " corresponde a la fecha: ", day,"/",t[1],"/",t[0])

def btnvacio(fil,col):
    print("El botón en la posición: ", fil-1, ", ", col+1, " no corresponde a ninguna fecha")

def guardarinformacion():
    evento = input("Dime que dia tienes un evento:")
def salir():
        print("Gracias por visitar el calendario")
        exit

# Tot això es sa finestra del login del usuari y contrasenya
ventana1 = Tk()
ventana1.title("Login")
ventana1.geometry("350x150+500+250")
ventana1.config(bg="#F5A9A9")
# Es creen les etiquetes i caixes per a quÃ¨ l'usuari pugui escriure
etiqueta1 = Label(ventana1, text = "User:", bg="#F5A9A9")
etiqueta1.place(x=148, y=20)
caixa1 = Entry(ventana1)
caixa1.place(x=100, y=40)
etiqueta2 = Label(ventana1, text = "Password:", bg="#F5A9A9")
etiqueta2.place(x=135,y=60)
caixa2 = Entry(ventana1, show ="*")
caixa2.place(x=100, y=80)

# Es crea el botÃ³ de login
Button (text = "Login", bg="#F78181", command = lambda:login()).place(x=150, y=110)

# Obtenemos los valores del aÃ±o y mes a mostrar
year = datetime.date.today().year
month = datetime.date.today().month

def correcto():
    # Es mostra el missagte de login correcte
    messagebox.showinfo(title="Login correcte", message="Usuari i contrasenya correctes")
    # Es tanca la finestra de login
    ventana1.destroy()
    menu()
def calendario_resultado():
    # Obtenemos el dia actual
    global t
    t = time.localtime()
    ayo = t[0]
    mes = t[1]
    dia = t[2]
    wday = t[6]
    # Averiguamos en qué posición de la semana cayó el primer día del mes
    d = int(wday+1)
    init = 7-(int(dia)-d%7)%7
    print(init)
    #Generamos el calendario mensual y lo convertimos en una lista ordenada
    c = calendar.TextCalendar()
    cstr=str(c.formatmonth(ayo,mes))
    partes = cstr.split()
    print(partes)
    #Creamos la ventana del calendario
    root = Tk()
    root.title("Calendario")
    #definimos el número total de filas y columnas en la ventana
    nfil = 7
    ncol = 7
    #Añadimos las etiquetas del mes y el año en la primera fila
    btn = []
    Grid.rowconfigure(root,0)
    btn.append([])
    Grid.columnconfigure(root,1)
    btn[0].append(Label(root,text=partes[0]))
    btn[0][0].grid(row=0, column=1, sticky=N+S+E+W)
    Grid.columnconfigure(root,2)
    btn[0].append(Label(root,text=partes[1]))
    btn[0][1].grid(row=0, column=5, sticky=N+S+E+W)
    #Añadimos los días de la semana en la segunda fila
    Grid.rowconfigure(root,1)
    btn.append([])
    for j in range(ncol):
        Grid.columnconfigure(root, j)
        btn[1].append(Label(root,text=partes[j+2]))
        btn[1][j].grid(row=1, column=j, sticky=N+S+E+W)
    #Generamos todos los botones del calendario con el número del día impreso
    k=0    
    for i in range(2,nfil):
        Grid.rowconfigure(root, i)
        btn.append([])
        for j in range(ncol):
            Grid.columnconfigure(root, j)
            if (j<init and i==2):
                #Se crea un boton dentro de cada elemento de la matriz
                #Se pasa para cada botón creado su valor concreto de i y j como parámetro
                btn[i].append(Button(root,text="",command=lambda fil=i,col=j:btnvacio(fil,col)) )
                btn[i][j].grid(row=i, column=j, sticky=N+S+E+W)
            else:
                if (k>30):
                    #Se crea un boton dentro de cada elemento de la matriz
                    #Se pasa para cada botón creado su valor concreto de i y j como parámetro
                    btn[i].append(Button(root,text="",command=lambda fil=i,col=j:btnvacio(fil,col)) )
                    btn[i][j].grid(row=i, column=j, sticky=N+S+E+W)
                else:
                    num = str(int(partes[9+k]))
                    #Se crea un boton dentro de cada elemento de la matriz
                    #Se pasa para cada botón creado su valor concreto de i y j como parámetro
                    btn[i].append(Button(root,text=num,command=lambda fil=i,col=j,day=num:introdato(fil,col,day)) )
                    btn[i][j].grid(row=i, column=j, sticky=N+S+E+W)
                k=k+1
def menu():
    print("Bienvenidos al proyecto de Enya y Paula \n 1. Consultar Calendario \n 2. Guardar Evento \n 3. Salir")
    opcion = input()
    
    if opcion == "1":
        calendario_resultado()
    elif opcion == "2":
        guardarinformacion()
    elif opcion == "3":
        salir()
