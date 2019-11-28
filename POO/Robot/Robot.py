#poner este clase en el servidor
import math
import time
class Robot:
    def __init__(self, velocidad, anguloGiro, sentido, dimension):#, posicionOrigen, tiempoOperacion, trayectoria, velMaxLineal, velMaxAngular, tipoRobot,configration, efectorFinal, dimensionMax):

        self.velocidad = velocidad
        #self.distancia = distancia
        self.anguloGiro = anguloGiro
        self.sentido = sentido
        self.velMaxAngular = 0
        self.velMaxLineal = 0
        self.tipoRobot = "3DF"
        self.configration = "RRR"
        self.efectorFinal = "pinza"
        self.dimensionMax = [0, 0, 0]
        self.longitud=longitud
        self.b_co = False
        self.b_ac = False

    def conectarRobot(self, port):
        #if server receive a request -> identificar el port Serial -> poner un bool a True
        if(port == "8080"):
            self.b_co = True
        else:
            self.b_co = False
            print("Wrong Port")

    def desconectarRobot(self, port):
        if(port == "8080"):
            self.b_co = False
        else:
            self.b_co = True
            print("Imposible de desconectar")
    
    def activar(self):
        #poner un bool a True
        if(self.b_co):
            self.b_ac = True
        else:
            self.b_ac = False
            print("El robot tiene que ser conectado")
    
    def desactivar(self):
        #poner un bool a False
        if(self.b_co & self.b_ac):
            self.b_ac = False
        else:
            self.b_ac = True
            print("Imposible de desactivar, ya está desconectado")
            
    
    orden='EA+50B-130C+3P'
    #aRREGLAR PARA QUE SEA SOLO HASTA 360 GRADOS
    #if (modo=='M'):   PONER ESTO DENTRO DE UN WHILE


    ######################################################################
    #########################Funcion es Orden Valida
    print("Este es el numero de diferencia entre indices B y A" )
    print((orden.index('B')-1)-orden.index('A'))    
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
                        valido=True
                        return (valido)
                    else:
                        print("Comando inválido") 
                        return(valido)            
                        
        guardarAngulo(x)                
                        #Probar de usar Catch errors          
    #diferencias entre A y B y A y C y B y C
    #luego hacer que si las posicions +2 +3 y +4 luego de la letra son numeros con un for y usando isdigit
                    #print("Acá hay una A")
                
    #########################Funcion guardarAngulo
    W=esOrdenValida(orden)           #poner rbt.esOrdenValida dentro de la clase robot
                                    # CAMBIAR W POR rbt.guardarAngulo()
    def guardarAngulo(self,orden):
        print("La diferencia entre indices es ")
        print(abs(orden.index('A')-orden.index('V')))
        print ("Los números entre letras (sin signo) son: ")
        print(orden[(orden.index('A')+2):(orden.index('V'))])
        print(orden[(orden.index('V')+2):(orden.index('R'))])
        print(orden[(orden.index('R')+2):(orden.index('P'))])
        print(W)
        #Angulos y signos de cada orden
        ang1=(orden[(orden.index('A')+2):(orden.index('V'))])
        sigA=orden[(orden.index('A')+1)]
        ang2=(orden[(orden.index('V')+2):(orden.index('R'))])
        sigB=orden[(orden.index('V')+1)]
        ang3=(orden[(orden.index('R')+2):(orden.index('P'))])
        sigC=orden[(orden.index('R')+1)]
        #*****************************ACA ASIGNAR LOS ANGULOS A LAS CLASES CREADAS**********************************
        #*****************************Mirar de sacar la velocidad y despues ponerla de nuevo************************
        #**********Hacer atributos a robot con todos los angulos y velocidades (EN REALIDAD ASIGNAR UNO A CADA OBJETO QUE SERÍA EL BRAZO)
    
     velocidad = input("Ingrese la velocidad ")      #En realidad es un argumento pasado por el cliente

    def operarEfector(self ,velocidad, ang1, ang2, ang3):
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
    def anguloActual(self, sigA, ang1, sigB, ang2, sigC, ang3):
        angulo1 = int(sigA+ang1)
        print("este es el angulo 1 con signo: ")
        print(angulo1)
        angulo2 = int(sigB+ang2)
        print("este es el angulo 2 con signo: ")
        print(angulo2)
        angulo3 = int(sigC+ang3)
        print("este es el angulo 3 con signo: ")
        print(angulo3)

    operarEfector(velocidad, ang1, ang2, ang3)
    anguloActual(sigA, ang1)







    def moverPosicionOrigen(self):
        #poner cada articulacion a 0
        #enviar los datos al cliente para poner el robot en su posicion de origen
        pass
    def operarEfector(self):
        #analizar el reporte por la pinza y hacer lo que dice
        pass
    def moverarticulaciones(self):
        pass
    def modoautomatica(self):
        pass