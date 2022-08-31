# Escribir 2 funciones separadas para imprimir por pantalla los siguientes patrones de ateriscos
# donde la cantidad de filas se recibe como parametro
# 
# 
# **********                       **
# **********                       ****
# **********                       ******
# **********                       ********
# **********                       **********


def cuadrado(filas):
    for i in range(filas):
        
        for j in range(10):
            print("*",end="" ) # este end para que los asteriscos se impriman uno al lado del otro
            
        print("\n",end="")   #este es para q no deje un salto entre cada fila
    
        
        
def triangulo(filas):
    for i in range(filas):
        for j in range(2+i*2):
            print("*", end="")
            
        print("\n",end="")   #este es para q no deje un salto entre cada fila
    

def main():
    filas= int(input("ingrese cantidad de filas"))
    cuadrado(filas)
    print("\n")
    triangulo (filas)
    
    
main()
    


