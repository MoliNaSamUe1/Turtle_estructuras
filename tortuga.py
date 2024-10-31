import turtle

def dibujarFigura(vertices, tono, pincel):
    pincel.fillcolor(tono)
    pincel.up()
    pincel.goto(vertices[0][0], vertices[0][1])
    pincel.down()
    pincel.begin_fill()
    pincel.goto(vertices[1][0], vertices[1][1])
    pincel.goto(vertices[2][0], vertices[2][1])
    pincel.goto(vertices[0][0], vertices[0][1])
    pincel.end_fill()

def calcularPuntoMedio(punto1, punto2):
    return ((punto1[0] + punto2[0]) / 2, (punto1[1] + punto2[1]) / 2)

def fractal(vertices, profundidad, pincel):
    paleta = ['purple', 'cyan', 'lime', 'gray', 'magenta', 'pink', 'brown']
    dibujarFigura(vertices, paleta[profundidad], pincel)
    if profundidad > 0:
        fractal([vertices[0],
                 calcularPuntoMedio(vertices[0], vertices[1]),
                 calcularPuntoMedio(vertices[0], vertices[2])],
                profundidad - 1, pincel)
        fractal([vertices[1],
                 calcularPuntoMedio(vertices[0], vertices[1]),
                 calcularPuntoMedio(vertices[1], vertices[2])],
                profundidad - 1, pincel)
        fractal([vertices[2],
                 calcularPuntoMedio(vertices[2], vertices[1]),
                 calcularPuntoMedio(vertices[0], vertices[2])],
                profundidad - 1, pincel)

def iniciarDibujo():
   pincel = turtle.Turtle()
   pantalla = turtle.Screen()
   puntosIniciales = [[-100, -50], [0, 100], [100, -50]]
   fractal(puntosIniciales, 3, pincel)
   pantalla.exitonclick()

iniciarDibujo()
