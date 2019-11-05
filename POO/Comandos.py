import Servidor.py as s

class Comandos(cmd.Cmd):
    """Interprete de comandos"""
    prompt = "Introduza un comando: "
   
    def do_Crear(self, args):
        """Ayuda del comando1"""
       # Interface.crear(self)
        proxy.crear()
        print("comando1 se ha ejecutado")

    def do_Borrar(self, args):
        """Ayuda del comando2"""
        #Interface.borrar(self)
        print("comando2 se ha ejecutado")

    def do_Renombrar(self, args):
        """Ayuda del comando2"""
        #Interface.renombrar(self)
        print("comando2 se ha ejecutado")

    def do_Agregar(self, args):
        """Ayuda del comando2"""
        #Interface.agregar(self)
        print("comando2 se ha ejecutado")

    def do_Listar(self, args):
        """Ayuda del comando2"""
        #Interface.listar(self)
        print("comando2 se ha ejecutado")
        
    def do_Devolver(self, args):
        """Ayuda del comando2"""
        #Interface.devolver(self)
        print("comando2 se ha ejecutado")

    def do_salir(self, args):
        """Salir del interprete"""
        print("Hasta pronto")
        return(True)

#class Comandos(s.Servidor):
    #def __init__(self, liste):
        #self.liste = liste #tiene que ser una list = []

    #def listarComandos(self):
     #   for a in self.liste:
      #      print(a + "\n")