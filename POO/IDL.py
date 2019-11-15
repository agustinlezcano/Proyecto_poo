#Este clase permite de analizar cada data que viene del servidor
#Este data he analizado y despues he tratado en la clase Comandos 
#La classe
import sys
class IDL:
    def __init__(self, auto):
        #self.cmd = cmd
        self.liste = []
        self.auto = auto #bool para saber si modo auto o modo manual

    def analizarReporte_auto(self, cmd, auto): #por el modo automatico
        if(auto):
            switcher = {
                "girar": 'Girar', #poner los letras requiridos
                "mover": 'Mover',
                "parar": 'Parar',
                #ect / cada opciones del robot
            }
            self.liste.append(switcher.get(cmd, "Error"))
        return(self.liste, auto)

    def analizarReporte_manu(self, cmd, auto, b_arti):
        b_arti = False #poner este estado si el reporte empienza con Arti
        if(auto != True):
            switcher = {
                "A": '1', #poner los letras requiridos
                "B": '2',
                "C": '3',
                "operarefector": 'operarEfector',
                "moverPosicionOrigen" : 'moverPosicionOrigen',
                "moverarticulaciones" : 'MoverArticulaciones',
                #ect
            }
            self.liste.append(switcher.get(cmd, "Error"))
        return(self.liste, b_arti) 

    def otroscomandos(self, cmd):
        switcher = {
                "salir": 'salir', #poner los letras requiridos
                "?": '?',
                "help": 'help',
                "activar": 'Activar',#ect
                "desactivar": 'Desactivar',
                "conexion" : 'Conexion',
                "deconexion" : 'Deconexion',
            }
        self.liste.append(switcher.get(cmd, "Error"))
        return self.liste 

if __name__ == "__main__":
    auto = True
    a = IDL(auto)
    print(a.analizarReporte_auto("girar", auto))