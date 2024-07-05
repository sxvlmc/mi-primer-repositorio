from turtle import*
title('tarea')
bgcolor('black')
pencolor('white')

speed(0)
def dibujar_hexagono(longitud):
    forward(longitud)
    right(120)
    for i in range(6):
        forward(longitud)
        right(120)
        forward(longitud)
        backward(longitud)
        left(60)
    right(60)
    forward(longitud)
    left(180)
for i in range(9):
    dibujar_hexagono(200 + i*3)
    right(3)
    



dibujar_hexagono()


mainloop()