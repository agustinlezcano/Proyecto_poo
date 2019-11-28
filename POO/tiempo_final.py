import sys
import time

class Tiempo:
    def __init__(self):
        self.time0 = 0
        self.timeOp = 0
        self.timeOrdenes 0 []
        
    def getTime0(self):
        return (self.time0)
    
    def setTime(self, new_time):
        self.time0 = new_time
        
    def medirTime(self):
        t = time.time()
        ss=[]
        Tiempo.setTime(t)
        segundos = ((Tiempo.getTime() - Tiempo.getTime0())) #/ CLOCKS_PER_SEC)
        ss.append("Instante de inicio orden: ", segundos, " seg") 
        print(ss)
        
    def setActivityTime(self, t):
        self.timeOp += t
        
    def setOrdenesTime(self, t):
        self.timeOrdenes.append(t)
