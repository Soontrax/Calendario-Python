# Simple calendario con tkinter
from tkinter import *
import calendar, time
import sqlite3
from tkinter import messagebox

# Funcions

def login():
    # Es conecta amb la base de dades i es crea un cursor que ens permetrà cercar, escriure,...
    db = sqlite3.connect("loginregla.db")
    c = db.cursor()
    # Es llegeixen l'usuari i la contrasenya introduïdes
    user = caixa1.get()
    passw = caixa2.get()
    # Es consula amb el cursor dins la BBDD si l'usuari i la contrasenya són correctes
    c.execute("SELECT * FROM login WHERE user = ? AND passw = ?", (user, passw))
    if c.fetchall():
        # Es realitza l'acció de login correcta
        correcto()
    else:
        # Es mostra un missatge de login incorrecte
        messagebox.showerror(title = "Login incorrecto", message = "Usuario y contraseña incorrectos")
    # Es tanca la connexió
    c.close()

def regla(i,j):
    global btn
    btn[i][j].configure(bg="red")

def introdato(fil,col,day):
    #print("El botón en la posición: ", fil-1, ", ", col+1, " corresponde a la fecha: ", day,"/",t[1],"/",t[0])
    ventana2 = Toplevel()
    ventana2.title("Menu")
    ventana2.geometry("250x250")
    ventana2.config(bg="#F5A9A9")
    etiqueta3 = Label(ventana2, text = "Regla", bg="#F5A9A9")
    etiqueta3.place(x=100, y=20)
    Button (ventana2, text = "Sí", bg="#F78181", command = lambda:regla(fil,col)).place(x=105, y=38)
    etiqueta4 = Label(ventana2, text = "Observaciones", bg="#F5A9A9")
    etiqueta4.place(x=80,y=80)
    caixa4 = Entry(ventana2)
    caixa4.place(x=60, y=110)
    
def EnviarDatos():
    db = sqlite3.connect("loginregla.db")
    c = db.cursor()
    mes = input("Dime el ultimo mes en el que te vino la regla:")
    dia = input("Dime el último dia que te vino la regla:")
    c.execute("INSERT INTO Regla (Dia, Mes) VALUES (?, ?)", (dia, mes))
    db.commit()
    c.close()
    db.close()
    print("Datos introducidos correctamente")
    menu()

def EliminarDatos():
    db = sqlite3.connect("loginregla.db")
    c = db.cursor()
    print("Has seleccionado la opcion de eliminar datos")
    borrar = input("Dime el dia que quieres eliminar:")
    c.execute('DELETE FROM Regla WHERE dia = ?',(borrar,))
    db.commit()
    c.close()
    db.close()
    print("Datos borrados correctamente")
    menu()
def ConsultarRegla():
    db = sqlite3.connect("loginregla.db")
    c = db.cursor()
    print("Has seleccionado la opcion Mostrar las últimas menstruaciones")
    c.execute("SELECT * FROM Regla")
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row)
    salir = input("Quieres seguir consultando la base de datos o salir:")
    if salir == "no":
        print("Que pases un buen dia")
        exit
    else:
        menu()
    
def btnvacio(fil,col):
    print("El botón en la posición: ", fil-1, ", ", col+1, " no corresponde a ninguna fecha")
    
def correcto():
    # Es mostra el missagte de login correcte
    messagebox.showinfo(title="Login correcte", message="Usuari i contrasenya correctes")
    # Es tanca la finestra de login
    ventana1.destroy()
    menu()
    
def salir():
        print("Gracias por visitar el calendario")
        exit
def calend():
    # Obtenemos el dia actual
    global t
    t = time.localtime()
    año = t[0]
    mes = t[1]
    dia = t[2]
    wday = t[6]
    # Averiguamos en qué posición de la semana cayó el primer día del mes
    d = int(wday+1)
    init = 7-(int(dia)-d%7)%7
    print(init)
    #Generamos el calendario mensual y lo convertimos en una lista ordenada
    c = calendar.TextCalendar()
    cstr=str(c.formatmonth(año,mes))
    partes = cstr.split()
    print(partes)
    #Creamos la ventana del calendario
    root = Tk()
    root.title("Calendario rojo")
    #definimos el número total de filas y columnas en la ventana
    nfil = 7
    ncol = 7
    #Añadimos las etiquetas del mes y el año en la primera fila
    global btn
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
    messagebox.showinfo(title = "Recordatorio", message = "Recuerda revisar regularmente la aplicación para llevar un buen control de tus periodos!")

def menu():
    print("Bienvenidas a vuestra aplicación Menstrual \n 1. Consultar Calendario \n 2. Introduce tus últimas menstruaciones \n 3. Consulta tus últimas menstruaciones \n 4. Eliminar Datos \n 5. Salir")
    opcion = input()
    if opcion == '1':
        calend()
    elif opcion == '2':
        EnviarDatos()
    elif opcion == '3':
        ConsultarRegla()
    elif opcion == '4':
        EliminarDatos()
    elif opcion == '5':
        salir()

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
