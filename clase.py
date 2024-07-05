lista = [1,4,7,2,5,8,14,72]
print(lista)

def en_orden(lista):
    x = 0
    y = 1
    indice = len(lista) - 1

    while y <= indice:
        if lista[x] > lista[y]:
            print("La lista no está ordenada.")
            return False

        x += 1
        y += 1

    print("La lista está ordenada.")
    return True

def ordenar(lista):
    x = 0
    y = 1
    indice_max = len(lista) -1
    while en_orden(lista) == False:
        x = 0
        y = 1
        while y <= indice_max:
            try:
                if lista[x] > lista[y]:
                    temp = lista[x]
                    lista[x] = lista[y]
                    lista[y] = temp
                    print(lista)

                else:
                    print(lista)
                x += 1
                y += 1
            except IndexError:
                print(f'INDEX x {x} and y {y}')
                break

        if en_orden(lista):
            print('la lista esta ordenada')
        else:
            print('la lista no esta ordenada')
        print(lista)
ordenar(lista)


#hacer funcion de ordenar una lista usando la funcion INSERTION SORT
