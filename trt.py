from turtle import*
title('tarea')
bgcolor('black')
pencolor('white')
'''
speed(0)
forward(100)
pencolor('red')
right(90)
forward(100)
pencolor('green')
right(90)
forward(100)
pencolor('blue')
right(90)
forward(100)
pencolor('white')
right(90)
forward(100)
'''

'''
forward(100)
left(120)
pencolor('green')
forward(100)
left(120)
pencolor('red')
forward(100)
'''
'''
backward(100)
right(90)
forward(100)
left(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
backward(100)
right(120)
forward(235)
right(120)
forward(235)
left(200)
pencolor('black')
forward(200)
right(140)
pencolor('white')
forward(150)
left(90)
forward(75)
backward(200)
right(90)
forward(150)
left(90)
forward(200)
right(90)
pencolor('black')
forward(25)
right(90)
pencolor('white')
forward(200)
left(90)
forward(130)
'''
'''
setup(600, 600)
speed(0)
width(6)
for i in range(110):
    forward(i * 5)
    right(90)
Screen().exitonclick()
'''
'''
def cuadrado(longitud):
    for i in range(4):
        forward(longitud)
        right(90)
cuadrado(30)
'''
'''
def triangulo(longitud):
    for i in range(3):
        forward(longitud)
        right(120)
triangulo(30)
'''
'''
speed(0)
def triangulo(longitud):
    for i in range(3):
        forward(longitud)
        right(180)


for i in range(6):
    triangulo(120)
    right(36)
'''

speed(0)


def dibujar_hexagono(longitud):
    forward(100)
    right(120)
    forward(100)
    right(120)
    forward(100)
    backward(100)
    left(60)
    forward(100)
    right(120)
    forward(100)
    backward(100)
    left(60)
    forward(100)
    right(120)
    forward(100)
    backward(100)
    left(60)
    forward(100)
    right(120)
    forward(100)
    backward(100)
    left(60)
    forward(100)
    right(120)
    forward(100)
    backward(100)
    left(60)
    forward(100)
    right(120)
    forward(100)

    for i in range(9):
        forward(longitud, i)
        right(3)
dibujar_hexagono(50)





dibujar_hexagono()


'''
speed(0)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
backward(100)
right(45)
forward(141.42)
backward(70.71)
right(90)
forward(70.71)
backward(70.71)
left(45)
forward(50)
left(120)
forward(35.35)
right(120)
forward(25)
'''
'''
def triangulo(longitud):
    for i in range(18):
        forward(longitud + i)
        right(60)
triangulo(100)
'''




mainloop()