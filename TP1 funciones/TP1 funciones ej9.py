# <> \n
import random

naranjas=int(input("ingrese cantidad de naranjas"))
def generadorCajones(naranjas):
    pesoTotal=0
    naranjasParaJugo=0
    pesoSobrante=0
    naranja=0
    naranjaBuena=0
    isNaranjaBuena=False
    resto=naranjas%100
    auxiliarCajones=naranjas//100
    cantidadCajones=0
    
    for i in range(naranjas):
        
        pesoNaranja=random.randint(150,350)
    
    
        if pesoNaranja >=200 and pesoNaranja <=300:
            naranjaBuena +=1
            pesoTotal+=pesoNaranja
                 
        else:
            naranjasParaJugo +=1
        
        
    cajones=naranjaBuena//100
    resto=naranjaBuena%100
        
        
        
        
    
        
        
 
            
        
        
    
    

        
        
    
       
                
  #return(pesoTotal,naranjasParaJugo,pesoSobrante,naranjasSobrante)
    return cajones, resto,pesoTotal/1000
    

print(generadorCajones(naranjas))

