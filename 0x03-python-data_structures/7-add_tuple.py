#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    matriz = [0, 0, 0, 0]
    i = 0
    for num in tuple_a:
        if i < 2:
            matriz[i] = num
            i += 1
    i = 2
    for num in tuple_b:
        if i < 4:
            matriz[i] = num
            i += 1
    return (matriz[0] + matriz[2], matriz[1] + matriz[3])
