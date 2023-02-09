import os
clear = lambda: os.system('cls')

# Mostrar Opcions
def MostrarOpcions():
    print("""
1 -
2 -
3 -
4 - Dibuixar un among us
5 -
6 -

0 - Tancar Programa
    """)


# Mostrar Missatge
def MostrarMissatge(msg):
    print(msg)
    input()

# Amongus
def Amongus():
    print("Anem a dibuixar un among us!!!")
    print("Sisplau posa un color que vols el among us. !!Alerta en cas que no entris res o t'equivoquis en llentras el color sera perdefecte white!!")
    import turtle

    formatCorrecte = False
    BODY_COLOR =  'white'
    BODY_SHADOW = ''
    GLASS_COLOR = '#9acedc'
    GLASS_SHADOW = ''
    print("Color --->",end="")
    try:
        BODY_COLOR = str(input())
        formatCorrecte = True
    except:
        print("Error")

    if(formatCorrecte):
        s = turtle.getscreen()
        t = turtle.Turtle()

        # it can move forward backward left right
        def body():
            """ draws the body """
            t.pensize(20)
            #t.speed(15)
            turtle.hideturtle()
            t.fillcolor(BODY_COLOR)
            t.begin_fill()

            # right side
            t.right(90)
            t.forward(50)
            t.right(180)
            t.circle(40, -180)
            t.right(180)
            t.forward(200)

            # head curve
            t.right(180)
            t.circle(100, -180)

            # left side
            t.backward(20)
            t.left(15)
            t.circle(500, -20)
            t.backward(20)

            #t.backward(200)
            t.circle(40, -180)
            #t.right(90)
            t.left(7)
            t.backward(50)

            # hip
            t.up()
            t.left(90)
            t.forward(10)
            t.right(90)
            t.down()
            #t.right(180)
            #t.circle(25, -180)
            t.right(240)
            t.circle(50, -70)

            t.end_fill()


        def glass():
            turtle.hideturtle()
            t.up()
            #t.right(180)
            t.right(230)
            t.forward(100)
            t.left(90)
            t.forward(20)
            t.right(90)

            t.down()
            t.fillcolor(GLASS_COLOR)
            t.begin_fill()

            t.right(150)
            t.circle(90, -55)

            t.right(180)
            t.forward(1)
            t.right(180)
            t.circle(10, -65)
            t.right(180)
            t.forward(110)
            t.right(180)
            
            #t.right(180)
            t.circle(50, -190)
            t.right(170)
            t.forward(80)

            t.right(180)
            t.circle(45, -30)

            t.end_fill()

        def backpack():
            turtle.hideturtle()
            t.up()
            t.right(60)
            t.forward(100)
            t.right(90)
            t.forward(75)

            t.fillcolor(BODY_COLOR)
            t.begin_fill()

            t.down()
            t.forward(30)
            t.right(255)

            t.circle(300, -30)
            t.right(260)
            t.forward(30)

            t.end_fill()


        body()
        glass()
        backpack()

        t.screen.exitonclick()
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

