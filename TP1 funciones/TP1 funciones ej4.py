# <>
# un comerio de electrodomesticos necesita para su linea de cajas un programa que le
# indique al cajero el cambio que debe entregarle al cliente . para eso se ingresan 2 numeros
# enteros, correspondientes al total de la compra y al dinero recibido. Informar
# cuantos billetes de cada denominacion debe ser entregados al cliente como vuelto.
# de tal formal que se minime la cantidad de billetas . considerar que existen billetes
# de $500 $100 $50 $20 $10 $5 y $1. Emitir un mensaje de error si el dinero recibido fuera
# insuficiente . EJemplo si la compra de 317 y se abona con 500 el vuelto debe contener
# 1 bullete de $100, 1 billete de $50, 1 billete de $20, 1 billete de $10,
# y 3 billetes de $1

def ingreso():
    compra= float(input("ingrese total de la compra"))
                
    recibido=float(input("ingrese valor recibido"))
    
    while compra>recibido or compra<=0 or recibido <=0:
        print("datos invalidos")
        compra= float(input("ingrese total de la compra"))
                
        recibido=float(input("ingrese valor recibido"))
        
        
    return compra,recibido


def cajero(compra,recibido):
    vuelto=recibido-compra
    vueltoaux=vuelto
    
    billete500=int(vuelto//500)    # este operador // devuelve el cociente entero de una division
    vueltoaux=vuelto-billete500*500
    
    billete100=int(vueltoaux//100)
    vueltoaux=vueltoaux-billete100*100
    
    billete50=int(vueltoaux//50)
    vueltoaux=vueltoaux-billete50*50
    
    billete20=int(vueltoaux//20)
    vueltoaux=vueltoaux-billete20*20
    
    billete10=int(vueltoaux//10)
    vueltoaux=vueltoaux-billete10*10
    
    billete5=int(vueltoaux//5)
    vueltoaux=vueltoaux-billete5*5
    
    billete1=int(vueltoaux//1)
    
    return vuelto,billete500,billete100,billete50,billete20,billete10,billete5,billete1
    
    
    
    
def mostrar(vuelto,billete500,billete100,billete50,billete20,billete10,billete5,billete1):
    print("su vuelto es.. $",vuelto)
    if billete500!=0:
        print(f"{billete500} billetes de 500")
        
    if billete100!=0:
        print(f"{billete100} billetes de 100")
        
    if billete50!=0:
        print(f"{billete50} billetes de 50")
        
    if billete20!=0:
        print(f"{billete20} billetes de 20")
        
    if billete10!=0:
        print(f"{billete10} billetes de 10")
        
    if billete5!=0:
        print(f"{billete5} billetes de 5")
        
    if billete1!=0:
        print(f"{billete1} billetes de 1")



def main():
    compra, recibido=ingreso()
    
    vuelto,billete500,billete100,billete50,billete20,billete10,billete5,billete1=cajero(compra, recibido)
    mostrar(vuelto,billete500,billete100,billete50,billete20,billete10,billete5,billete1)
    
    
    
main()
    
    
    
        


                