#escribir una funcion que reciba una lista de numeros enteros como parametro y la normalice, es decir que todos sus elementos
#deben sumar 1.0, respetando las proporciones relativas que cada elemento tiene en la lista original. Desarrollar tambien un 
#programa quie permita verificar el comportamiento de la funcion.



def normalizar_lista(lista):
    norma=sum(lista)

    for i in range(len(lista)):
        lista[i]=lista[i]/norma
    suma=sum(lista)
    print(suma)
    return lista


    

suma=normalizar_lista([1, 1, 2])

print(suma)