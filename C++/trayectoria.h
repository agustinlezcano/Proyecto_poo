#pragma once
#include <cstdlib>
#include <iostream>
#include <list>
#include <string>
#include <sstream>
#include <cmath>
#include <ctime>
#include "movimiento.h"
using namespace std;

class Trayectoria{
private:
    string ordenActual;
    list <string> Ordenes;
    float distanciaTotal;
    int cantMov[5];
    int anguloGiro[3];
    
    double time0;
    double time;
public:
    Trayectoria();
    ~Trayectoria();
    void actualizarEstado();
    void ejecutarOrden();
    bool esOrdenValida(string);
    float getDistanciaTotal();
    void setOrdenActual(string); 
    string getOrdenActual();
    list<string> getOrdenes();
    void getCantOrdenes();
    void guardarAngulo(string);
    void tiempo(int);
    void medirtime();
    double gettime();
    void settime(double time);	
    double gettime0();
    void settime0(double time);
    double setPosicionx(int);
    double setPosiciony(int);
    void posicion2d(int,int,int);
};