def pedir_operador():
    operadores_validos = ['sumar', 'restar', 'multiplicar', 'dividir', 'potencia']

    el_operador_es_valido = True
    while el_operador_es_valido:
        operador = input('ingresa un operador valido (sumar, restar, multiplicar, dividir, potencia):')
        if operador in operadores_validos:
            return operador
        else:
            print('operador no valido, por favor, ingresa un operador valido')

def pedir_numero(num_id):
    return float(input(f'Ingresa el {num_id} numero: '))
def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2


def convertir_a_entero(num):
    numstr = str(num)
    #10,5
    indice = numstr.find('.')
    x = len(numstr) - indice - 1 
    multiplicador = '1'
    for i in range(x):
        multiplicador = multiplicador + '0'
    multiplicador = int(multiplicador)
    return [int(multiplicar_enteros(num, multiplicador)), multiplicador]

def multiplicar(num1, num2):
    resultado = 0
    if num1 == 0 or num2 == 0:
        resultado = 0
        return resultado
    es_negativo = False
    if num2 < 0:
        es_negativo = True 
        num2 = str(num2)
        num2 = num2.replace('-', '')
        num2 = float(num2)
        #convertir num2 a positivo
    conversion_num1 = convertir_a_entero(num1) #regresa una lista con 2 elementos
    conversion_num2 = convertir_a_entero(num2)
    resultado = multiplicar_enteros(conversion_num1[0], conversion_num2[0])
    resultado = resultado / multiplicar_enteros(conversion_num1[1], conversion_num2[1])
    if es_negativo and num1 < 0:
        resultado = str(resultado)
        resultado = resultado.replace('-', '')
        resultado = float(resultado)
    elif es_negativo and num1 > 0:
        resultado = str(resultado)
        resultado = '-' + resultado
        resultado = float(resultado)
    return resultado

def restar_hasta_que_se_pueda(numero_original, numero_para_restar):
    cantidad_de_veces_que_se_resto = 0
    while numero_original >= numero_para_restar:
        numero_original = numero_original - numero_para_restar
        cantidad_de_veces_que_se_resto = cantidad_de_veces_que_se_resto +1
    return[cantidad_de_veces_que_se_resto, numero_original]
  

def dividir(num, divisor, presicion):
    resultado = ''
    div = resultado + str(div[0])
    resultado = resultado + "."
    for i in range(presicion+1):
        div = (restar_hasta_que_se_pueda(div[1],10), divisor)
        return None

    resultado = 0
    while num1 >= num2:
        num1 -= num2
        resultado += 1

    return resultado

def potencia(num1, num2):
    resultado = 1
    for i in range (int(num2)):
        resultado = multiplicar(resultado, num2)
    return resultado    



def calcular():
    num1 = pedir_numero('primer')
    num2 = pedir_numero('segundo')
    operador = pedir_operador()
    if operador == "sumar":
        print (sumar(num1, num2))
    elif operador == "restar":
        print (restar(num1, num2))
    elif operador == 'multiplicar':
        print (multiplicar(num1, num2))
    elif operador == 'dividir':
        print (dividir(num1, num2))
    elif operador == 'potencia':
        print(potencia(num1, num2))

def calculadora():
    # Hacer una funcion para pedir al usuario que ingrese un numero
    # La funcion debe de regresar el numero ingresado por el usuario
    print('Bienvenido a la calculadora')
    el_usuario_quiere_calcular = True
    while(el_usuario_quiere_calcular):
        num1 = pedir_numero('primer')
        num2 = pedir_numero('segundo')
        operador = pedir_operador()
        resultado = calcular(num1, num2, operador)
        print(f'El resultado de {operador} {num1} y {num2} es: {resultado}')
        while(True):
            seguir = input('Quieres seguir calculando? (s/n)')
            if seguir == 'n':
                el_usuario_quiere_calcular = False
                break
            elif seguir == 's':
                break
            else:
                print('Opcion invalida, intentalo otra vez')
    return resultado



calcular()
