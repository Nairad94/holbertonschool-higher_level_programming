#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        lst = list(tuple_a)
        lst.append(0)
        return lst
    if len(tuple_b) < 2:
        lst = list(tuple_b)
        lst.append(0)
        return lst
    if len(tuple_a) > 2:
        tuple_a[:2]
        return tuple_a
    if len(tuple_b) > 2:
        tuple_b[:2]
        return tuple_b
    new_tuple = ([a + b for a, b in (zip(tuple_a, tuple_b))])
    return new_tuple
#zip() devuelve un objeto, que es un iterador de tuplas donde el primer
#elemento de cada iterador pasado se empareja, y luego el segundo, etc
# append() se usa para agregar elementos al final de una lista
    