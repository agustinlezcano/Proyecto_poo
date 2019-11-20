#ifndef TIEMPO_H
#define TIEMPO_H

#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
#include <ctime>
#include <list>
using namespace std;

class Tiempo{
private:
    double time0;
    double time;
    double timeOp;
    list <double> timeOrdenes;
    
public:
    Tiempo ();
    ~Tiempo();
    void tiempo(int); //no hace nada (?)
    void medirTime();
    double getTime();
    void setTime(double);	
    double getTime0();
    void setTime0(double);
    void setActivityTime(double);
    double getActivityTime();
    void setOrdenesTime(double);
};
#endif /* TIEMPO_H */