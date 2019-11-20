#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include "trayectoria.h"
#include "articulacion.h"
#include "tiempo.h"
#include "leer.h"

using namespace std;

void emitirReporte(Trayectoria *trayec,Tiempo *T,string,string);
string controlBrazo();
string controlPinza();

int main(){
    Trayectoria *trayec = new Trayectoria();
    Tiempo *T = new Tiempo();
    string reportArticulacion, reportAcciones;
    
    int ej;
    bool band = true;
    while (band) {
        cout <<"==========================================="<<endl;
        cout << "             ORDENES             " << endl << 
        "1 - Control articulaciones" << endl <<
        "2 - Control efector final" << endl <<
        "3 - Generar reporte" << endl <<
        "0 - Salir"<< endl;
        cout <<"==========================================="<<endl;
        cout << "Ingrese el número de orden a realizar: ";
            cin >> ej;
        switch (ej) {
        case (0): band = false;
                break;
        case (1):
                reportAcciones=controlBrazo();
                break;
        case (2): 
                reportArticulacion=controlPinza();
                break;
        case (3): emitirReporte(trayec,T,reportAcciones,reportArticulacion);
                break;
        default: cout << "Orden NO válida, vuelva a intentarlo." << endl;
        break;
        }
    }    
}

string controlBrazo(){
    
    string modo;
    cout << endl << "Ingrese modo:" << endl << 
    "A - Modo Automático" << endl <<
    "M - Modo Manual" << endl;
    cin >> modo;
    
    Trayectoria * trayec= new Trayectoria();
    Leer * lectura = new Leer();
    Trayectoria * dato1 = new Trayectoria;
    
    int angulo1,angulo2,angulo3;
    Trayectoria * ang1 = new Trayectoria;
    
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
    
    if (modo == "M"){
        cout<< "===========================================" << endl;
        cout<< "          MOVIMIENTO ARTICULACIONES          " << endl;
        cout<< "===========================================" << endl;
        cout << "E - Empezar" << endl <<
                "P - Parar" << endl <<
                "A - Articulacion A" << endl <<
                "B - Articulacion B" << endl <<
                "C - Articulacion C" << endl <<
                "T para terminar" << endl;
        cout << endl << "Ingrese el número de la acción: " << endl;
        cin >> orden;
        cout << orden << endl;
    }
        
    if(orden=="T"){
        delete trayec;
    }
       
    if(trayec->esOrdenValida(orden)){
        cout << "Orden válida" << endl << endl;
        dato1->setAcciones(orden);
        cout << "Movimientos: " << dato1->acciones<< endl;
        
        ang1->guardarAngulo(orden);
        angulo1 = ang1->angulo1;
        angulo2 = ang1->angulo2;
        angulo3 = ang1->angulo3;
        
        delete trayec;
    }
    stringstream ss;
    ss << dato1->acciones << "\n"<< "Ángulos: " << ang1->angulo1 <<"," << ang1->angulo2 <<","<< ang1->angulo3;
    return ss.str();
}

string controlPinza() {
    
    string modo;
    Leer * lectura = new Leer();
    
    string orden, archivo;
    string inicializacion;
    string efector = "pinza";
    
    Articulacion *ef;
    ef = new Articulacion();
    
    Articulacion * dato = new Articulacion;
    
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
        
        if(ef->esOrdenValida(orden,efector)){
            cout << "Orden válida" << endl << endl;
            dato->setAcciones(orden);
            cout << "Secuencia: " << dato->acciones<< endl;
            delete ef;
        }
    }
    
    if (modo == "M"){
        cout<< "===========================================" << endl;
        cout<< "               ACCIONES               " << endl;
        cout << "E  para Empezar" << endl <<
                "P  para Parar" << endl <<
                "A+ para Abrir" << endl <<
                "A- para Cerrar" << endl <<
                "R  para Rotar" << endl <<
                "V  para Cambiar velocidad" << endl <<
                "T  para Terminar" << endl;
        cout<< "===========================================" << endl;
    
        while (ef->getEstado()) {
            cout << "Elija la acción a realizar: " << endl;
            cin >> orden;
            
            if(orden=="T"){
                delete ef;
                break;
            }
            
            if(ef->esOrdenValida(orden,efector)){
                cout << "Orden válida" << endl;
                dato->setAcciones(orden);
                cout << "Secuencia: " << dato->acciones<< endl<< endl;
                delete ef;
            }
        } 
    }
    //delete dato;
    return dato->acciones;
}

void emitirReporte(Trayectoria *trayec,Tiempo *T,string reportAcciones,string reportArticulacion){
// ==================
//     Reporte
// ==================
// Estado de conexión               LISTO
// Estado de actividad del robot    LISTO 
// Instante de tiempo acumulado     LISTO
// Coordenadas de cada articulación NO (Falta guardar angulos)
// Velocidad efector final          NO ()
// Secuencia de movimiento          NO (Carlos lo hace)
    
    stringstream rep;
    rep << "Conexion: ";
    if(trayec->getConexion()) rep << "conectado";
    else rep << "desconectado";

    rep << "\nEstado: ";
    if(trayec->getEstado()) rep << "activado";
    else rep << "desactivado";
    
    rep << "\nTiempo acumulado: " << T->getActivityTime();
    rep << "\nCoordenadas:\nArticulacion A: (";//posicion_artA[0] << ", " << posicion_artA[1] << ", " << posicion_artA[2] << ")"
    rep << "\nArticulacion B: ("; //posicion_artB[0] << ", " << posicion_artB[1] << ", " << posicion_artB[2] << ")"
    rep << "\nArticulacion C: ("; //posicion_artC[0] << ", " << posicion_artC[1] << ", " << posicion_artC[2] << ")"
    rep << "\nSecuenciac de articulación: " << reportAcciones << endl;
    rep << "\nSecuencia de efector: "<< reportArticulacion << endl;
    cout << rep.str() << endl;
}