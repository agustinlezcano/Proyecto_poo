#!/usr/bin/env python3
#encoding: UTF-8
import os
import glob
import time
import sys
sys.path.insert(0, 'media/datos/UNCUYO/POO/PROYECTO/Respaldo_proyecto/POO')
from trayectoria import Trayectoria
from tiempo11   import Tiempo

class Orden_godot:
    def __init__(self):
        self.orden1
        self.orden2
        self.orden3

    def generarOrden(self,orden1, orden2, orden3):
        f='orden_godot.txt'
        if not os.path.isfile(f):
            fp=open('orden_godot.txt', '+w') 
        else:
            fp=open('orden_godot.txt', 'a+') 
        
            fp.append(orden1, '\n', orden2, '\n', orden3, '\n')
              





