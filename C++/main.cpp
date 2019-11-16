#include <iostream>
#include <string>
#include <cstdlib>
#include "trayectoria.h"
#include "articulacion.h"
#include "tiempo.h"
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
    Trayectoria * trayec= new Trayectoria();
    while(true){
        string orden;
        cout << endl << "Ingrese el número de la acción:" << endl << 
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
            cout << "Orden válida" << endl << endl;
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

int controlPinza() {
    int accion, counter;
    string inicializacion;
    stringstream ss;
    float vel;
    enum accion {
	ABRIR, CERRAR, ROTAR, CAMBIAR_VELOCIDAD
    };
    Articulacion *ef;
    ef = new Articulacion();
	
    cout << "¿Desea inicializar?? S / N:  " << endl;
    cin >> inicializacion;
    if (inicializacion == "s" || inicializacion == "S") {
	ef->Inicio();
    } else {
	cout << "Saliendo..." << endl;
	ef->setEstado(false); // Falso activo
    }
    while (ef->getEstado()) {
	cout << "Elija la acción a realizar: " << endl
		<< "1. ABRIR" << endl
		<< "2. CERRAR" << endl
		<< "3. ROTAR" << endl
		<< "4. CAMBIAR VELOCIDAD" << endl
		<< "0. TERMINAR" << endl;
	cin >> accion;
	if (accion == 0) {
		ef->parada();
		break;
	}
	if (accion == 4) {
		cout << "Ingrese velocidad de giro: " << endl;
		cin >> vel;
	}
	if (accion < 0 || accion > 4) {
		cout << "Acción NO válida, vuelva a intentarlo." << endl;
		break;
	}
	cout << "Ingrese la cantidad de ciclos que durará la acción seleccionada: ";
	cin >> counter;
	for (int i = 0; i < counter; i++) {
            switch (accion) {
            case ABRIR: ef->Abrir(i, counter);
		break;
            case CERRAR: ef->Cerrar(i, counter);
		break;
            case ROTAR: ef->Rotar(i, counter);
		break;
            case CAMBIAR_VELOCIDAD: ef->Cambiar_Velocidad(vel, i, counter);
		break;
            default: 
		break;
            }
            ss << endl;
            ss << "Estado de la Pinza: " << ef->getEstadostr() << endl;
            ss << "Operación en proceso: " << ef->getOperacion() << endl;
            ss << "Ciclo actual: " << i + 1 << endl;
            ss << "Ciclos prefijados: " << counter << endl;
            ss << "Ciclos totales: " << ef->getciclos() << endl;
            ss << "Velocidad actual: " << ef->getvelocidad() << endl;
            cout << ss.str() << endl << endl;
            ss.str("");
	}
    }
    delete ef;
    return 0;
}