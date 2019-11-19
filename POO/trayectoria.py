import sys
sys.path.insert(0, 'home/agustin/Proyecto_poo/Proyecto_poo/POO')
sys.path.insert(0, 'home/agustin/Proyecto_poo/Proyecto_poo/POO/Robot')
import Robot as rbt
import math







orden='EA+50B-130C+3P'
#aRREGLAR PARA QUE SEA SOLO HASTA 360 GRADOS
#if (modo=='M'):   PONER ESTO DENTRO DE UN WHILE


######################################################################
#########################Funcion es Orden Valida
class Trayectoria:
    def __init__(self):
        self.anguloGiro[3]    
        self.posicion_artB[3]
        self.posicion_artC[3]
        self.velocidad
        self.ang1
        self.ang2
        self.ang3
        print("Este es el numero de diferencia entre indices B y A" )
        print((orden.index('B')-1)-orden.index('A'))    
    def recibirOrden(x):
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
    W=recibirOrden(orden)           #poner rbt.RecibirOrden dentro de la clase robot
                                    # CAMBIAR W POR rbt.RecibirOrden()

    print("La diferencia entre indices es ")
    print(abs(orden.index('A')-orden.index('B')))
    print ("Los números entre letras (sin signo) son: ")
    print(orden[(orden.index('A')+2):(orden.index('B'))])
    print(orden[(orden.index('B')+2):(orden.index('C'))])
    print(orden[(orden.index('C')+2):(orden.index('P'))])
    print(W)
    #Angulos y signos de cada orden
    self.ang1=(orden[(orden.index('A')+2):(orden.index('B'))])
    sigA=orden[(orden.index('A')+1)]
    self.ang2=(orden[(orden.index('B')+2):(orden.index('C'))])
    sigB=orden[(orden.index('B')+1)]
    self.ang3=(orden[(orden.index('C')+2):(orden.index('P'))])
    sigC=orden[(orden.index('C')+1)]
    #*****************************ACA ASIGNAR LOS ANGULOS A LAS CLASES CREADAS**********************************
    #*****************************Mirar de sacar la velocidad y despues ponerla de nuevo************************
    #**********Hacer atributos a robot con todos los angulos y velocidades (EN REALIDAD ASIGNAR UNO A CADA OBJETO QUE SERÍA EL BRAZO)
    self.velocidad = input("Ingrese la velocidad ")      #En realidad es un argumento pasado por el cliente

    def operarEfector(velocidad, ang1, ang2, ang3):
        dimA=input("Ingrese la dimensión del brazo A")
        dimB=input("Ingrese la dimensión del brazo B")
        dimC=input("Ingrese la dimensión del brazo C")
        if (W):
            print("aca se guardan los valores para cada articulacion")
            #Brazo_A= rbt(velocidad, ang1, sigA, dimA)
            #Brazo_B= rbt(velocidad, ang2, sigB, dimB)
            #Brazo_C= rbt(velocidad, ang3, sigC, dimC)
        else:
            pass
    def anguloActual(sigA, ang1):
        angulo1 = int(sigA+ang1)
        print("este es el angulo 1 con signo: ")
        print(angulo1)
        angulo2 = int(sigB+ang2)
        print("este es el angulo 2 con signo: ")
        print(angulo2)
        angulo3 = int(sigC+ang3)
        print("este es el angulo 3 con signo: ")
        print(angulo3)








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
            l1=10; l2=5; l3=4.5
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







operarEfector(velocidad, ang1, ang2, ang3)
anguloActual(sigA, ang1)



