import sys
sys.path.insert(0, 'home/agustin/Proyecto_poo/Proyecto_poo/POO')
sys.path.insert(0, 'media/datos/UNCUYO/POO/PROYECTO/Proyecto_poo/POO')
import robot
import math
import tiempo as Tiempo
import para_gotod as rgodot

class Trayectoria:
    def __init__(self):
        self.anguloGiro[0]=0
        self.anguloGiro[1]=0
        self.anguloGiro[2]=0  
        self.posicion_artB[3] 
        self.posicion_artC[3] 
        self.orden='EA+50B-130C+3P'
#print("Este es el numero de diferencia entre indices B y A" )
        #print((orden.index('B')-1)-orden.index('A'))    
    
    def guardarAngulo(self, orden):
                #Angulos y signos de cada orden
        self.anguloGiro[0]=int (orden[(orden.index('A')+1):(orden.index('B'))])
        print("angulo 1 ", self.anguloGiro[0])
        self.anguloGiro[1]=int (orden[(orden.index('B')+1):(orden.index('C'))])
        print("angulo 2 ", self.anguloGiro[1])
        self.anguloGiro[2]=int (orden[(orden.index('C')+1):(orden.index('P'))])
        print("angulo 3 ", self.anguloGiro[2])

            #archivo_godot=input("Ingrese un no")
        rgodot.generarOrden(self.anguloGiro[0], self.anguloGiro[1], self.anguloGiro[2])


        Tiempo.setActivityTime(self.anguloGiro[0]*0.01)
        Tiempo.setActivityTime(self.anguloGiro[1]*0.01)
        Tiempo.setActivityTime(self.anguloGiro[2]*0.01)
             
        Tiempo.medirTime()
        posicion(self.anguloGiro[0],self.anguloGiro[1],self.anguloGiro[2])
            
            #*****************************ACA ASIGNAR LOS ANGULOS A LAS CLASES CREADAS**********************************
            #*****************************Mirar de sacar la velocidad y despues ponerla de nuevo************************
            #**********Hacer atributos a robot con todos los angulos y velocidades (EN REALIDAD ASIGNAR UNO A CADA OBJETO QUE SERÍA EL BRAZO)
        velocidad = input("Ingrese la velocidad ")      #En realidad es un argumento pasado por el cliente

    def esOrdenValida(self, x):
        valido= False
        if (x[0]=='E' and x[len(x)-1]=='P'):
            print("es cierto que hay e o p")
            if ('A' in x or 'B' in x or 'C' in x):
                if ((x[x.index('A')+1]=='+' or x[x.index('A')+1]=='-')  and (x[x.index('B')+1]=='+' or x[x.index('B')+1]=='-') and (x[x.index('C')+1]=='+' or x[x.index('C')+1]=='-')):
                    print("Hay un signo de + o de -")
                    if ((1<=abs((x.index('A')+1)-x.index('B'))<=4) and (1<=abs((x.index('B')+1)-x.index('C'))<=4) and (1<=abs((x.index('C')+1)-x.index('P'))<=4)):
                            # or (1<=abs(x.index('A')-x.index('C'))<=4 and (1<=(x.index('B')-x.index('C'))<=4)): # 
                        print("anda")
                            #Llamar a la funcion para variar el ángulo
                            #Las tres variables de abajo probablemente no hagan falta
                        funcion=Trayectoria()
                        funcion.guardarAngulo(x)
                        valido=True
                        return (valido)
                    else:
                        print("Comando inválido") 
                        return(valido)            
                            
                            
                            #Probar de usar Catch errors          
        #diferencias entre A y B y A y C y B y C
        #luego hacer que si las posicions +2 +3 y +4 luego de la letra son numeros con un for y usando isdigit
                        #print("Acá hay una A")
                    
            #########################Funcion guardarAngulo
                    #poner rbt.RecibirOrden dentro de la clase robot
                                            # CAMBIAR W POR rbt.RecibirOrden()
   
    
    orden='EA+40B-30C180P'
    prueba=Trayectoria()
    prueba.esOrdenValida(orden)
    #Trayectoria.esOrdenValida
    print=("angulo 1 ", __self__.anguloGiro[0])
    print=("angulo 2 ", __self__.anguloGiro[1])
    print=("angulo 3 ", __self__.anguloGiro[2])

#si no anda el AnguloGiro usar ang1 ang2 y ang3 
    def setPosicionX(self, anguloGiro,):
            #Obtengo la posición en X del brazo
            #Primero paso el ángulo a radianes (por la librería)

        return(math.cos(math.radians(anguloGiro)))

    def setPosicionY(self, anguloGiro,):
            #Obtengo la posición en Y del brazo
            #Primero paso el ángulo a radianes (por la librería)

        return(math.cos(math.radians(anguloGiro)))   

    def setPosicionZ(self, anguloGiro,):
            #Obtengo la posición en Y del brazo
            #Primero paso el ángulo a radianes (por la librería)

        return(math.cos(math.radians(anguloGiro)))       
        
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







    


