import sys
sys.path.append('home/agustin/Proyecto_poo/Proyecto_poo/POO')
sys.path.append('media/datos/UNCUYO/POO/PROYECTO/Respaldo_proyecto/POO')
#import robot
import math
from tiempo11 import Tiempo
from para_gotod import Orden_godot

class Articulacion:
    def __init__(self):
		self.anguloGiro1 = 0
        self.anguloGiro2 = 0
        self.anguloGiro3 = 0
        self.ciclos_totales = 0
		self.velocidad = 0
		self.Estado # Activo = FALSE Inactivo = TRUE
		self.Estadostr
		self.Operacion  

    