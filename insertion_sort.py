def insertarNumero():
    lista=[]
    while True: 
        n=int(input('ingresa los numero en la lista (0 terminar)'))
        if  n==0:
            return lista
        else:
            lista.append(n)
def ordenar_por_insercion(lista):
    pos = 0
    i = 0
    aux = 0
    for _ in lista:
        pos = i
        aux = lista[i]
        while pos > 0 and lista [pos -1]> aux:
            lista[pos] = lista [pos-1]
            pos = pos - 1 
            lista [pos] = aux
        i = i+1
    return lista
def mostrar_lista (lista):
    for numero in lista:
        print (numero)

lista = insertarNumero()
ordenar_por_insercion(lista)
print('aqui esta tu lista ordenada')
mostrar_lista(lista)
        

