def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Dividir la lista en dos mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Ordenar recursivamente cada mitad
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Combinar las mitades ordenadas
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_list = []
    i = j = 0

    # Combinar los elementos de las dos listas en orden ascendente
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Agregar los elementos restantes de la lista izquierda
    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    # Agregar los elementos restantes de la lista derecha
    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list

# Ejemplo de uso
arr = [38, 27, 43, 3, 9, 82, 10 ]
print("Lista ordenada:", merge_sort(arr))
