#ifndef LEER_H
#define LEER_H

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class Leer{
public:
    string read(string txt);
    void crear_rutina();
private:
    string orden;
};

#endif /* LEER_H */

