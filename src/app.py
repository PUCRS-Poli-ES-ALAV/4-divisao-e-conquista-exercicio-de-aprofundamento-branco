def mergesort( array ):
    if len(array) > 1:
        meio = len(array)//2
        metade_esquerda = array[:meio]
        metade_direita = array[meio:]
        mergesort(metade_esquerda)
        mergesort(metade_direita)

        i = j = k = 0

        while i < len(metade_esquerda) and j < len(metade_direita):
            if metade_esquerda[i] < metade_direita[j]:
                array[k] = metade_esquerda[i]
                i+=1
            else:
                array[k] = metade_direita[j]
                j+=1
            k+=1
            
        while i < len(metade_esquerda):
            array[k] = metade_esquerda[i]
            i += 1
            k += 1

        while j < len(metade_direita):
            array[k] = metade_direita[j]
            j += 1
            k += 1
    return array
    


array = [9,7,12,5]
print(mergesort(array))
print(len(array[:0]))
print(len(array[0:]))



