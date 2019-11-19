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
    double posicion_artB[3];
    double posicion_artC[3];
public:
    Trayectoria();
    ~Trayectoria();
    bool esOrdenValida(string);
    void guardarAngulo(string);
    double setPosicionx(int);
    double setPosiciony(int);
    double setPosicionz(int);
    void posicion(int,int,int);
};


#endif /* TRAYECTORIA_H */

