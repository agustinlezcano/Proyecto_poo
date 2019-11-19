#include "tiempo.h"

double Tiempo::getTime() {
    return this->time;
}

void Tiempo::setTime(double new_time) {
    this->time = new_time;
}

double Tiempo::getTime0() {
    return this->time0;
}

void Tiempo::setTime0(double new_time) {
    this->time0 = new_time;
}

void Tiempo::medirTime(){
    double t = clock();
    Tiempo::setTime(t);
    stringstream ss;
    double segundos = (double(Tiempo::getTime() - Tiempo::getTime0()) / CLOCKS_PER_SEC);
    ss << "Instante de inicio orden: " << segundos << " seg" << endl;
    cout << ss.str() << endl;
}

void Tiempo::setActivityTime(double t){
    timeOp = ++t;
}

void Tiempo::setOrdenesTime(double t){
    timeOrdenes.insert(timeOrdenes.end(),t);
}