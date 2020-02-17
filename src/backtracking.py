def permutacao(list, lista):
    if list == 1:
        return lista
    else:
        return [ y + x
                for y in permutacao(1, lista)
                for x in permutacao(list - 1, lista)
                ]