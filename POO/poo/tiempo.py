import time

class Tiempo:
    def __init__(self):
        #super().__init__()
        self.time0
        self.time
        self.timeOp
        self.timeOrdenes

    
    def getTime(self) :
        return Tiempo.time
    

    def setTime(self, new_time) :
        Tiempo.time = new_time
    

    def getTime0(self) :
        return Tiempo.time0
    

    def setTime0(self, new_time) :
        Tiempo.time0 = new_time
    

    def medirTime(self):
        t = time.time()
        ss=[]       #Vector para guardar los tiempos
        Tiempo.setTime(t)     
        segundos = ((Tiempo.getTime() - Tiempo.getTime0())) #/ CLOCKS_PER_SEC)
        ss.append("Instante de inicio orden: ", segundos, " seg") 
        print(ss) 
    

    def setActivityTime(self, t):
        self.timeOp += t 
    

    def setOrdenesTime(self, t):
        Tiempo.timeOrdenes.append(t)
        



