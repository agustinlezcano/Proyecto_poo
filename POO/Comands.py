import cmd, sys
import IDL as idl
import Robot as rbt
import Trayectoria as tr
import Articulacion as arti
#from . import Robot.py
#Class por la ayuda y por los comandos y panel de control
#mirar a este ejemplo : https://docs.python.org/fr/3/library/cmd.html
#Hacer un class para leer los comandos del cliente -> ejecutar este commando 

class Comandos(cmd.Cmd):
    """Interprete de comandos"""
    def __init__(self):
        self.r = rbt.Robot(0,0,0,0)
        self.tr = tr.Trayectoria()
        
    prompt = "Introduza un comando: "
    def do_Conexion(self, args):
        """Ayuda de la funcion Conexion : Conectar el robot usando comunicación serial"""
        self.r.connectarRobot("3000")
        if(self.r.b_co):
            print("El robot está conectado")

    def do_Deconexion(self, args):
        """Ayuda de la funcion Deconexion : Deconectar el robot usando comunicación serial"""
        self.r.desconnectarRobot("3000")
        if(self.r.b_co == False):
            print("El robot está desconectado")

    def do_Activar(self, args):
        """Ayuda de la funcion Activar : Activacion del Robot"""
        self.r.activar()
        if(self.r.b_co):
            print("El robot está activado")

    def do_Desactivar(self, args):
        """Ayuda de la funcion Desactivar : Desactivacion del Robot"""
        self.r.desactivar()
        if(self.r.b_ac == False):
            print("El robot está desactivado")

    def do_MoverArticulaciones(self, args):
        """Ayuda de la funcion MoverArticulaciones : Permite de eligir una articulacion y mover la de un angulo"""
        self.r.moverarticulaciones()
        print("MoverArticulaciones se ha ejecutado")

    def do_operarEfector(self, args):
        """Ayuda de la funcion operarEfector : Permite de operar el efector : 
        podemos cerrar, abrir, rotar el efector"""
        #self.tr.operarEfector(tr.velocidad, tr.ang1, tr.ang2, tr.ang3)
        print("ooperarEfector se ha ejecutado")
    
    def do_moverPosicionOrigen(self, args):
        """Ayuda de la funcion moverPosicionOrigen : Permite de volver a la posicion de origen del robot"""
        self.r.moverPosicionOrigen()
        print("moverPosicionOrigen se ha ejecutado")

    def do_ModoAutomatica(self, args):
        """ Ejecutar un reporte con diferentes aciones"""
        self.r.modoautomatica()
        print("ModoAutomatica se ha ejecutado")

    def do_salir(self, args):
        """Salir del interprete"""
        print("Hasta pronto")
        return(True)

if __name__ == "__main__":
    #poner este en el servidor
    #when we have la lista de del IDL podemos activar los onecmd 
    #if auto == True hacemos ModoAutomatica
    #if manu -> hacemos 
    interprete = Comandos()
    interprete.onecmd("Conexion")
    interprete.onecmd("Activar")
    interprete.onecmd("Desactivar")
    interprete.onecmd("Deconexion")
    auto = True
    a = idl.IDL(auto)
    print(a.analizarReporte_auto("girar", auto))