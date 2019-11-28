#Este clase permite analizar cada data que viene del servidor
#Este data he analizado y despues he tratado en la clase Comandos 
#La clase
import sys
sys.path.insert(0, 'media/datos/UNCUYO/POO/PROYECTO/Proyecto_poo/POO')
from reporte import lectura
from trayectoria import trayec
from articulacion import ef

class IDL:
    def __init__(self):
        #self.cmd = cmd
        self.liste = []

    def __main__(self):
        print("==========================================="
              "             ORDENES             "   
            "1 - Control articulaciones"  
            "2 - Control efector final"  
            "0 - Salir"
            "===========================================")
        band = True
        while (band==True) :
            ej=input( "Ingrese el número de orden a realizar: ")
            if (ej == 0):
                band =False
                break
            if (ej == 1):
                IDL.controlBrazo()
                break 
            if (ej == 2):
                IDL.controlPinza()
                break


def controlBrazo(self):
    
   
    modo=input("Ingrese modo:"   
    "A - Modo Automático"  
    "M - Modo Manual" )
    
    #Aca solo llama a las otras clases
    #Trayectoria * trayec= new Trayectoria()
    #Leer * lectura = new Leer()
    
    #string orden
    if (modo == "A"):
        #string archivo
        status = True #Inactivo
        while (status==True):
            aux=0
            aux=input("1. Cargar rutina \n2. Generar rutina de aprendizaje")
            print( "\n")
            if (aux==2):
                lectura.crear_rutina()
            
            if (aux==1):
                archivo=input( "Ingrese archivo para leer: ")
                orden=lectura.read(archivo)
            
                if (orden!="ERROR"):
                    status = 0
 
    while(True):
        if (modo == "M"):
            orden=input("Ingrese el número de la acción:"   
            "E - Empezar"  
            "P - Parar"  
            "A - Articulacion A"  
            "B - Articulacion B"  
            "C - Articulacion C"  
            "T para terminar") 
            print(orden) 
        
        
        if(orden=="T"):
            break
        
       
        if(trayec.esOrdenValida(orden)):
            print( "Orden válida")  
        
        if (modo == "A"):
            orden="T"

def controlPinza(self) :
    
    
    #Leer * lectura = new Leer()
    
    #string orden, archivo
    #string inicializacion
    
    
    inicializacion=input( "¿Desea inicializar? S / N:  ") 
   
    if (inicializacion == "s" or inicializacion == "S") :
	    ef.Inicio()
    else :
	    print( "Saliendo...") 
	    ef.setEstado(False) # Falso activo
    
    
    modo=input("Ingrese modo:"   
                "A - Modo Automático"  
                 "M - Modo Manual") 
    
    
    if(modo == "A"):
        archivo=input( "Ingrese archivo para leer: ")
        orden=lectura.read(archivo)
        
        if(ef.esOrdenValida(orden)):
            print( "Orden válida" ) 
        
    
    
    if (modo == "M"):
    
        while (ef.getEstado()) :
            orden=input( "Elija la acción a realizar: "  
                     "E para Empezar"  
                     "P para Parar"  
                     "A+ para Abrir"  
                     "A- para Cerrar"  
                     "R para Rotar"  
                     "V para Cambiar velocidad"  
                     "T para Terminar") 
            
            if(orden=="T"):
                #delete ef
                break
            
            
            if(ef.esOrdenValida(orden)):
                print( "Orden válida")  
                #delete ef
            
            if (modo == "A"):
                orden="T"
            
         
    
  
    

