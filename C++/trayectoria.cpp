#include "trayectoria.h"
#include "tiempo.h"

float x;
float y;
const double PI = 3.141592; 

Trayectoria::Trayectoria(){}
Trayectoria::~Trayectoria(){}

bool Trayectoria::esOrdenValida(string x,Trayectoria * trayec){
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
  trayec->guardarAngulo(x);
  //Tiempo una vez ya guardado los ángulos
  Tiempo::medirTime();
  return true;
}

void Trayectoria::guardarAngulo(string x,Trayectoria * trayec){
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
        int angle;
        istringstream(aux)>>angle;

        if(x[index]=='A') anguloGiro[0]=angle;
        if(x[index]=='B') anguloGiro[1]=angle;
        if(x[index]=='C') anguloGiro[2]=angle;

        
        Tiempo::setActivityTime(abs(angle)*0.01);
        Tiempo::medirTime();
        posicion(anguloGiro[0],anguloGiro[1],anguloGiro[2]);
      break;
    }
  }
}

double Trayectoria::setPosicionx(int angulo,Trayectoria * trayec){
    return (cos(angulo*PI/180));
}

double Trayectoria::setPosiciony(int angulo,Trayectoria * trayec){
    return (cos(angulo*PI/180));
}

double Trayectoria::setPosicionz(int angulo,Trayectoria * trayec){
    return (cos(angulo*PI/180));
}

void Trayectoria::posicion(int a, int b, int c,Trayectoria * trayec){
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

void Trayectoria::setEstado(bool estado,Trayectoria * trayec){
  this->estado = estado; //1-conectado 0-desconectado
}

bool Trayectoria::getEstado(Trayectoria * trayec){
  return this->estado; //1-activo 0-inactivo
}

void Trayectoria::setConexion(bool conexion,Trayectoria * trayec){
  this->conexion = conexion;
}

bool Trayectoria::getConexion(Trayectoria * trayec){
  return conexion;
}