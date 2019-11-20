#Este clase permite analizar cada data que viene del servidor
#Este data he analizado y despues he tratado en la clase Comandos 
#La clase
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import sys
sys.path.insert(0, 'media/datos/UNCUYO/POO/PROYECTO/Respaldo_proyecto/POO')
import reporte 
from trayectoria import Trayectoria
from articulacion import Articulacion
#from Comands import Comandos
from tiempo11 import Tiempo
from reporte import Reporte
import subprocess

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)



# Create server
with SimpleXMLRPCServer(('192.168.0.21', 8080),
                        requestHandler=RequestHandler) as server:
#    subprocess.call(['./run_godot.sh'])                    
    server.register_introspection_functions()
#    server.register_instance(IDL)
#    server.register_instance(Comandos)
    def registro(orden):
        return orden 
    server.register_function(registro, 'registrar_orden')

    server.register_instance(Trayectoria)
    server.register_instance(Articulacion)
    server.register_instance(Tiempo)
    server.register_instance(Reporte)
    class IDL:
        def __init__(self):
            self.modo
        
        def controlBrazo(self):
            modo=input("Ingrese modo:"   
                        "A - Modo Automático"  
                        "M - Modo Manual" )
        
            if (modo == "A"):
                    #string archivo
                archivo=input("Ingrese archivo para leer: ")
                Reporte.read(archivo)
                status = True #Inactivo
                while (status==True):
                    aux=0
                    aux=input("1. Cargar rutina \n2. Generar rutina de aprendizaje")
                    print( "\n")
                    if (aux==2):
                        reporte.crear_rutina()
                
                    if (aux==1):
                        archivo=input( "Ingrese archivo para leer: ")
                        orden=reporte.read(archivo)
                
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

                    if(Trayectoria.esOrdenValida(orden)):
                        print( "Orden válida")  
            
                    if (modo == "A"):
                        orden="T"

        def controlPinza(self) :
            
            inicializacion=input( "¿Desea inicializar? S / N:  ") 
        
            if (inicializacion == "s" or inicializacion == "S") :
                Articulacion.Inicio()
            else :
                print( "Saliendo...") 
                Articulacion.setEstado(False) # Falso activo
            
            
            modo=input("Ingrese modo:"   
                        "A - Modo Automático"  
                        "M - Modo Manual") 
            
            
            if(modo == "A"):
                archivo=input( "Ingrese archivo para leer: ")
                orden=reporte.read(archivo)
                
                if(Articulacion.esOrdenValida(orden)):
                    print( "Orden válida" ) 
                
            
            
            if (modo == "M"):
            
                while (Articulacion.getEstado()) :
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
                    
                    
                    if(Articulacion.esOrdenValida(orden)):
                        print( "Orden válida")  
                        #delete ef
                    
                    if (modo == "A"):
                        orden="T"
    if __name__ == "__main__":
        print('Servidor XML-RPC funcionando en puerto 8080')                    
        try:
            print("===========================================\n"
                "             ORDENES             \n"   
                "1 - Control articulaciones\n"  
                "2 - Control efector final\n"  
                "0 - Salir\n"
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
                else:
                    band=False
                    break
            print("Sending...")
            orden='EA+40B-30C+180P'                  #Aca va la orden enviada del cliente 
            #registro(orden)
            prueba=Trayectoria()
            prueba.esOrdenValida(orden)
            print=("angulo 1 ", prueba.anguloGiro1)
            print=("angulo 2 ", prueba.anguloGiro2)
            print=("angulo 3 ", prueba.anguloGiro3)
            if (prueba.esOrdenValida(orden)):
                prueba.guardarAngulo(orden)
                prueba.setPosicionX(prueba.anguloGiro1)
                prueba.setPosicionY(prueba.anguloGiro2)
                prueba.setPosicionZ(prueba.anguloGiro3)
            orden2='EA+50V-130R+3P'                 #Aca va la otra orden de la pinza
            prueba2=Articulacion()
            prueba2.esOrdenValida(orden2)
            #print("efector: \n")
            print=("angulo de abertura ", prueba2.anguloGiro1)
            print=("velocidad ", prueba2.anguloGiro2)
            print=("rotacion ", prueba2.anguloGiro3)
            if (prueba2.esOrdenValida(orden2)):
                prueba2.guardarAngulo(orden2)    

            server.serve_forever()
        except KeyboardInterrupt:
            print("Exiting")
#            subprocess.call(['./close_godot.sh'])
            sys.exit(0)
            
         
    
  
    

