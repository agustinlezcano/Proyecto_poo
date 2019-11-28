import sys
sys.path.append('home/agustin/Proyecto_poo/Proyecto_poo/POO')
sys.path.append('media/datos/UNCUYO/POO/PROYECTO/Respaldo_proyecto/POO')
#import robot
import math
from tiempo11 import Tiempo
from para_gotod import Orden_godot
from articulacion import Articulacion

class Trayectoria:
    def __init__(self):
        self.anguloGiro1  = 0  
        self.anguloGiro2  = 0
        self.anguloGiro3  = 0        
        #print(self.anguloGiro1, self.anguloGiro2, self.anguloGiro3)
        #self.posicion_artB[3] 
        #self.posicion_artC[3] 
        self.orden='EA+50B-130C+3P'
#print("Este es el numero de diferencia entre indices B y A" )
        #print((orden.index('B')-1)-orden.index('A'))    
    

            
            #*****************************ACA ASIGNAR LOS ANGULOS A LAS CLASES CREADAS**********************************
            #*****************************Mirar de sacar la velocidad y despues ponerla de nuevo************************
            #**********Hacer atributos a robot con todos los angulos y velocidades (EN REALIDAD ASIGNAR UNO A CADA OBJETO QUE SERÍA EL BRAZO)
        velocidad = input("Ingrese la velocidad ")      #En realidad es un argumento pasado por el cliente

    def esOrdenValida(self, x):
        valido= False
        if (x[0]=='E' and x[len(x)-1]=='P'):
            print("es cierto que hay e o p")
            if ('A' in x or 'B' in x or 'C' in x):
                #No pasa de este if
                if ((x[x.index('A')+1]=='+' or x[x.index('A')+1]=='-')  and (x[x.index('B')+1]=='+' or x[x.index('B')+1]=='-') and (x[x.index('C')+1]=='+' or x[x.index('C')+1]=='-')):
                    print("Hay un signo de + o de -")
                    if ((1<=abs((x.index('A')+1)-x.index('B'))<=4) and (1<=abs((x.index('B')+1)-x.index('C'))<=4) and (1<=abs((x.index('C')+1)-x.index('P'))<=4)):
                            # or (1<=abs(x.index('A')-x.index('C'))<=4 and (1<=(x.index('B')-x.index('C'))<=4)): # 
                        print("anda")
                        valido=True                             #obtener la salida
                        return (valido)
                    else:
                        print("Comando inválido") 
                        return(valido)            
                else:
                    print("Falta colocar los signos, vuelva a intentarlo")

                            
                            
                            #Probar de usar Catch errors          
        #diferencias entre A y B y A y C y B y C
        #luego hacer que si las posicions +2 +3 y +4 luego de la letra son numeros con un for y usando isdigit
                        #print("Acá hay una A")
                    
            #########################Funcion guardarAngulo
                    #poner rbt.RecibirOrden dentro de la clase robot
                                            # CAMBIAR W POR rbt.RecibirOrden()
    def guardarAngulo(self, orden):
                #Angulos y signos de cada orden
        self.anguloGiro1=int (orden[(orden.index('A')+1):(orden.index('B'))])
        ang1=self.anguloGiro1
        print("angulo 1 ", self.anguloGiro1)
        self.anguloGiro2=int (orden[(orden.index('B')+1):(orden.index('C'))])
        ang2=self.anguloGiro2
        print("angulo 2 ", self.anguloGiro2)
        self.anguloGiro3=int (orden[(orden.index('C')+1):(orden.index('P'))])
        ang3=self.anguloGiro3
        print("angulo 3 ", self.anguloGiro3)

        lista=[ang1, ang2, ang3]
        return(lista)
        #archivo_godot=input("Ingrese un no")
        #rgodot.generarOrden(self.anguloGiro1, self.anguloGiro2, self.anguloGiro3)

           
    
 

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
        pos2x = l2*(Trayectoria.setPosicionX(ang2))
        pos2y = l2*(Trayectoria.setPosicionY(ang2))
        pos2Z = l2*(Trayectoria.setPosicionZ(ang2))
            #Posición de la articulacion 1 en el plano
        pos3x = l3*setPosicionX(ang3)+pos2x
        pos3y = l3*setPosicionX(ang3)+pos2y


if __name__ == "__main__":
    orden='EA+40B-30C+180P'
    print(abs((orden.index('A')+1)-orden.index('B')))
    print(orden[orden.index('A')+1])
    print((orden[orden.index('B')+1]))
    prueba=Trayectoria()
    prueba.esOrdenValida(orden)
    
    if (prueba.esOrdenValida(orden)):
        print(prueba.guardarAngulo(orden))
    
    #godot= para_gotod()
    #godot.generarOrden(Trayectoria.anguloGiro1, Trayectoria.anguloGiro2, Trayectoria.anguloGiro3 )
    
    #Aca estaba el bloque de times
        prueba.setPosicionX(prueba.anguloGiro1)
        prueba.setPosicionY(prueba.anguloGiro2)
        prueba.setPosicionZ(prueba.anguloGiro3)
        #prueba.posicion(prueba.anguloGiro1,prueba.anguloGiro2,prueba.anguloGiro3)
        #mide_tiempo = Tiempo()
        #mide_tiempo.setActivityTime((prueba.anguloGiro1)*0.01)
        #mide_tiempo.setActivityTime((prueba.anguloGiro2)*0.01)
        #mide_tiempo.setActivityTime((prueba.anguloGiro3)*0.01)        
        #mide_tiempo.medirTime()
    orden2='EA+50V-130R+3P'
  
    prueba2=Articulacion()
    prueba2.esOrdenValida(orden2)
    
    if (prueba2.esOrdenValida(orden2)):
        print(prueba2.guardarAngulo(orden2))
    
        prueba2.setPosicionX(prueba2.anguloGiro1)
        prueba2.setPosicionY(prueba2.anguloGiro2)
        prueba2.setPosicionZ(prueba2.anguloGiro3)




    


