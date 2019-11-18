#include <iostream>
#include <string>
#include <cstdlib>
#include "trayectoria.h"
#include "articulacion.h"
#include "tiempo.h"

#include "leer.h"

using namespace std;

void emitirReporte(Trayectoria *);
int controlBrazo();
int controlPinza();

int main(){
    cout <<"==========================================="<<endl;
    cout << "             ORDENES             " << endl << 
        "1 - Control articulaciones" << endl <<
        "2 - Control efector final" << endl <<
        "0 - Salir"<< endl;
    cout <<"==========================================="<<endl;
    int ej;
    bool band = true;
    while (band) {
	cout << "Ingrese el número de orden a realizar: ";
        cin >> ej;
	switch (ej) {
	case (0): band = false;
            break;
	case (1): controlBrazo();
            break;
	case (2): controlPinza();
            break;
	default: cout << "Orden NO válida, vuelva a intentarlo." << endl;
	break;
	}
    }    
}

int controlBrazo(){
    
    string modo;
    cout << endl << "Ingrese modo:" << endl << 
    "A - Modo Automático" << endl <<
    "M - Modo Manual" << endl;
    cin >> modo;
    
    Trayectoria * trayec= new Trayectoria();
    Leer * lectura = new Leer();
    
    string orden;
    if (modo == "A"){
        string archivo;
        bool status = 1; //Inactivo
        while (status==1){
            int aux=0;
            cout << endl << "1. Cargar rutina \n2. Generar rutina de aprendizaje" << endl;
            cin >> aux;
            cout << "\n" <<endl;
            if (aux==2){
                lectura->crear_rutina();
            }
            if (aux==1){
                cout << "Ingrese archivo para leer: "<<endl;
                cin >> archivo;
                orden=lectura->read(archivo);
            
                if (orden!="ERROR"){
                    status = 0;
                }
            }
        }
    };
    
    
    while(true){
        if (modo == "M"){
            cout << endl << "Ingrese el número de la acción:" << endl << 
            "E - Empezar" << endl <<
            "P - Parar" << endl <<
            "A - Articulacion A" << endl <<
            "B - Articulacion B" << endl <<
            "C - Articulacion C" << endl <<
            "T para terminar" << endl;
            cin >> orden;
            cout << orden << endl;
        }
        
        if(orden=="T"){
            delete trayec;
            break;
        }
       
        if(trayec->esOrdenValida(orden)){
            cout << "Orden válida" << endl << endl;
        }
        if (modo == "A"){
            orden="T";
        }
    }
    return 0;
}

int controlPinza() {
    
    string modo;
    Leer * lectura = new Leer();
    
    string orden, archivo;
    string inicializacion;
    
    Articulacion *ef;
    ef = new Articulacion();
	
    cout << "¿Desea inicializar? S / N:  " << endl;
    cin >> inicializacion;
    if (inicializacion == "s" || inicializacion == "S") {
	ef->Inicio();
    } else {
	cout << "Saliendo..." << endl;
	ef->setEstado(false); // Falso activo
    }
    
    cout << endl << "Ingrese modo:" << endl << 
    "A - Modo Automático" << endl <<
    "M - Modo Manual" << endl;
    cin >> modo;
    
    if(modo == "A"){
        cout << "Ingrese archivo para leer: "<<endl;
        cin >> archivo;
        orden=lectura->read(archivo);
        
        if(ef->esOrdenValida(orden)){
            cout << "Orden válida" << endl << endl;
        }
    }
    
    if (modo == "M"){
    
        while (ef->getEstado()) {
            cout << "Elija la acción a realizar: " << endl <<
                     "E para Empezar" << endl <<
                     "P para Parar" << endl <<
                     "A+ para Abrir" << endl <<
                     "A- para Cerrar" << endl <<
                     "R para Rotar" << endl <<
                     "V para Cambiar velocidad" << endl <<
                     "T para Terminar" << endl;
            cin >> orden;
            
            if(orden=="T"){
                delete ef;
                break;
            }
            
            if(ef->esOrdenValida(orden)){
                cout << "Orden válida" << endl << endl;
                delete ef;
            }
            if (modo == "A"){
                orden="T";
            }
        } 
    }
    return 0;
}