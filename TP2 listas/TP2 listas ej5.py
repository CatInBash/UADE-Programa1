#Escribir una funcion q reciba una lista como parametro y devuelva True si la lista esta ordenadda en forma ascendente
# o False en caso contrario.

def esOrdenada(lista):
    res = True
    for i in range(len(lista)-1):
        if(lista[i]>lista[i+1]):
            res = False
            break
    return res

order_des=["c", "b", "a"]
order_as=["a", "b", "c"]

respuesta = esOrdenada(order_as)
print(order_as)
print(respuesta, "\n")

respuesta = esOrdenada(order_des)
print(order_des)
print(respuesta)


