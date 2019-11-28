#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include "trayectoria.h"
#include "articulacion.h"
#include "tiempo.h"
#include "leer.h"
#include "lib/XmlRpc.h"

using namespace XmlRpc;

void emitirReporte(Trayectoria *trayec,Tiempo *T,string,string);
string controlBrazo();
string controlPinza();

int main(int argc, char* argv[]){
    Trayectoria *trayec = new Trayectoria();
    Tiempo *T = new Tiempo();
    string reportArticulacion, reportAcciones;
    
    int port = atoi(argv[2]);
    // Create a client and connect to the server at hostname:port
    XmlRpcClient client(hostname, port);

    XmlRpcValue noArgs, codigoB, codigoP, result;

    int ej;
    bool band = true;
    while (band) {
        std::cout <<"==========================================="<<std::endl;
        std::cout << "             ORDENES             " << std::endl <<
        "1 - Control articulaciones" << std::endl <<
        "2 - Control efector final" << std::endl <<
        "3 - Generar reporte" << std::endl <<
        "0 - Salir"<< std::endl;
        std::cout <<"==========================================="<<std::endl;
        std::cout << "Ingrese el número de orden a realizar: ";
            std::cin >> ej;
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
        default: std::cout << "Orden NO válida, vuelva a intentarlo." << std::endl;
        break;
        }
    }    
}

