#Escribir una funcion q reciba una lista como parametro y devuelva True si la lista esta ordenadda en forma ascendente
# o False en caso contrario.

import random

def esOrdenada(lista):
    res = True
    for i in range(len(lista)-1):
        if(lista[i]>lista[i+1]):
            res = False
            break
    return res


def crearLista():
    lista = []
    for i in range(5):
        lista.append(random.randint(0, 20))
    return lista

myList = crearLista()
respuesta = esOrdenada(myList)
print(myList)
print(respuesta)
