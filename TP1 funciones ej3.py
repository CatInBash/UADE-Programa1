#  <> 
# Una persona desea llevar el control de los gastos realizados
#al viajar en el subterraneo dentro de un mes . sabiendo que dicho
#medio de transporte utiliza un esquema de tarifas decrecientes.
#se solicita desarrollar una funcion q reciba como parametro la cantidad
# de viajes realizados en un determinado mes y devuelva el total de
# gastado en viajes. Realizar tambien un programa para verificar el
#comportamiento de la funcion


def ingreso():
    
    viajes= int(input("cuantos viajes realizo en el mes?"))
    while viajes <0:
        viajes= int(input("ingrese un numero valido"))
        
        
    precio= float(input("cuanto cuesta el voleto?"))
    while precio <0:
        viajes= float(input("ingrese un numero valido para el boleto"))


    return viajes, precio


def calculos(viajes, precio):
    descuento=1
    maximo=viajes*precio
    valorSinDescuento = viajes*precio
    
    if 30>=viajes>=21:
        descuento=0.8
        
    elif 40>=viajes>=31:
        descuento=0.7
        
    elif viajes>40:
        descuento=0.6
        
        
        
    total= valorSinDescuento*descuento
    descuentoPorcentual=(1-descuento)*100
    return total, descuentoPorcentual
        
        
def mostrar(viaje,precio,total,descuentoPorcentual):
    print("suy cantidad de viajes en el mes es",viaje)
    print(f"el precio del boleto es ${precio:.2f}" )
    print(f"su total incluidos descuentos es $ {total:.2f} " )
    print(f"su descuento fue del % {descuentoPorcentual:.2f}" )
    
def main():
    
    viajes, precio= ingreso()
    total,descuentoPorcentual = calculos(viajes,precio)
    mostrar(viajes,precio,total,descuentoPorcentual)
    
main()
                
    