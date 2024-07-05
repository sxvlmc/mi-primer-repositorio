# Crear un programa en un bucle, para jugar tictactoe.
import random

def regresar_indices(numero):
    if numero > 9 or numero < 1:
        print('Tu numero es invalido')
        return None
    
    if numero <= 3:
        return [0,numero-1]
    elif numero <= 6:
        return [1, numero-4]
    elif numero <= 9:
        return [2, numero-7]

tictactoe = [[1,2,3],[4,5,6],[7,8,9]]
# 9

def imprimir_ttt(tictactoe):
    print(tictactoe[0])
    print(tictactoe[1])
    print(tictactoe[2])

def check(numero):
    indices =  regresar_indices(numero)
    if type(tictactoe[indices[0]][indices[1]]) == type('x'):
        print('Este espacio ta ocupado')
        return False
    if type(tictactoe[indices[0]][indices[1]]) == type(1):
        print('Esta espacio ta libre')
        return True


"""
funcion para checar estado de juego
Si el jugador 1 ha ganado, regresamos 1
Si el jugador 2 ha ganado, regresamos 2
Si nadie ha ganado, regresamos 0
"""
def checar_estado_de_juego(ttt, emoji_jug_1, emojis_jug_2):
    # checar filas.
    for fila in ttt:
        if fila.count(emoji_jug_1) == 3:
            return 1
        if fila.count(emojis_jug_2) == 3:
            return 2
    # checar todas las columnas
    for i in range(3):
        if (ttt[0][i] == ttt[1][i]) and (ttt[1][i] == ttt[2][i]):
            if ttt[0][i] == emoji_jug_1:
                return 1
            elif ttt[0][i] == emojis_jug_2:
                return 2
    # checar las diagonales
    if (ttt[0][0] == ttt[1][1] and ttt[1][1] == ttt[2][2]):
        if ttt[0][0] == emoji_jug_1:
            return 1
        elif ttt[0][0] == emojis_jug_2:
            return 2
    
    if (ttt[0][2] == ttt[1][1] and ttt[1][1] == ttt[2][0]):
        if ttt[1][1] == emoji_jug_1:
            return 1
        elif ttt[1][1] == emojis_jug_2:
            return 2
    return 0
def escojer_emojis():
    emojis = ['👾', '👻', '🥵', '👽', '🙈', '🌚', '😑', '😎', '😜', '😶‍🌫️']
    # indice 0 - 9
    mensaje = 'escoje tu emoji: 1:👾, 2:👻, 3:🥵, 4:👽, 5:🙈, 6:🌚, 7:😑, 8:😎, 9:😜,10:😶‍🌫️'
    # jugador 1 escoja su emoji
    indice_jugador1 = None
    indice_jugador2 = None
    emoji_jugador1 = None
    emoji_jugador2 = None

    escogio_bien_su_indice = False
    print('Para el jugador 1:')
    while (escogio_bien_su_indice == False):
        indice_jugador1 = int(input(mensaje))
        if indice_jugador1 >= 1 and indice_jugador1 <= 10:
            # el indice esta bien
            print('tu indice es correcto')
            emoji_jugador1 = emojis[indice_jugador1-1]
            escogio_bien_su_indice = True
        else:
            print('Tu indice es incorrecto, intentalo otra vez.')

    # jugador 2
    escogio_bien_su_indice = False
    print('Para el jugador 2:')
    while (escogio_bien_su_indice == False):
        indice_jugador2 = int(input(mensaje))
        if indice_jugador1 >= 1 and indice_jugador1 <= 10:
            # el indice esta bien
            
            if indice_jugador1 == indice_jugador2:
                print('El jugador 1 ya escogio ese emoji, escoje otro')
            else:
                escogio_bien_su_indice = True
                emoji_jugador2 = emojis[indice_jugador2-1]
                print('El jugador 2 escogio bien su indice.')
        else:
            print('Tu indice es incorrecto, intentalo otra vez.')

    return [emoji_jugador1, emoji_jugador2]

def jugar_computadora(ttt):
    emoji_compu = '🤖'
    # generar un numero aleatorio entre 1-9
    lugar_aleatorio = random.randint(1,9)
    while(check(lugar_aleatorio) == False):
        lugar_aleatorio = random.randint(1,9)
    # hay un lugar disponible
    indices = regresar_indices(lugar_aleatorio)
    ttt[indices[0]][indices[1]] = emoji_compu
    return emoji_compu
la_partida_sigue = True

print('Bienvenidos a tictactoe')
respondio_bien = False
oponente_computadora = False
while(respondio_bien == False):
    jugar_compu = input('Quieres jugar contra la computadora? si/no')
    if jugar_compu == 'si':
        oponente_computadora = True
        respondio_bien = True
    elif jugar_compu == 'no':
        oponente_computadora = False
        respondio_bien = True
    else:
        print('Tu respuesta no es valida. Intentalo de nuevo')
imprimir_ttt(tictactoe)
lugares = 9
emojis = escojer_emojis()
# emojis[0] <-- emoji del jugador 1
# emojis[1] <-- emoji del jugador 2
while(la_partida_sigue):
    print('Turno del jugador 1')
    imprimir_ttt(tictactoe)
    input_valido = False
    while (input_valido == False):
        lugar = int(input(f"ingresa el lugar donde quieres poner tu {emojis[0]}"))
        input_valido = check(lugar)
        if input_valido == False:
            print('Has ingresado un lugar invalido, intentalo de nuevo')
    indices = regresar_indices(lugar)
    tictactoe[indices[0]][indices[1]] = emojis[0]
    estado = checar_estado_de_juego(tictactoe, emojis[0], emojis[1])
    imprimir_ttt(tictactoe)
    if estado == 1 or estado == 2:
        la_partida_sigue = False
        print(f'Ha ganado el jugador {estado}')
        break
        
    lugares -= 1
    if lugares <= 0:
        la_partida_sigue = False
        print('Ya no hay lugares, empataron')
        break
    # checar si el oponente es la computadora.
    if oponente_computadora == False:
        print('Turno del jugador 2')
        input_valido = False
        while input_valido == False:
            lugar = int(input(f"ingresa el lugar donde quieres poner tu {emojis[1]}"))
            input_valido = check(lugar)
            if input_valido == False:
                print('Has ingresado un lugar invalido, intentalo de nuevo')
        indices = regresar_indices(lugar)
        tictactoe[indices[0]][indices[1]] = emojis[1]
        estado = checar_estado_de_juego(tictactoe, emojis[0], emojis[1])
        imprimir_ttt(tictactoe)
        if estado == 1 or estado == 2:
            la_partida_sigue = False
            print(f'Ha ganado el jugador {estado}')
            break
        lugares -= 1
        if lugares <= 0:
            la_partida_sigue = False
            print('Ya no hay lugares, empataron')
            break
    else:
        emoji_compu = jugar_computadora(tictactoe)
        estado = checar_estado_de_juego(tictactoe, emojis[0], emoji_compu)
        imprimir_ttt(tictactoe)
        if estado == 1 or estado == 2:
            la_partida_sigue = False
            print(f'Ha ganado el jugador {estado}')
            break
        lugares -= 1
        if lugares <= 0:
            la_partida_sigue = False
            print('Ya no hay lugares, empataron')
            break