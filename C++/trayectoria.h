#ifndef TRAYECTORIA_H
#define TRAYECTORIA_H

#include <cstdlib>
#include <iostream>
#include <list>
#include <string>
#include <sstream>
#include <cmath>
#include <ctime>
#include "movimiento.h"
#include "tiempo.h"
using namespace std;

class Trayectoria: public Tiempo {
private:
    int anguloGiro[3]; 
    //la articulacion A no cambia de posicion, solo rota. Es nuestra referencia (0,0,0)
    double posicion_artA[3];
    double posicion_artB[3];
    double posicion_artC[3];
    bool conexion;
    bool estado;
public:
    Trayectoria();
    ~Trayectoria();
    void setEstado(bool,Trayectoria *);
    bool getEstado(Trayectoria *);
    void setConexion(bool,Trayectoria *);
    bool getConexion(Trayectoria *);
    bool esOrdenValida(string,Trayectoria *);
    void guardarAngulo(string,Trayectoria *);
    double setPosicionx(int,Trayectoria *);
    double setPosiciony(int,Trayectoria *);
    double setPosicionz(int,Trayectoria *);
    void posicion(int,int,int,Trayectoria *);
};


#endif /* TRAYECTORIA_H */

