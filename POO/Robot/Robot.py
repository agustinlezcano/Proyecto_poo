class Trayectoria:
    def __init__(self, x, y, z, direccion):
        self.x = x
        self.y = y
        self.z = z
        self.direccion = direccion
    def guardarTrayectoria(self):
        pass

class Articulation:
    def __init__(self, nombre, velocidad, distancia, anguloGiro, sentido):
        self.velocidad = velocidad
        self.distancia = distancia
        self.anguloGiro = anguloGiro
        self.sentido = sentido
    def girar(self, self.anguloGiro):
        pass
    def mover(self, self.x, self.y, self.y):
        pass

class Robot:
    def __init__(self, velocidad, distancia, anguloGiro, sentido, 
    posicionOrigen, tiempoOperacion, trayectoria, velMaxLineal, velMaxAngular, tipoRobot, 
    configration, efectorFinal, dimensionMax):
        self.articlation = Articulation(nombre, velocidad, distancia, anguloGiro, sentido )
        self.posicionOrigen = posicionOrigen
        
    
    def connectarRobot(self):
        pass
    def desconnectarRobot(self):
        pass
    def activar(self):
        pass
    def desactivar(self):
        pass
    def generarReporte(self):
        pass
    def moverPosicionOrigen(self):
        pass
    def operarEffector(self):
        pass