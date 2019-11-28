import cmd, sys
import IDL as idl
import Robot as rbt
#from . import Robot.py
#Class por la ayuda y por los comandos y panel de control
#mirar a este ejemplo : https://docs.python.org/fr/3/library/cmd.html
#Hacer un class para leer los comandos del cliente -> ejecutar este commando 

class Comandos(cmd.Cmd):
    """Interprete de comandos"""
    def __init__(self):
        self.r = rbt.Robot(0,0,0,0)

    prompt = "Introduza un comando: "
    def do_Conexion(self, args):
        """Ayuda del .... """
        self.r.connectarRobot("3000")
        if(self.r.b_co):
            print("El robot está conectado")

    def do_Deconexion(self, args):
        """Ayuda del .... """
        self.r.desconnectarRobot("3000")
        if(self.r.b_co == False):
            print("El robot está desconectado")

    def do_Activar(self, args):
        """Ayuda del .... """
        self.r.activar()
        if(self.r.b_co):
            print("El robot está activado")

    def do_Desactivar(self, args):
        """Ayuda del .... """
        self.r.desactivar()
        if(self.r.b_ac == False):
            print("El robot está desactivado")

    def do_MoverArticulaciones(self, args):
        """Ayuda del comando1"""
        self.r.moverarticulaciones()
        print("comando1 se ha ejecutado")

    def do_operarEfector(self, args):
        """Ayuda del comando2"""
        self.r.operarEffector()
        print("comando2 se ha ejecutado")
    
    def do_moverPosicionOrigen(self, args):
        """Ayuda del comando2"""
        self.r.moverPosicionOrigen()
        print("comando2 se ha ejecutado")

    def do_ModoAutomatica(self, args):
        """ Ejecutar un reporte con diferentes aciones"""
        self.r.modoautomatica()
        print("bdfkk")

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