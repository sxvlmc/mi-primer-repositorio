import turtle

# Configuración de la pantalla y la tortuga
wn = turtle.Screen()
wn.title("Gracias con Turtle")
wn.bgcolor("white")

pen = turtle.Turtle()
pen.color("black")
pen.pensize(3)
pen.speed(2)

# Función para dibujar la letra 'G'
def draw_G():
    pen.penup()
    pen.goto(-300, 0)
    pen.pendown()
    pen.circle(50, 270)
    pen.setheading(180)
    pen.forward(50)
    pen.penup()
    pen.goto(-200, 0)
    pen.pendown()

# Función para dibujar la letra 'r'
def draw_r():
    pen.setheading(90)
    pen.forward(100)
    pen.right(90)
    pen.circle(25, 180)
    pen.setheading(270)
    pen.forward(50)
    pen.penup()
    pen.goto(-130, 0)
    pen.pendown()

# Función para dibujar la letra 'a'
def draw_a():
    pen.penup()
    pen.goto(-100, -50)
    pen.pendown()
    pen.setheading(60)
    pen.forward(100)
    pen.right(120)
    pen.forward(100)
    pen.right(180)
    pen.forward(50)
    pen.right(120)
    pen.forward(50)
    pen.penup()
    pen.goto(-40, 0)
    pen.pendown()

# Función para dibujar la letra 'c'
def draw_c():
    pen.penup()
    pen.goto(-20, 50)
    pen.pendown()
    pen.circle(50, 180)
    pen.penup()
    pen.goto(10, 0)
    pen.pendown()

# Función para dibujar la letra 'i'
def draw_i():
    pen.penup()
    pen.goto(30, 0)
    pen.pendown()
    pen.setheading(90)
    pen.forward(100)
    pen.penup()
    pen.goto(30, 120)
    pen.pendown()
    pen.dot(10)
    pen.penup()
    pen.goto(60, 0)
    pen.pendown()

# Función para dibujar la letra 'a'
def draw_a2():
    pen.penup()
    pen.goto(60, -50)
    pen.pendown()
    pen.setheading(60)
    pen.forward(100)
    pen.right(120)
    pen.forward(100)
    pen.right(180)
    pen.forward(50)
    pen.right(120)
    pen.forward(50)
    pen.penup()
    pen.goto(120, 0)
    pen.pendown()

# Función para dibujar la letra 's'
def draw_s():
    pen.penup()
    pen.goto(140, 50)
    pen.pendown()
    pen.circle(30, 180)
    pen.right(180)
    pen.circle(30, -180)
    pen.penup()
    pen.goto(150, 0)
    pen.pendown()

# Función para dibujar la palabra "Gracias"
def draw_gracias():
    draw_G()
    draw_r()
    draw_a()
    draw_c()
    draw_i()
    draw_a2()
    draw_s()

# Llamar a la función para dibujar "Gracias"
draw_gracias()

# Finalizar el dibujo
pen.hideturtle()
wn.mainloop()

