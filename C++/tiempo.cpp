#include "tiempo.h"

double Tiempo::gettime() {
    return this->time;
}

void Tiempo::settime(double Nuevo_time) {
    this->time = Nuevo_time;
}

double Tiempo::gettime0() {
    return this->time0;
}

void Tiempo::settime0(double Nuevo_time) {
    this->time0 = Nuevo_time;
}

void Tiempo::medirtime(){
    double t = clock();
    Tiempo::settime(t);
    stringstream ss;
    double segundos = (double(Tiempo::gettime() - Tiempo::gettime0()) / CLOCKS_PER_SEC);
    ss << "Instante de inicio orden: " << segundos << " seg" << endl;
    cout << ss.str() << endl;
}
