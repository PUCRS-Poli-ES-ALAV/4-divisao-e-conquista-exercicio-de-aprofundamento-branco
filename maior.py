def pega_maior(array):
    maior = 0
    if len(array) > 0:
        for item in array:
            if item > maior:
                maior = item
    else:
        return "array vazia"
    return maior

array = [10,3,22,54,23,12,45,6]
arrayvazia = []
print(pega_maior(array))