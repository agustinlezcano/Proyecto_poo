#include "trayectoria.h"
#include "tiempo.h"

const double PI = 3.141592; 

Trayectoria::Trayectoria(){}
Trayectoria::~Trayectoria(){}

bool Trayectoria::esOrdenValida(string x){
//Casos de orden invalida:
//no comienza con E o termina con P
//hay caracteres invalidos
//el siguiente caracter de A,B,C es distinto de +,-
//el siguiente caracte de +,- es distinto de un nro
  for(int i=0;i<x.length();i++){
    if ((x[0]!='E' || x[x.length()-1]!='P')
      || ((i!=0 && i!=x.length()-1)&&(x[i]!='A' && x[i]!='B' && x[i]!='C' 
          && x[i]!='+' && x[i]!='-' && (x[i]-'0'>9 || x[i]-'0'<0)))
      || ((x[i-1]=='A' || x[i-1]=='B' ||x[i-1]=='C')&&(x[i]!='-' && x[i]!='+'))
      || ((x[i-1]=='+' || x[i-1]=='-')&&(x[i]-'0'>9 || x[i]-'0'<0)))
      return false; 
  }
  guardarAngulo(x);
  //Tiempo una vez ya guardado los ángulos
  Tiempo::medirTime();
  return true;
}

void Trayectoria::guardarAngulo(string x){
  int index;
  for(int i=1;i<x.length()-1;i++){
    string aux;
    switch(int(x[i])){
      case(65):
      case(66):
      case(67):
        index=i;
        while(x[i+1]!='A' && x[i+1]!='B'&& x[i+1]!='C'&& x[i+1]!='P'){
          aux += x[i+1];
          i++;
        }
        if(x[index]=='A') istringstream(aux)>>anguloGiro[0];
        if(x[index]=='B') istringstream(aux)>>anguloGiro[1];
        if(x[index]=='C') istringstream(aux)>>anguloGiro[2];
        
        Tiempo::setActivityTime(anguloGiro[0]*0.01);
        Tiempo::setActivityTime(anguloGiro[1]*0.01);
        Tiempo::setActivityTime(anguloGiro[2]*0.01);
        //Lo coloque acá solo para guardar valores de ángulos válidos.
        Tiempo::medirTime();
        posicion(anguloGiro[0],anguloGiro[1],anguloGiro[2]);
      break;
    }
  }
}

double Trayectoria::setPosicionx(int angulo){
    //La librería cmath trabaja con radianes por eso hay que hacer la respectiva conversión.
    return (cos(angulo*PI/180));
}

double Trayectoria::setPosiciony(int angulo){
    //La librería cmath trabaja con radianes por eso hay que hacer la respectiva conversión.
    return (cos(angulo*PI/180));
}

double Trayectoria::setPosicionz(int angulo){
    //La librería cmath trabaja con radianes por eso hay que hacer la respectiva conversión.
    return (cos(angulo*PI/180));
}

void Trayectoria::posicion(int a, int b, int c){
    //Longitudes de cada brazo
    double d1=10,d2=5,d3=4.5;
    //Posición Brazo A en el plano.
    double p1x=0;
    double p1y=0;
    double p1z=0;
    //Posición Brazo B en el plano.
    double p2x=d2*(Trayectoria::setPosicionx(b));
    double p2y=d2*(Trayectoria::setPosiciony(b));
    double p2z=d2*(Trayectoria::setPosicionz(b));
    //Posición Brazo C en el plano.
    double p3x=d3*(Trayectoria::setPosicionx(c)) + p2x;
    double p3y=d3*(Trayectoria::setPosiciony(c)) + p2y;
    double p3z=d3*(Trayectoria::setPosicionz(c)) + p2z;
}

void Trayectoria::setAcciones(string x){
    string accion = "[";
    for(int index=1;index<x.length()-1;index++){
        if (x[index]=='A'){
            accion.append(" Articulación_A");
          }
            if (x[index]=='B'){
            accion.append(" Articulación_B");
          }
            if (x[index]=='C'){
            accion.append(" Articulación_C");
          }
    }
    accion.append(" ]");
    acciones = accion;
}

void Trayectoria::setEstado(bool estado){
  this->estado = estado; //1-conectado 0-desconectado
}

bool Trayectoria::getEstado(){
  return this->estado; //1-activo 0-inactivo
}

void Trayectoria::setConexion(bool conexion){
  this->conexion = conexion;
}

bool Trayectoria::getConexion(){
  return conexion;
}

