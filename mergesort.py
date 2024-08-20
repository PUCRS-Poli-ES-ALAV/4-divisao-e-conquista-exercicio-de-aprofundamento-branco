def mergesort(array):
    if len(array) > 1:
        indice_metade = len(array) // 2
        metade_esquerda = array[:indice_metade]
        metade_direita = array[indice_metade:]
        mergesort(metade_esquerda)
        mergesort(metade_direita)

        i = 0
        j = 0
        k = 0

        while i < len(metade_esquerda) and j < len(metade_direita):
            if metade_esquerda[i] < metade_direita[j]:
                array[k] = metade_esquerda[i]
                i += 1
            else:
                array[k] = metade_direita[j]
                j += 1
            k += 1
        
        while i < len(metade_esquerda):
            array[k] = metade_esquerda[i]
            i += 1
            k += 1

        while j < len(metade_direita):
            array[k] = metade_direita[j]
            j += 1
            k += 1


        
    return array

array = [13, 5, 22, 2, 1, 6]
print(mergesort(array))