# <> \n

# desarrollar una funcion que recbia como parametros dos numeros enteros positivos y devuelve
# el numero que resulte de concatenar ambos valores. por ejemplo su recibe 1234 y 567 debe devolver
# 1234567. No usar facilidades de python no vistas en clase


def ingreso():
    
    a=int(input("ingrese un valor positivo")) # los tengo q pasar como enteros para poder hacer
    b=int(input("ingrese un valor positivo"))  # la validacion
    while a<0 or b <0:
        a=int(input("ingrese un valor positivo"))
        b=int(input("ingrese un valor positivo"))
        
    
    c=str(a)
    d=str(b)
    
    return c+d



def mostrar(string):
    print(string)
    
    
def main():
    string=ingreso()
    suma=int(string)   # no lo pide el ejercio pero lo devuelvo de tipo entero luego de hacer la
    mostrar(suma)     #concatenacion
    
main()



