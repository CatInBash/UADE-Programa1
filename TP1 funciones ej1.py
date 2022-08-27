#<>
# desarrollar una funcion q reciba tre numeros positivos y devuelva
# el mayor de los 3 solo si este es unico (mayor o estricto).
# en caso de no existir el mayor estricto devolver -1.
#no utilizar operadores logicos(and or not). desarrollar tambien un
#programa para ingresar los 3 valores invocar a la funcion y mostrar
#el maximo hallado , o un mensaje informativo si este no existe


def ingresar():
    
    num1=int(input("ingrese un numero"))
    while num1 <= 0:
        num1=int(input("ingrese un numero correcto"))
        
    num2=int(input("ingrese un numero"))
    while num2 <= 0:
        num2=int(input("ingrese un numero correcto"))
        
        
    num3=int(input("ingrese un numero"))
    while num3 <= 0:
        num3=int(input("ingrese un numero correcto"))
    
    return num1, num2, num3




def buscarMayor(num1,num2,num3):
    mayor=0
    if num2<num1>num3:  #es igual num2<num1 and num3<num1
        mayor = num1
    
       
    elif num1<num2>num3:
        mayor=num2
        
        
    elif num1<num3>num2:
        mayor=num3
        
    else:
        mayor=-1
        
    return mayor
        
def mostrar(mayor):
    if mayor==-1:
        print("no hay valor excluyente")
    else:
        print("el valor mas alto es el", mayor)
        
        
def main ():
    num1, num2, num3, =ingresar()
    mayor=buscarMayor(num1,num2,num3)
    mostrar(mayor)
    
main()
        
        

    
    
    
        
    
    





        
    