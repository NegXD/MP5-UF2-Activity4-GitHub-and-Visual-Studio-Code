import os
clear = lambda: os.system('cls') # Aquest variable serà com el clear de linux, et borrarà lo que hi ha mostrat a la consola

# Mostrar Opcions
def MostrarOpcions(): # Aquest funció podrà mostrar totes les opcions del programa
    print("""
1 - Mostrar Taula de Multiplicar
2 - Grafic de Notes
3 - Calcular Dies Viscuts
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
    linia = "X \t" # Aquesta linia servirà per afegir linia en linia
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
        suspesos = int(input()) # Entrem variable de suspesos
        if (suspesos < 0 or suspesos > 1000):
            raise Exception
        print("Núm de alumnes que han tret Suficients ->", end="")
        suficients = int(input()) # Entrem variable de suficients
        if (suficients < 0 or suficients > 1000):
            raise Exception
        print("Núm de alumnes que han tret Notables->", end="")
        notables = int(input()) # Entrem variable de notables
        if (notables < 0 or notables > 1000):
            raise Exception
        print("Núm de alumnes que han tret Excel·lents->", end="")
        excellents = int(input()) # Entrem variable de excel·lents
        if (excellents < 0 or excellents > 1000):
            raise Exception
        formatCorrecte = True  
    except:
        print("Error el format no és correcte, Ha de ser de 0 a 1000")

    if (formatCorrecte): # Si format és correcte entra al if
        totals = suficients + suspesos + notables + excellents
        aP = (suficients / totals) * 360
        sP1= (suspesos / totals) * 360
        nP1 = (notables / totals) * 360
        eP = (excellents / totals) * 360
        sP = sP1 + aP
        nP = sP + nP1
        coord = (100,100,500,500) # Coordenades del diagrama
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

# Dies Viscuts
def DiesViscuts():
    from calendar import different_locale # Importem el calendar per restar dia actual amb el que has posat
    import datetime
    formatCorrecte = False
    print ("Escriu el dia que vas neixer (0-31) -> ")
    dia = int(input()) # Esperem que ens entri les variables dia, mes i any
    print ("Escriu el mes que vas neixer (0-12) -> ")
    mes = int(input())
    print ("Escriu el any que vas neixer (XXXX) -> ")
    any = int(input())
    try:
        dataNaixament = datetime.datetime (any, mes, dia) # Si ens entra coses rares salta excepció
        formatCorrecte = True
    except:
        print("Error Format Incorrecte")
    
    if (formatCorrecte): # Si el format és correcte doncs farà el IF que calcularà els dies viscuts
        dataAra = datetime.datetime.now ()
        total = dataAra - dataNaixament
        diesTotal = total.days
        segonsTotal = total.seconds
        horesTotal, segonsTotal = divmod(segonsTotal, 3600)
        minutsTotal, segonsTotal = divmod(segonsTotal, 60)

        missatge = ("En total has viscut: {} Dies, {} Hores, {} Minuts i {} Segons".format(diesTotal, horesTotal, minutsTotal, segonsTotal))
        print (missatge)
    MostrarMissatge("Entra tecla enter per continuar")

# Main
tecla = 10
while (tecla != 0):
    correcte = False
    try:
        MostrarOpcions() # Cridem la funció per que mostri els opcions
        print("Entra un número -> ", end="")
        tecla = int(input())
        if (tecla < 0 or tecla > 6) : # Esperem un numero de 0 al 6 altrament serà un Exception
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
            DiesViscuts()
        elif (tecla == 4):
            print()
        elif (tecla == 5):
            print()
        elif (tecla == 6):
            print()
        elif (tecla == 0) :
            MostrarMissatge("Entra Tecla Enter Per Sortir Del Programa")

