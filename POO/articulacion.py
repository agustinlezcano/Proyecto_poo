
import sys
sys.path.append('home/agustin/Proyecto_poo/Proyecto_poo/POO')
sys.path.append('media/datos/UNCUYO/POO/PROYECTO/Respaldo_proyecto/POO')

#import robot
import math
# from tiempo11 import Tiempo
from para_gotod import Orden_godot

class Articulacion:
    
	def __init__(self):
	
		self.Estado = False
		self.Estadostr =False    
		self.anguloGiro1 = 0
		self.anguloGiro2 = 0
		self.anguloGiro3 = 0  

# Estado Activo es FALSO e Inactivo es VERDADERO
	def Inicio(self):
	    Articulacion.setEstado(True) # Inactivo
	    print ("Estado del efector final: ", Articulacion.getEstadostr())    #Arreglar esto
	    self.ciclos_totales = 0
  
	def getEstado(self) :
	    return Articulacion.Estado


	def setEstado(self, Nuevo_Estado) :
	    Articulacion.Estado = Nuevo_Estado


	def getEstadostr(self) :
		if (Articulacion.Estado == True) :
			return ("INACTIVO (libre)")
		else :
			return ("ACTIVO (en proceso)")

    
		
	def esOrdenValida(self, x):
		valido= False
		if (x[0]=='E' and x[len(x)-1]=='P'):
			if ('A' in x or 'V' in x or 'R' in x):
				if ((x[x.index('A')+1]=='+' or x[x.index('A')+1]=='-')  and (x[x.index('V')+1]=='+' or x[x.index('V')+1]=='-') and (x[x.index('R')+1]=='+' or x[x.index('R')+1]=='-')):
					if ((1<=abs((x.index('A')+1)-x.index('V'))<=4) and (1<=abs((x.index('V')+1)-x.index('R'))<=4) and (1<=abs((x.index('R')+1)-x.index('P'))<=4)):
						valido=True
						return(valido)
					else:
						print("comando invalido")
						return(valido)
				else:
					print("No olvide colocar los signos, intente nuevamente")	


	def guardarAngulo(self, orden):           #poner rbt.RecibirOrden dentro de la clase robot  CAMBIAR W POR rbt.RecibirOrden										
		self.anguloGiro1=int (orden[(orden.index('A')+1):(orden.index('V'))])
		ang1=self.anguloGiro1
		print("angulo 1 ", self.anguloGiro1)
		self.anguloGiro2=int (orden[(orden.index('V')+1):(orden.index('R'))])
		ang2=self.anguloGiro2
		print("angulo 2 ", self.anguloGiro2)
		self.anguloGiro3=int (orden[(orden.index('R')+1):(orden.index('P'))])
		ang3=self.anguloGiro3
		print("angulo 3 ", self.anguloGiro3)


		

if __name__ == "__main__":
    orden='EA+40V-30R+180P'
    print(abs((orden.index('A')+1)-orden.index('R')))
    print(orden[orden.index('A')+1])
    print((orden[orden.index('R')+1]))
    prueba2=Articulacion()
    prueba2.esOrdenValida(orden)
    
    if (prueba2.esOrdenValida(orden)):
        print(prueba2.guardarAngulo(orden))
    
    #godot= para_gotod()
    #godot.generarOrden(Trayectoria.anguloGiro1, Trayectoria.anguloGiro2, Trayectoria.anguloGiro3 )
    
    #Aca estaba el bloque de times
	#    prueba2.setPosicionX(prueba2.anguloGiro1)
    #	 prueba2.setPosicionY(prueba2.anguloGiro2)
    #    prueba2.setPosicionZ(prueba2.anguloGiro3)
        #prueba.posicion(prueba.anguloGiro1,prueba.anguloGiro2,prueba.anguloGiro3)
        #mide_tiempo = Tiempo()
        #mide_tiempo.setActivityTime((prueba.anguloGiro1)*0.01)
        #mide_tiempo.setActivityTime((prueba.anguloGiro2)*0.01)
        #mide_tiempo.setActivityTime((prueba.anguloGiro3)*0.01)        
        #mide_tiempo.medirTime()
