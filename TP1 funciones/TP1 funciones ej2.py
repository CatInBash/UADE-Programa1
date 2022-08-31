#  <> 
#desarrollar una funcion que reciba 3 numetors enteros positivos
# y verifique si corresponden a una fecha valida (dia mes año)
# devolver True oFalse segun la fecha sea correcta o no .
#Realizar tambiien un programa para verificar comportamiento
#de la funcion


def cargarFecha():
    
    dia=int(input("ingrese dia"))
    while dia<0:
        dia=int(input("ingrese dia positivo"))
        
    mes=int(input("ingrese mes"))
    while mes<0:
        mes=int(input("ingrese mes positivo"))
        
    año=int(input("ingrese año"))
    while año<0:
        año=int(input("ingrese año positivo"))
        
    return dia, mes, año
    
   


def validar(dia,mes,año):
    diaFlag=False
    mesFlag=False
    añoFlag=False
    if 30>=dia>=1:
         diaFlag=True
         
        
    if 12>=mes>=1:
         mesFlag=True
         
    
    if 3000>=año>=1900:
         añoFlag=True
         
    return diaFlag, mesFlag, añoFlag
         
         
         
def validarMensaje(diaFlag, mesFlag, añoFlag):
    if diaFlag and mesFlag and añoFlag:
        print("las fechas son correctas")
        return True
        
        
    else:
        print("las fechas son incorrectas")
        return False
    
    
    
    





def main():
    dia, mes, año= cargarFecha()
    diaFlag, mesFlag, añoFlag=validar(dia, mes, año)
    flagMain=validarMensaje(diaFlag,mesFlag,añoFlag)
    if flagMain:
        print(dia, mes , año)
        
        
    
    
    
main()
    
    
    
    

    