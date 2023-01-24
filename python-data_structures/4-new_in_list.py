#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
# new_list = my_list[:] es la forma slice de copiar o clonar una lista,
# o se puede usar la funcion list() o el modulo copy().
# Tambien existe el metodo incorporado list.copy() disponible desde python3