string controlBrazo(){
    
    string modo;
    std::cout << std::endl << "Ingrese modo:" << std::endl <<
    "A - Modo Automático" << std::endl <<
    "M - Modo Manual" << std::endl;
    std::cin >> modo;
    


    Trayectoria * trayec= new Trayectoria();
    Leer * lectura = new Leer();
    Trayectoria * dato1 = new Trayectoria;
    
    int angulo1,angulo2,angulo3;
    Trayectoria * ang1 = new Trayectoria;
    //ESTOY ACÁ
    double timer1,timer2,timer3;
    //Tiempo * timer1 = new Tiempo;
    //Tiempo * timer2 = new Tiempo;
    //Tiempo * timer3 = new Tiempo;
    
    string orden;
    if (modo == "A"){
        string archivo;
        bool status = 1; //Inactivo
        while (status==1){
            int aux=0;
            std::cout << std::endl << "1. Cargar rutina \n2. Generar rutina de aprendizaje" << std::endl;
            std::cin >> aux;
            std::cout << "\n" <<std::endl;
            if (aux==2){
                lectura->crear_rutina();
            }
            if (aux==1){
                std::cout << "Ingrese archivo para leer: "<<std::endl;
                std::cin >> archivo;
                orden=lectura->read(archivo);
            
                if (orden!="ERROR"){
                    status = 0;
                }
            }
        }
    };
    
    if (modo == "M"){
        std::cout<< "===========================================" << std::endl;
        std::cout<< "          MOVIMIENTO ARTICULACIONES          " << std::endl;
        std::cout<< "===========================================" << std::endl;
        std::cout << "E - Empezar" << std::endl <<
                "P - Parar" << std::endl <<
                "A - Articulacion A" << std::endl <<
                "B - Articulacion B" << std::endl <<
                "C - Articulacion C" << std::endl <<
                "T para terminar" << std::endl;
        std::cout << std::endl << "Ingrese el número de la acción: " << std::endl;
        std::cin >> orden;
        std::cout << orden << std::endl;
        codigoB=orden;

    }
        
    if(orden=="T"){
        delete trayec;
    }
       
    if(trayec->esOrdenValida(orden)){
        std::cout << "Orden válida" << std::endl << std::endl;
        dato1->setAcciones(orden);
        //std::cout << "Movimientos: " << dato1->acciones<< std::endl;
        //Envía la señal del movimiento del brazo
            client.execute("brazo", codigoB, result);
            std::std::cout << result << std::std::endl;

        ang1->guardarAngulo(orden);
        angulo1 = ang1->angulo1;
        angulo2 = ang1->angulo2;
        angulo3 = ang1->angulo3;
        
        //timer1->Tiempo::setActivityTime(angulo1*0.01);
        //timer2->Tiempo::setActivityTime(angulo2*0.01);
        //timer3->Tiempo::setActivityTime(angulo3*0.01);
        //Velocidad angulas, donde k=0.01 es una constante de proporcionalidad
        timer1 = angulo1*0.01;
        timer2 = angulo2*0.01;
        timer3 = angulo3*0.01;
        
        delete trayec;
    }
    stringstream ss;
    ss << dato1->acciones << "\n"<< "Ángulos: " << ang1->angulo1 <<"," << ang1->angulo2 <<","<< ang1->angulo3 << "\n"<<"Tiempo instántaneo: "<<timer1<<","<<timer2<<","<<timer3;
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
    
    std::cout << "¿Desea inicializar? S / N:  " << std::endl;
    std::cin >> inicializacion;
    if (inicializacion == "s" || inicializacion == "S") {
	ef->Inicio();
    } else {
        std::cout << "Saliendo..." << std::endl;
	ef->setEstado(false); // Falso activo
    }
    
    std::cout << std::endl << "Ingrese modo:" << std::endl <<
    "A - Modo Automático" << std::endl <<
    "M - Modo Manual" << std::endl;
    std::cin >> modo;
    
    if(modo == "A"){
        std::cout << "Ingrese archivo para leer: "<<std::endl;
        std::cin >> archivo;
        orden=lectura->read(archivo);
        
        if(ef->esOrdenValida(orden,efector)){
            std::cout << "Orden válida" << std::endl << std::endl;
            dato->setAcciones(orden);
            std::cout << "Secuencia: " << dato->acciones<< std::endl;
            delete ef;
        }
    }
    
    if (modo == "M"){
        std::cout<< "===========================================" << std::endl;
        std::cout<< "               ACCIONES               " << std::endl;
        std::cout << "E  para Empezar" << std::endl <<
                "P  para Parar" << std::endl <<
                "A+ para Abrir" << std::endl <<
                "A- para Cerrar" << std::endl <<
                "R  para Rotar" << std::endl <<
                "V  para Cambiar velocidad" << std::endl <<
                "T  para Terminar" << std::endl;
        std::cout<< "===========================================" << std::endl;
    
        while (ef->getEstado()) {
            std::cout << "Elija la acción a realizar: " << std::endl;
            std::cin >> orden;
            
            if(orden=="T"){
                delete ef;
                break;
            }
            
            if(ef->esOrdenValida(orden,efector)){
                std::cout << "Orden válida" << std::endl;
                dato->setAcciones(orden);
                std::cout << "Secuencia: " << dato->acciones<< std::endl<< std::endl;
                client.execute("pinza", codigoP, result);
                std::std::cout << result << std::std::endl;

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
    //rep << "Conexion: ";
    //if(trayec->getConexion()) rep << "conectado";
    //else rep << "desconectado";

    //rep << "\nEstado: ";
    //if(trayec->getEstado()) rep << "activado";
    //else rep << "desactivado";
    
    //rep << "\nTiempo acumulado: " << T->getActivityTime();
    //rep << "\nCoordenadas:\nArticulacion A: (";//posicion_artA[0] << ", " << posicion_artA[1] << ", " << posicion_artA[2] << ")"
    //rep << "\nArticulacion B: ("; //posicion_artB[0] << ", " << posicion_artB[1] << ", " << posicion_artB[2] << ")"
    //rep << "\nArticulacion C: ("; //posicion_artC[0] << ", " << posicion_artC[1] << ", " << posicion_artC[2] << ")"
    rep << "\nSecuenciac de articulación: " << reportAcciones << std::endl;
    rep << "\nSecuencia de efector: "<< reportArticulacion << std::endl;
    std::cout << rep.str() << std::endl;
}
