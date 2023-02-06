import os
clear = lambda: os.system('cls')

# Mostrar Opcions
def MostrarOpcions():
    print("""
1 -
2 -
3 -
4 -
5 -
6 -

0 - Tancar Programa
    """)


# Mostrar Missatge
def MostrarMissatge(msg):
    print(msg)
    input()



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
            print()
        elif (tecla == 2):
            print()
        elif (tecla == 3):
            print()
        elif (tecla == 4):
            print()
        elif (tecla == 5):
            print()
        elif (tecla == 6):
            print()
        elif (tecla == 0) :
            MostrarMissatge("Clica Qualsevol Tecla Per Sortir Del Programa")

