#!/usr/bin/env python3
#encoding: UTF-8
import os
import glob
import time
import sys
sys.path.insert(0, 'home/agustin/Proyecto_poo/Proyecto_poo/POO')
class Reporte:
    def __init__(self):
        self.orden

    def Escribir(self, orden):
        existe=os.path.exists('home/agustin/Proyecto_poo/Proyecto_poo/C++/brazo.txt')    #Acá poner el archivo a leer
        
    
        if (existe == False):
            f= open ('brazo.txt','+w') #escribe el archivo data para lectura 
            f.write("Articulación 1:        Articulacion 2:         Articulacion 3: \n")
            f.write( "\n", orden)
            f.close()
        else:
            f=open ('brazo.txt','a+')           #Abre el archivo existente para agregar datos    

    def read(self, archivo):
        f=archivo
        if not os.path.isfile(f):
            print("No se pudo abrir el archivo, vuelva a intentar")
            orden = "ERROR"
            sys.exit()
        line=f.readlines()
        with open(f) as f:
            line = f.readlines()            #Si no anda es porque es readline sin S
            cnt = 1
        while line:
            print("Orden {}: {}".format(cnt, line.strip()))
            line = f.readlines()
            cnt += 1
            orden=line
            return(orden)
        
        #Esta es otra forma
    #    if  (f.closed==False):   
    #        while
    #            f = open(archivo, 'r')
    #            line = f.readlines()
    #        f.close()

    def crear_rutina(self):
        
        archivo=input("Ingrese nombre del archivo a crear: ")
            
        op=1
        print("Escriba GUARDAR una vez terminado de cargar de ordenes" 
                "\nIngrese orden nueva: ") 
            
        while (op==1):
            fin=open(archivo,'+w')
            fout=open(archivo,'r')
            orden=input("orden: ")
            
            if ((orden != "GUARDAR") and (os.path.isfile(fin))):
                fout.append('\n')
                fout.append(orden)
                    #fin=open(archivo, 'a+')
                    #fin.write(orden)            
            
            if ((orden == "GUARDAR") or (orden == "guardar")):
                op=0
                print("Rutina guardada exitosamente")
    
            fin.close()
            fout.close()
            
