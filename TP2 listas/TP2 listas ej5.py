#Escribir una funcion q reciba una lista como parametro y devuelva True si la lista esta ordenadda en forma ascendente
# o False en caso contrario.

def esOrdenada(lista):
  
    listaaux=list(lista)    
    listaaux.sort()
    print(lista,"original")
    print(listaaux,"auxiliar/ordenada")
    return lista==listaaux         
         
lista=["b","a","d"]        
res=esOrdenada(lista) 
print(res)

