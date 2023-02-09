import os
clear = lambda: os.system('cls')

# Mostrar Opcions
def MostrarOpcions():
    print("""
1 - Mostrar Taula de Multiplicar
2 - Grafic de Notes
3 -
4 -
5 -
6 -

0 - Tancar Programa
    """)


# Mostrar Missatge
def MostrarMissatge(msg):
    print(msg, end="")
    input()
    clear()

# Taula de Multiplicar
def TaulaMultiplicar():
    linia = "X \t"
    for i in range(1, 11):
        linia = linia + str(i) + "\t"
    print(linia)

    for a in range(1,11):
        linia = f"{a} \t"
        for i in range(1,11):
            linia = linia + str(i * a) + "\t"
        print(linia)
    MostrarMissatge("Entra tecla enter per continuar")

# Gràfic de Notes
def GraficNotes():
    from tkinter import Tk, Canvas, mainloop, Button
    formatCorrecte = False
    try:
        print("Núm de alumnes que han tret Suspesos->", end="")
        suspesos = int(input())
        if (suspesos < 0 or suspesos > 1000):
            raise Exception
        print("Núm de alumnes que han tret Suficients ->", end="")
        suficients = int(input())
        if (suficients < 0 or suficients > 1000):
            raise Exception
        print("Núm de alumnes que han tret Notables->", end="")
        notables = int(input())
        if (notables < 0 or notables > 1000):
            raise Exception
        print("Núm de alumnes que han tret Excel·lents->", end="")
        excellents = int(input())
        if (excellents < 0 or excellents > 1000):
            raise Exception
        formatCorrecte = True  
    except:
        print("Error el format no és correcte, Ha de ser de 0 a 1000")

    if (formatCorrecte):
        totals = suficients + suspesos + notables + excellents
        aP = (suficients / totals) * 360
        sP1= (suspesos / totals) * 360
        nP1 = (notables / totals) * 360
        eP = (excellents / totals) * 360
        sP = sP1 + aP
        nP = sP + nP1
        coord = (100,100,500,500)
        finestra = Tk()
        canvas = Canvas(finestra, width=700, height=600)
        canvas.create_arc(coord,start = 0,extent = aP,fill ="yellow",width ="2")
        canvas.create_arc(coord,start = aP,extent = sP1,fill ="blue",width ="2")
        canvas.create_arc(coord,start = sP,extent = nP1,fill ="red",width ="2")
        canvas.create_arc(coord,start = nP,extent = eP,fill ="green",width ="2")
        canvas.create_rectangle(550,270,570,290,fill="blue",width="1")
        canvas.create_text(600,280,text="Suspesos")
        canvas.create_rectangle(550,300,570,320,fill="yellow",width="1")
        canvas.create_text(600,310,text="Suficients")
        canvas.create_rectangle(550,330,570,350,fill="red",width="1")
        canvas.create_text(600,340,text="Notables")
        canvas.create_rectangle(550,360,570,380,fill="green",width="1")
        canvas.create_text(600,370,text="Excel·lents")
        canvas.pack()
        mainloop()
    
    MostrarMissatge("Entra tecla enter per continuar")

# Main
tecla = 10
while (tecla != 0):
    correcte = False
    try:
        MostrarOpcions()
        print("Entra un número -> ", end="")
        tecla = int(input())
        if (tecla < 0 or tecla > 6) :
            raise Exception
        correcte = True
    except:
        print("Entra un enter de 0 a 6")

    if (correcte):
        clear()
        if (tecla == 1):
            TaulaMultiplicar()
        elif (tecla == 2):
            GraficNotes()
        elif (tecla == 3):
            print()
        elif (tecla == 4):
            print()
        elif (tecla == 5):
            print()
        elif (tecla == 6):
            print()
        elif (tecla == 0) :
            MostrarMissatge("Entra Tecla Enter Per Sortir Del Programa")

