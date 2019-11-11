#include <iostream>
#include <string>
#include <cstdlib>
#include "trayectoria.h"
#include "articulacion.h"

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
	
    cout << "Desea inicializar?? Y / any:  " << endl;
    cin >> inicializacion;
    if (inicializacion == "y" || inicializacion == "Y") {
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