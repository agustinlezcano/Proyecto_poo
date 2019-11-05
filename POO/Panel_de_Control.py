import Servidor.py as s

class Panel_de_control(s.Servidor):

    def __init__(self, estadoPanel):
        self.estadoPanel = estadoPanel

    def recibirOrden(self):
