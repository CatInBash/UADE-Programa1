# <> \n
# Escribir una funcion diassiguiente que reciba como parametro una fecha cualquiera expresada por
# 3 enteros (correspondientes el dia mes y año) y calcule y devuelva 3 enteras correspondiente
# al dia dado Utilizando una funcion, desarrollar programas que permitan:
#     a Sumar N dias a una fecha
#     b Calcular la cantidad de dias existentes entre 2 fechas cualquiera
    
def ingreso():
    dia=int(input("ingrese dia"))
    mes=int(input("ingrese mes"))
    año=int(input("ingrese año"))
    while dia>30 or 1>mes>12:
        dia=int(input("ingrese dia"))
        mes=int(input("ingrese mes"))
        año=int(input("ingrese año"))
        
    return dia,mes,año        
        
        
        
def diassiguiente(a,b,c):
    a=a+1
    if a==31:
        a=1
        b=b+1
        if b==13:
            b=1
            c=c+1
    dia=a
    mes=b
    año=c
    
    return dia,mes,año

def main():
    dia,mes,año =ingreso()
    dias=int(input("cuantos dias quiere sumar"))  
    for i in range(dias):
    
        dia,mes,año=diassiguiente(dia,mes,año)
    
    print(dia,mes,año)
    
main()

   




