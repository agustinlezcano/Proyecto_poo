#include <iostream>
#include <string>
#include <cstdlib>
#include "trayectoria.h"

using namespace std;

void emitirReporte(Trayectoria *);

int main(){
    Trayectoria * trayec= new Trayectoria();
    while(true){
        string orden;
        cout << "*************" << endl << "Ingrese orden:" << endl << 
        "E - Empezar" << endl <<
        "P - Parar" << endl <<
        "A - Articulacion A" << endl <<
        "B - Articulacion B" << endl <<
        "C - Articulacion C" << endl <<
        "T para terminar" << endl;
        cin >> orden;
        if(orden=="T"){
            delete trayec;
            break;
        }
        if(orden=="R"){
            emitirReporte(trayec);
            continue;
        }
        if(trayec->esOrdenValida(orden)){
            cout << "Orden valida" << endl << endl;
            trayec->setOrdenActual(orden);
            trayec->ejecutarOrden();
        }
    }
    return 0;
}

void emitirReporte(Trayectoria * T){
    cout << endl << "Distancia recorrida: " << T->getDistanciaTotal() << " mm" << endl;
    list<string> ordenes = T->getOrdenes();
    cout << "Lista de ordenes:" << endl;
    for(list<string>::iterator it=ordenes.begin();it!=ordenes.end();++it){
        cout << *it << ", ";
    }
    cout<< endl << endl;
    T->getCantOrdenes();
}
