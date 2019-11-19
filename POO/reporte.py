#!/usr/bin/env python3
#encoding: UTF-8
import os
import glob
import time
import sys
sys.path.insert(0, 'home/agustin/Proyecto_poo/Proyecto_poo/POO')

def Escribir(orden):
    f= open ('datos.txt','+w') #escribe el archivo data para lectura con C
    f.write("Articulación 1:        Articulacion 2:         Articulacion 3: \n")
    f.write(orden)
    f.close()
