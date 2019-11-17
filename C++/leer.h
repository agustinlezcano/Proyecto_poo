#ifndef LEER_H
#define LEER_H

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class Leer{
public:
    void read(string txt);
    string get_orden();
private:
    string orden;
};

#endif /* LEER_H */

