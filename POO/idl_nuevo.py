#Esta clase permite analizar los datos que vienen del servidor
#Los datos analizados son tratados en la clase Comandos 
#La clase
import os
from xmlrpc.server import SimpleXMLRPCServer
import sys
sys.path.insert(0, 'media/datos/UNCUYO/POO/PROYECTO/Respaldo_proyecto/POO')
#import reporte 
#from Comands import Comandos
from tiempo12 import Tiempo
from trayectoria import Trayectoria
from articulacion import Articulacion
import subprocess
from builtins import print
from reporte import Reporte
# A simple server with simple arithmetic functions
server = SimpleXMLRPCServer(("192.168.0.21", 8080))
print("Listening on port 8080...")
#Recibe las ordenes de brazo o pinza

def letras(x):
    c="El código es "
    c+=x
    print(c)
    return (c) 
    
    existe=os.path.exists('home/agustin/Proyecto_poo/Proyecto_poo/C++/brazo.txt')    #Acá poner el archivo a leer

    if (existe == False):
        f= open ('brazo.txt','+w') #escribe el archivo data para lectura 
        f.write("\n", x)
        f.close()
    else:
        f=open ('brazo.txt','a+')           #Abre el archivo existente para agregar datos    
        f.write("\n",x)
        f.close()
server.register_function(letras, 'brazo')

def ordenes(x):
    c="El código es "
    c+=x
    print(c)
    return (c) 
    
    existe=os.path.exists('home/agustin/Proyecto_poo/Proyecto_poo/C++/pinza.txt')    #Acá poner el archivo a leer

    if (existe == False):
        f= open ('pinza.txt','+w') #escribe el archivo data para lectura 
        f.write("\n", x)
        f.close()
    else:
        f=open ('pinza.txt','a+')           #Abre el archivo existente para agregar datos    
        f.write("\n",x)
        f.close()

server.register_function(letras, 'brazo')
server.register_function(ordenes, 'pinza')



server.register_multicall_functions()
server.register_instance(Trayectoria)
server.register_instance(Articulacion)
server.register_instance(Tiempo)
server.register_instance(Reporte)
class IDL:
    def __init__(self):
        self.codigo
        
    
    
    
if __name__ == "__main__":
    print('Servidor XML-RPC funcionando en puerto 8080')                    
    try:
        print("===========================================\n"
                "             ORDENES             \n"   
                "1 - Control articulaciones\n"  
                "2 - Control efector final\n"  
                "0 - Salir\n"
                "===========================================")
        





        print("Sending...")
        
      
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exiting")
#            subprocess.call(['./close_godot.sh'])
        sys.exit(0)       