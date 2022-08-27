#falta terminar demas funciones
import random
def cargarLista():
    lista=[]
    for i in range(random.randint(1,4)):
        num=random.randint(1,5)
        lista.append(num)
        
        
    return lista




def sumarElementosLista(lista):
    suma=0
    for i in range(len(lista)):
        suma+=lista[i]
        
        
    return suma,lista




def eliminarValor(valor,lista):
    for i in range(lista.count(valor)):
        
        lista.remove(valor)
        
        
        
    return lista
        
    
    
    

    

lista=cargarLista()
print(lista)
valorEliminar=int(input("ingrese un valor para eliminar de la lista"))
listaNueva=eliminarValor(valorEliminar,lista)
print(listaNueva)



        
    