class Articulacion:
    def __init__(self):
			self.ciclos_totales = 0
			self.actual = 0
			self.velocidad = 0
			self.Estado # Activo = FALSE Inactivo = TRUE
			self.Estadostr
			self.Operacion    
        	self.anguloGiro
		
    def Inicio(self):
	    Articulacion.setEstado(True) # Inactivo
	    print ("Estado del efector final: ",Articulacion.getEstadostr())    #Arreglar esto
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

		
	def esOrdenValida(self, x):
        valido= False
        if (x[0]=='E' and x[len(x)-1]=='P'):
            print("es cierto que hay e o p")
            if ('A' in x or 'B' in x or 'C' in x):
                if ((x[x.index('A')+1]=='+' or x[x.index('A')+1]=='-')  and (x[x.index('V')+1]=='+' or x[x.index('V')+1]=='-') and (x[x.index('R')+1]=='+' or x[x.index('R')+1]=='-')):
                    print("Hay un signo de + o de -")
                    if ((1<=abs((x.index('A')+1)-x.index('V'))<=4) and (1<=abs((x.index('V')+1)-x.index('R'))<=4) and (1<=abs((x.index('R')+1)-x.index('P'))<=4)):
                        # or (1<=abs(x.index('A')-x.index('C'))<=4 and (1<=(x.index('B')-x.index('C'))<=4)): # 
                        print("anda")
                        #Llamar a la funcion para variar el ángulo
                        #Las tres variables de abajo probablemente no hagan falta
                        valido=True
                        return (valido)
                    else:
                        print("Comando inválido") 
                        return(valido) 