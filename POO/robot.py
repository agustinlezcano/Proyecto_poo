#poner este clase en el servidor
import articulacion.py as arti
import trayectoria.py  as tr

class Robot(arti.Articulacion, tr.Trayectoria):
    def __init__(self, velocidad, anguloGiro, sentido):#, posicionOrigen, tiempoOperacion, trayectoria, velMaxLineal, velMaxAngular, tipoRobot,configration, efectorFinal, dimensionMax):
        self.tra = tr.Trayectoria()
        self.velocidad = velocidad
        #self.distancia = distancia
        self.anguloGiro = anguloGiro
        self.sentido = sentido
        self.velMaxAngular = 0
        self.velMaxLineal = 0
        self.tipoRobot = "3DF"
        self.configration = "RRR"
        self.efectorFinal = "pinza"
        self.dimensionMax = [0, 0, 0]
        self.b_co = False
        self.b_ac = False

    def connectarRobot(self, port):
        #if server receive a request -> identificar el port Serial -> poner un bool a True
        if(port == "3000"):
            self.b_co = True
        else:
            self.b_co = False
            print("Wrong Port")

    def desconnectarRobot(self, port):
        if(port == "3000"):
            self.b_co = False
        else:
            self.b_co = True
            print("Imposible de desconnectar")

    def activar(self):
        #poner un bool a True
        if(self.b_co):
            self.b_ac = True
        else:
            self.b_ac = False
            print("El robot tiene que ser connectado")
    
    def desactivar(self):
        #poner un bool a False
        if(self.b_co & self.b_ac):
            self.b_ac = False
        else:
            self.b_ac = True
            print("Imposible de desactivar")

    def moverPosicionOrigen(self):
        #poner cada articulaciones a 0
        #enviar los datos al cliente para poner el robot en su posicion de origen
        pass
    def operarEffector(self):
        self.tra.operarEffector(self.tra.velocidad, self.tra.ang1, self.tra.ang2, self.tra.ang3)
        
    def moverarticulaciones(self):
        print("Elegir el movimiento de la articulaciones")
        print("1 - Abrir")
        print("2 - Cerrar")
        print("3 - Rotar")
        print("4 - Cambiar Velocidad")
        arti = arti.Articulacion()
        arti.Inicio()
        e = int(input("Elegir el numero"))
        if e == 1:
            arti.Abrir(arti.actual, arti.ciclo_totales)
        elif e == 2:
            arti.Cerrar(arti.actual, arti.ciclo_totales)
        elif e == 3:
            arti.Rotar(arti.actual, arti.ciclo_totales)
        elif e == 4:
            arti.velocidad = float(input("Poner una nueva velocidad"))
            arti.Cambiar_Velocidad(arti.velocidad, arti.actual, arti.ciclo_totales)
        else: 
            print("Errores")
        arti.parada()
    