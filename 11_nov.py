from turtle import*
title('tarea')
bgcolor('black')
pencolor('white')

speed(0)
'''
def triangulo(longitud):
    for i in range(3):
        forward(longitud)
        right(120)


for i in range(10):
    triangulo(90)
    right(36)
'''

def poligonos(longitud, lados):
    for i in range(lados):
        forward(longitud)
        right(360 / lados)
poligonos(100, 6)


def espiral(lados, longitud):
    for i in range(lados):
        poligonos(longitud, i)
        right(360/lados)
espiral(9, 100) 
    
mainloop()