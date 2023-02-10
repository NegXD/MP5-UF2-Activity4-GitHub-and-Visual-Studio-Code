
import os
clear = lambda: os.system('cls')

# Mostrar Opcions
def MostrarOpcions():
    print("""
1 -
2 -
3 -
4 - Dibuixar un among us
5 - Dibuixar el logo de Avengers
6 - Un figura de colors 

0 - Tancar Programa
    """)


# Mostrar Missatge
def MostrarMissatge(msg):
    print(msg)
    input()

# cercle
def cercle():
    import turtle
    rango = 0 #vueltas
    puntas = 0 #puntas de final
    rotasion = 0 # 0grado
    formatCorrecte = False
    try:
        print("""
        Ajustes por defecto:
        rango = 600 | el max = 1000
        puntas = 10 | el max = 40
        rotasion = 777 | el max = 1000
        
        Canvia de configuracio si vols
        """)
        
        rango = (input("Entra un rang -->"))
        puntas = (input("Entra un puntas -->"))
        rotasion = (input("Entra un rotasion -->"))
        if(rango == ""):
            rango = 600
        if(puntas == ""):
            puntas = 10
        if(rotasion == ""):
            rotasion = 777
        rango = int(rango)
        puntas = int(puntas)
        rotasion = int(rotasion)
        if (rango > 1000 or puntas > 40 or rotasion > 1000 or rango < 0 or puntas < 0 or rotasion < 0):
            raise Exception
        formatCorrecte = True
    except:
        print("Error")
    if(formatCorrecte):
        turtle.hideturtle()
        t = turtle.Turtle()
        t.speed(100) #la velocitat
        turtle.bgcolor('black')
        color=('steelblue','coral','magenta','palegreen')
        for i in range(rango):
            t.pencolor(color[i%4])
            t.rt(i)
            t.circle(puntas,i)
            t.fd(i)
            t.rt(rotasion)
        t.end_fill()
        turtle.exitonclick()
        MostrarMissatge("Entra tecla enter per continuar")


# Avengers
def Avengers():
    import turtle
    s = turtle.getscreen()
    t = turtle.Turtle()
    turtle.bgcolor('black')
    def draw_circle():
        # circle gran
        t.setposition(0, -280)
        t.pendown()
        t.begin_fill()
        t.color('red')
        t.pencolor('white')
        t.circle(300)
        t.end_fill()
        t.penup()
    def draw_circle2():
        # circle petit
        t.pensize(2)
        t.setposition(0, -230)
        t.pendown()
        t.begin_fill()
        t.color('black')
        t.circle(250)
        t.end_fill()
        t.penup()
    def draw_A():
        # letra ‘A’
        t.setposition(30, -110)
        t.pendown()
        t.begin_fill()
        t.color('red')
        t.pensize(10)
        t.pencolor('white')
        t.forward(23)
        t.backward(123)
        t.left(60)
        t.backward(220)
        t.right(60)
        t.backward(100)
        t.right(117)
        t.backward(710)
        t.right(63)
        t.backward(110)
        t.right(90)
        t.backward(510)
        t.right(90)
        t.backward(100)
        t.right(90)
        t.backward(70)
        t.end_fill()
        t.penup()
    def draw_triangle():
        # Triangle dentro de ‘A’ 
        t.pensize(10)
        t.setposition(53, -40)
        t.pendown()
        t.begin_fill()
        t.color('black')
        t.pencolor('white')
        t.right(90)
        t.forward(100)
        t.right(115)
        t.forward(250)
        t.right(157)
        t.forward(227)
        t.end_fill()
        
    def draw_arrow():
        # flecha dentro de ‘A’ i triangle
        t.backward(80)
        t.left(42)
        t.forward(147)
        t.right(83)
        t.forward(140)
    
    draw_circle()
    draw_circle2()
    draw_A()
    draw_triangle()
    draw_arrow()

    t.screen.exitonclick()
    MostrarMissatge("Entra tecla enter per continuar")

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

        
        def body():
            
            """ draws the body """
            t.pensize(20)
            #t.speed(15) es la velositat de la flecha
            turtle.hideturtle()
            t.fillcolor(BODY_COLOR)
            t.begin_fill()

            # sitio de derecha 
            t.right(90)
            t.forward(50)
            t.right(180)
            t.circle(40, -180)
            t.right(180)
            t.forward(200)

            # cabesa curve
            t.right(180)
            t.circle(100, -180)

            # sitio de esquera
            t.backward(20)
            t.left(15)
            t.circle(500, -20)
            t.backward(20)

            #t.backward(200)
            t.circle(40, -180)
            #t.right(90)
            t.left(7)
            t.backward(50)

            # cadera
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
            Amongus()
        elif (tecla == 5):
            Avengers()
        elif (tecla == 6):
            cercle()
        elif (tecla == 0) :
            MostrarMissatge("Clica Qualsevol Tecla Per Sortir Del Programa")

