import turtle as tu
import docx
import re

data = docx.Document('tulips.docx')
coordinates = []
colours = []

# Procesamiento del archivo .docx para extraer datos
for para in data.paragraphs:
    # Utiliza expresiones regulares o métodos de procesamiento de texto para extraer coordenadas y colores
    # Aquí se asume un patrón específico en el archivo .docx

    # Ejemplo básico de patrones para coordenadas (ajústalos según el formato real en tu documento)
    coord_pattern = r'\((-?\d+\.?\d*), (-?\d+\.?\d*)\)'
    color_pattern = r'(\d+\.\d+)'

    coords = re.findall(coord_pattern, para.text)
    color = re.findall(color_pattern, para.text)

    if coords and color:
        coordinates.append([(float(x), float(y)) for x, y in coords])
        colours.append(tuple(float(c) for c in color))

# Dibujo con Turtle
screen = tu.Screen()
pen = tu.Turtle()
pen.speed(2)
screen.setup(width=600, height=400)  # Ajusta el tamaño de la ventana según tu preferencia

for i in range(len(coordinates)):
    pen.penup()
    pen.goto(coordinates[i][0])  # Mueve la pluma a la primera coordenada
    pen.pendown()
    pen.fillcolor(colours[i])
    pen.begin_fill()

    for coord in coordinates[i][1:]:
        pen.goto(coord)  # Dibuja líneas a las coordenadas restantes

    pen.goto(coordinates[i][0])  # Completa la figura
    pen.end_fill()

screen.mainloop()
