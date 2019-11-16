#ifndef TIEMPO_H
#define TIEMPO_H

#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
#include <ctime>
using namespace std;

class Tiempo{
private:
    double time0;
    double time;
public:
    void tiempo(int);
    void medirtime();
    double gettime();
    void settime(double time);	
    double gettime0();
    void settime0(double time);
};
#endif /* TIEMPO_H */