
class Robot:
    def __init__(self, velocidad, anguloGiro, sentido):#, posicionOrigen, tiempoOperacion, trayectoria, velMaxLineal, velMaxAngular, tipoRobot,configration, efectorFinal, dimensionMax):

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
        #analizar el reporte por la pinza y hacer lo que dice
        pass
    def moverarticulaciones(self):
        pass
    def modoautomatica(self):
        pass