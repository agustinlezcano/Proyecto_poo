#import para_gotod as rgodot
from builtins import print

anguloGiro=[0, 0, 0]
orden='EA+50B-130C+3P'
anguloGiro[0]=int (orden[(orden.index('A')+1):(orden.index('B'))])
print("angulo 1 ", anguloGiro[0])
anguloGiro[1]=int (orden[(orden.index('B')+1):(orden.index('C'))])
print("angulo 2 ", anguloGiro[1])
anguloGiro[2]=int (orden[(orden.index('C')+1):(orden.index('P'))])
print("angulo 3 ", anguloGiro[2])
#rgodot.generarOrden(anguloGiro[0], anguloGiro[1], anguloGiro[2])

print('Despues de esto no and')



def esOrdenValida(x):
    valido= False
    if (x[0]=='E' and x[len(x)-1]=='P'):
        if ('A' in x or 'B' in x or 'C' in x):
            if ((x[x.index('A')+1]=='+' or x[x.index('A')+1]=='-')  and (x[x.index('B')+1]=='+' or x[x.index('B')+1]=='-') and (x[x.index('C')+1]=='+' or x[x.index('C')+1]=='-')):
                if ((1<=abs((x.index('A')+1)-x.index('B'))<=4) and (1<=abs((x.index('B')+1)-x.index('C'))<=4) and (1<=abs((x.index('C')+1)-x.index('P'))<=4)):
                    guardarAngulo(x)
                    valido=True
                    return (valido)
                else:
                    print("Comando inválido") 
                    return(valido)            
                            
                            
                            #Probar de usar Catch errors          
        #diferencias entre A y B y A y C y B y C
        #luego hacer que si las posicions +2 +3 y +4 luego de la letra son numeros con un for y usando isdigit
                        #print("Acá hay una A")
                    
            #########################Funcion guardarAngulo
                    #poner rbt.RecibirOrden dentro de la clase robot
                                            # CAMBIAR W POR rbt.RecibirOrden()
def guardarAngulo(orden):

    anguloGiro[0]=int (orden[(orden.index('A')+1):(orden.index('B'))])
    print=("angulo 1 ", anguloGiro[0])
    anguloGiro[1]=int (orden[(orden.index('B')+1):(orden.index('C'))])
    print=("angulo 2 ", anguloGiro[1])
    anguloGiro[2]=int (orden[(orden.index('C')+1):(orden.index('P'))])
    print=("angulo 3 ", anguloGiro[2])
    #rgodot.generarOrden(anguloGiro[0], anguloGiro[1], anguloGiro[2])

esOrdenValida(orden)
