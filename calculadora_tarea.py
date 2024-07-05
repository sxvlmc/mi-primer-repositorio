def pedir_operador():
    operadores_validos = ['sumar', 'restar', 'multiplicar', 'dividir', 'potencia']
    while True:
        operador = input('Ingresa un operador válido (sumar, restar, multiplicar, dividir, potencia): ')
        if operador in operadores_validos:
            return operador  
        else:
            print('Operador no válido, por favor, ingresa un operador válido.')

def pedir_numero(num_id):
    return float(input(f'Ingresa el {num_id} número: '))

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    resultado = 0
    for i in range(int(num2)):
        resultado += num1
    return resultado

def dividir(num1, num2):
    if num2 == 0:
        print("No puedes dividir por cero.")
        return None
    resultado = num1
    while resultado >= num2:
        resultado -= num2
    return resultado

def potencia(num1, num2):
    resultado = 1
    for _ in range(int(num2)):
        resultado = multiplicar(resultado, num1)
    return resultado

def calcular():
    num1 = pedir_numero('primer')
    num2 = pedir_numero('segundo')
    operador = pedir_operador()

    if operador == 'sumar':
        resultado = sumar(num1, num2)
    elif operador == 'restar':
        resultado = restar(num1, num2)
    elif operador == 'multiplicar':
        resultado = multiplicar(num1, num2)
    elif operador == 'dividir':
        resultado = dividir(num1, num2)
        if resultado is None:
            return
    elif operador == 'potencia':
        resultado = potencia(num1, num2)
    else:
        print('Operador no reconocido') 
        return

    print(f'Resultado: {resultado}')

calcular()
