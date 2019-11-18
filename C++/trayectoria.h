#ifndef TRAYECTORIA_H
#define TRAYECTORIA_H

#pragma once
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

public:
    Trayectoria();
    ~Trayectoria();
    bool esOrdenValida(string);
    void guardarAngulo(string);
    double setPosicionx(int);
    double setPosiciony(int);
    void posicion2d(int,int,int);
};


#endif /* TRAYECTORIA_H */

