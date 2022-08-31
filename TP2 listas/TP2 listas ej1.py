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
        
def capicua(lista):
    final=-1
    bandera = True
    
    for i in range(len(lista)):
        if(lista[i] != lista[final]):
            bandera = not(bandera)
            break
        else:
            final-=1
            
    if(bandera): print("Es capicua")
    else: print("No es capicua")
        
    
lista=cargarLista()
print(lista)
valorEliminar=int(input("ingrese un valor para eliminar de la lista"))
listaNueva=eliminarValor(valorEliminar,lista)
print(listaNueva)
ejemploListaCapicua = [50, 17, 91, 17, 50]
capicua(ejemploListaCapicua)



        
    