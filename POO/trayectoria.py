import sys
sys.path.insert(0, 'home/agustin/Proyecto_poo/Proyecto_poo/POO')
sys.path.insert(0, 'media/datos/UNCUYO/POO/PROYECTO/Respaldo_proyecto/POO')
#from robot import Robot
import math
from tiempo11 import Tiempo
#from para_gotod import Orden_godot

class Trayectoria:
    def __init__(self):
        self.anguloGiro1=0
        self.anguloGiro2=0
        self.anguloGiro3=0  
#        self.posicion_artB[3] 
#        self.posicion_artC[3]    
    
    def guardarAngulo(self, orden):
                #Angulos y signos de cada orden
        self.anguloGiro1=int (orden[(orden.index('A')+1):(orden.index('B'))])
        print("angulo 1 ", self.anguloGiro1)
        self.anguloGiro2=int (orden[(orden.index('B')+1):(orden.index('C'))])
        print("angulo 2 ", self.anguloGiro2)
        self.anguloGiro3=int (orden[(orden.index('C')+1):(orden.index('P'))])
        print("angulo 3 ", self.anguloGiro3)

        #rgodot.generarOrden(self.anguloGiro1, self.anguloGiro2, self.anguloGiro3)


        #Tiempo.setActivityTime(Trayectoria.anguloGiro1*0.01)
        #Tiempo.setActivityTime(Trayectoria.anguloGiro2*0.01)
        #Tiempo.setActivityTime(Trayectoria.anguloGiro3*0.01)
             
        #Tiempo.medirTime()
        #posicion(self.anguloGiro1,self.anguloGiro2,self.anguloGiro3)

    def esOrdenValida(self, x):
        valido= False
        if (x[0]=='E' and x[len(x)-1]=='P'):
            if ('A' in x or 'B' in x or 'C' in x):
                if ((x[x.index('A')+1]=='+' or x[x.index('A')+1]=='-')  and (x[x.index('B')+1]=='+' or x[x.index('B')+1]=='-') and (x[x.index('C')+1]=='+' or x[x.index('C')+1]=='-')):
                    if ((1<=abs((x.index('A')+1)-x.index('B'))<=4) and (1<=abs((x.index('B')+1)-x.index('C'))<=4) and (1<=abs((x.index('C')+1)-x.index('P'))<=4)):
                        funcion=Trayectoria()
                        funcion.guardarAngulo(x)
                        valido=True
                        return (valido)
                    else:
                        print("Comando inválido") 
                        return(valido)
                else:
                    print("Se deben colocar los signos, vuelva a intentarlo")            
    

#si no anda el AnguloGiro usar ang1 ang2 y ang3 
    def setPosicionX(self, anguloGiro1):
            #Obtengo la posición en X del brazo
            #Primero paso el ángulo a radianes (por la librería)

        return(math.cos(math.radians(anguloGiro1)))

    def setPosicionY(self, anguloGiro2):
            #Obtengo la posición en Y del brazo
            #Primero paso el ángulo a radianes (por la librería)

        return(math.cos(math.radians(anguloGiro2)))   

    def setPosicionZ(self, anguloGiro3):
            #Obtengo la posición en Y del brazo
            #Primero paso el ángulo a radianes (por la librería)

        return(math.cos(math.radians(anguloGiro3)))       
        
        #Acá abajo en vez de pasar una longitud estática se debe hacer con el atributo tamaño del robot
        #Lo hago con un def y un set_tamaño
        #También con un solo argumento ángulo alcanza. Se llama a los atributos de cada objeto
    def posicion(self, ang1, ang2, ang3):
            #longitudes de cada articulación
        l1=10 
        l2=5 
        l3=4.5
            #Posición del brazo A en el plano
        pos1x = 0
        pos1y = 0
        pos1z=0
            #Posición de la articulacion 1 en el plano
        pos2x = l2*Trayectoria.setPosicionX(ang2)
        pos2y = l2*Trayectoria.setPosicionY(ang2)
        pos2Z = l2*Trayectoria.setPosicionZ(ang2)
            #Posición de la articulacion 1 en el plano
        pos3x = l3*setPosicionX(ang3)+pos2x
        pos3y = l3*setPosicionX(ang3)+pos2y







    


