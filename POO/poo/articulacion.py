

class Articulacion:
    def __init__(self):
        #super().__init__()
		self.ciclos_totales
		self.velocidad = 0
		self.Estado # Activo = FALSE Inactivo = TRUE
		self.Estadostr
		self.Operacion    
        self.anguloGiro[0]=0
		self.anguloGiro[1]=0
		self.anguloGiro[2]=0
		self.orden

    def Inicio(self):
	    Articulacion.setEstado(True) # Inactivo
	    print ("Estado del efector final: ", Articulacion.getEstadostr())    #Arreglar esto
	    self.ciclos_totales = 0
    
	
    def Abrir(self, actual, counter) :
	    Articulacion.setEstado(False) # Activo
	    Operacion = "Abrir" #Abre sus pinzas
	    if (actual + 1 == counter) :
		    Articulacion.setEstado(True) # Inactivo
	    self.ciclos_totales+=1


    def Cerrar(self,actual,  counter) :
	    Articulacion.setEstado(False) # Activo
	    Operacion = "Cerrar" #Cierra sus pinzas
	    if (actual + 1 == counter) :
		    Articulacion.setEstado(True) # Inactivo
	    self.ciclos_totales+=1


    def Rotar(self,actual, counter) :
	    Articulacion.setEstado(False) # Activo
	    Operacion = "Rotar" 
	    if (actual + 1 == counter) :
		    Articulacion.setEstado(True) # Inactivo	
	    self.ciclos_totales+=1


    def Cambiar_Velocidad(self, Nueva_velocidad, actual, counter):
	    Articulacion.setEstado(False) # Activo
	    Operacion = "Cambiar Velocidad"
	    velocidad = Nueva_velocidad
	    if (actual + 1 == counter) :
		    Articulacion.setEstado(True) # Inactivo
	    self.ciclos_totales+=1


    def getvelocidad(self) :
        return Articulacion.velocidad


    def getEstado(self) :
	    return Articulacion.Estado


    def setEstado(self, Nuevo_Estado) :
	    Articulacion.Estado = Nuevo_Estado


    def getEstadostr(self) :
	if (Articulacion.Estado == True) :
		return ("INACTIVO (libre)")
	else :
		return ("ACTIVO (en proceso)")
	


    def getciclos(self) :
	    return Articulacion.ciclos_totales


    def sumarciclos(self) :
	    Articulacion.ciclos_totales+=1


    def getOperacion(self) :
	    return Articulacion.Operacion


    def parada(self) :
	        Articulacion.setEstado(False) # Activo

		
	def esOrdenValida (self, x) :
        valido= False
        if (x[0]=='E' and x[len(x)-1]=='P'):
            #print("es cierto que hay e o p")
            if ('A' in x or 'V' in x or 'R' in x):
                if ((x[x.index('A')+1]=='+' or x[x.index('A')+1]=='-')  and (x[x.index('V')+1]=='+' or x[x.index('V')+1]=='-') and (x[x.index('R')+1]=='+' or x[x.index('R')+1]=='-')):
                    #print("Hay un signo de + o de -")
                    if ((1<=abs((x.index('A')+1)-x.index('V'))<=4) and (1<=abs((x.index('V')+1)-x.index('R'))<=4) and (1<=abs((x.index('R')+1)-x.index('P'))<=4)):
                        #Llamar a la funcion para variar el ángulo
                        #Las tres variables de abajo probablemente no hagan falta
						Articulacion.guardarAngulo(x)
                        valido=True
                        return (valido)
                    else:
                        print("Comando inválido") 
                        return(valido) 

	#########################Funcion guardarAngulo
	def guardarAngulo(self, orden)           #poner rbt.RecibirOrden dentro de la clase robot
										# CAMBIAR W POR rbt.RecibirOrden()
		#print ("Los números entre letras (con signo) son: ")
		#print(orden[(orden.index('A')+1):(orden.index('V'))])
		#print(orden[(orden.index('V')+1):(orden.index('R'))])
		#print(orden[(orden.index('R')+1):(orden.index('P'))])
		self.anguloGiro[0]=int (orden[(orden.index('A')+1):(orden.index('B'))])
        print=("angulo:  ", self.anguloGiro[0])
        self.anguloGiro[1]=int (orden[(orden.index('B')+1):(orden.index('C'))])
        print=("velocidad ", self.anguloGiro[1])
        self.anguloGiro[2]=int (orden[(orden.index('C')+1):(orden.index('P'))])
    	print=("rotacion ", self.anguloGiro[2])


		#Angulos y signos de cada orden
		#ang1=(orden[(orden.index('A')+2):(orden.index('V'))])
		#sigA=orden[(orden.index('A')+1)]
		#ang2=(orden[(orden.index('V')+2):(orden.index('R'))])
		#sigB=orden[(orden.index('V')+1)]
		#ang3=(orden[(orden.index('R')+2):(orden.index('P'))])
		#sigC=orden[(orden.index('R')+1)]
		#*****************************ACA ASIGNAR LOS ANGULOS A LAS CLASES CREADAS**********************************
		#*****************************Mirar de sacar la velocidad y despues ponerla de nuevo************************
		#**********Hacer atributos a robot con todos los angulos y velocidades (EN REALIDAD ASIGNAR UNO A CADA OBJETO QUE SERÍA EL BRAZO)
		velocidad = input("Ingrese la velocidad ")      #En realidad es un argumento pasado por el cliente

#	def operarEfector(self, velocidad, ang1, ang2, ang3):
#		dimA=input("Ingrese la dimensión del brazo A")
#		dimB=input("Ingrese la dimensión del brazo B")
#		dimC=input("Ingrese la dimensión del brazo C")
#		if (W):
#			print("aca se guardan los valores para cada articulacion")
			#Brazo_A= rbt(velocidad, ang1, sigA, dimA)
			#Brazo_B= rbt(velocidad, ang2, sigB, dimB)
			#Brazo_C= rbt(velocidad, ang3, sigC, dimC)
#		else:
#			pass
#	def anguloActual(self, sigA, ang1):
#		angulo1 = int(sigA+ang1)
#		print("este es el angulo 1 con signo: ")
#		print(angulo1)
#		angulo2 = int(sigB+ang2)
#		print("este es el angulo 2 con signo: ")
#		print(angulo2)
#		angulo3 = int(sigC+ang3)
#		print("este es el angulo 3 con signo: ")
#		print(angulo3)					