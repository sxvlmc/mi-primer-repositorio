use = True

while(use):
    print('*Anciano* Hola viajero no te habia visto por aqui, cuenta la leyenda que si escibes un tipo de operacion y dos numeros en esta piedra, se resolveran tus dudas')
    primer_numero = None
    segundo_numero = None
    numero_incorrecto = True
    incorrecto = True  
    Escribe_tu_nombre = True
    
    while(Escribe_tu_nombre):
        Nombre = input("*Anciano* Viajero me podrias decir tu nombre: ")
        print("*Anciano* !Hola¡ " + str(Nombre))
        Escribe_tu_nombre = False
   
    while(incorrecto):
        respuesta = input("*Piedra* Los escuche mientras hablaban uuuuuuuuuucofcof yo soy la piedra magica, elige una operacion y tus deseos seran consedidos: +, -, *, /, ^: ")
        if (respuesta == '+' or respuesta == '-' or respuesta == '*' or respuesta == '/' or respuesta == '^'):
            if  respuesta == '+':
                print("*Piedra* " + str(Nombre) + ' Has elegido la antigua suma')
                Nombre_de_operacion = "suma magica"
                Tipo_de_operacion = "+"
            elif respuesta == '-':
                print("*Piedra* " + str(Nombre) + ' Has elegido la antigua restar')
                Nombre_de_operacion = "resta magica"
                Tipo_de_operacion = "-"
            elif respuesta == '*':
                print("*Piedra* " + str(Nombre) + ' Has elegido la antigua multiplicacion')
                Nombre_de_operacion = "multiplicacion magica"
                Tipo_de_operacion = "*"
            elif respuesta == '/':
                print("*Piedra* " + str(Nombre) + ' Has elegido la antigua divicion')
                Nombre_de_operacion = "divicion magica"
                Tipo_de_operacion = "/"
            elif respuesta == '^':
                print("*Piedra* " + str(Nombre) + ' Has elegido la antigua exponenciacion ')
                Nombre_de_operacion = "exponeciacion magica"
                Tipo_de_operacion = "^"
            print('*Piedra* has elegido ' + respuesta)
            incorrecto = False
        else:
            print("*Piedra* " + str(Nombre) + " UUUUUUUUU No es una operacion valida. reeintentalo.")
   
    # bucle atinar numero
    # si el usuario no nos da el numero correcto, el usuario se queda en el bucle.
    while(numero_incorrecto):
        print("*Piedra* " + 'provee el primer numero magico')
        res = input("*Piedra* " + str(Nombre) + ' escribe tu numero magico: ')
        # checamos si la respuesta es numerica
        if res.isnumeric():
            si_no_invalido = True
            while(si_no_invalido):
                # la respuesta es numerica
                print("*Piedra* ¿es correcto este numero magico?")
                res_s_n = input('S/N: ')
                res_s_n = res_s_n.lower()
                if res_s_n == 'n' or res_s_n == 'no':
                    # repetimos este bucle
                    si_no_invalido = False
                    numero_incorrecto = True
                    print('*Piedra* okey')
                elif res_s_n == 's' or res_s_n == 'si':
                    # esta bien la respuesta
                    primer_numero = int(res)
                    si_no_invalido = False
                    numero_incorrecto = False

                else:
                    print("*Piedra* " + str(Nombre) + ' uuuuuuuuu no es un numero magico, Humano tonto')
        else:
            print("*Piedra* " + str(Nombre) + ' uuuuuuuu Tu respuesta no es un numero magico, Humano tonto')
    numero_incorrecto = True
    while(numero_incorrecto):
        print("*Piedra* " + "provee el segundo numero magico")
        res = input("*Piedra* " + str(Nombre) + ' escribe tu numero magico: ')
        # checamos si la respuesta es numerica
        if res.isnumeric():
            si_no_invalido = True
            while(si_no_invalido):
                # la respuesta es numerica
                print('*Piedra* es correcto este numero magico?')
                res_s_n = input('S/N: ')
                res_s_n = res_s_n.lower()
                if res_s_n == 'n' or res_s_n == 'no':
                    # repetimos este bucle
                    print('*Piedra* uuuuuuuucofcof okey')
                    si_no_invalido = False
                    numero_incorrecto = True
                elif res_s_n == 's' or res_s_n == 'si':
                    # esta bien la respuesta
                    segundo_numero = int(res)
                    si_no_invalido = False
                    numero_incorrecto = False

                else:
                    print("*Piedra* " + str(Nombre) + ' no es un numero magico. Humano tonto')
        else:
            print("*Piedra* " + str(Nombre) + ' tu respuesta no es un numero magico, Humano tonto')
    
    incorrecto = True 
    while(incorrecto):
        if Tipo_de_operacion == "+":
            calculacion = primer_numero + segundo_numero
            Nombre_de_operacion = "suma magica"
        if Tipo_de_operacion == "-":
            calculacion = primer_numero - segundo_numero
            Nombre_de_operacion = "resta magica"
        if Tipo_de_operacion == "*":
            calculacion = primer_numero * segundo_numero
            Nombre_de_operacion = "multiplicacion magica"
        if Tipo_de_operacion == "/":
            calculacion = primer_numero / segundo_numero
            Nombre_de_operacion = "divicion magica"
        if Tipo_de_operacion == "^":
            calculacion = primer_numero ** segundo_numero
            Nombre_de_operacion = "exponenciacion magica"
    
        print(str(Nombre) + ' El resultado de la ' + str(Nombre_de_operacion) + (" es ") + str(primer_numero) + str(Tipo_de_operacion) + str(segundo_numero) + ' igual a ' + str(calculacion))
        incorrecto = False
    res = input('*Piedra* quieres salir de la calculadora magica? \' S/N \': ')
    if res == 's' or res == "si":
        print ("*Piedra* ¡Adios!" + str(Nombre))
        use = False 