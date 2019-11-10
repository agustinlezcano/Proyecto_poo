#include "trayectoria.h"

float x;
float y;

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
  return true;
}

void Trayectoria::setOrdenActual(string ordenActual){
  this->ordenActual = ordenActual;
}

void Trayectoria::ejecutarOrden(){
  for(int i=1;i<ordenActual.length()-1;i+=2){ //saltea los numeros
    switch (ordenActual[i]){
      case(IZQUIERDA):
        Ordenes.push_back("IZQUIERDA");
        cantMov[0]+=1;       
        break;
      case(DERECHA):
        Ordenes.push_back("DERECHA");
        cantMov[1]+=1;
        break;
      case(AVANZAR):
        Ordenes.push_back("AVANZAR");
        cantMov[2]+=1;
        break;
      case(RETROCEDER):
        Ordenes.push_back("RETROCEDER");
        cantMov[3]+=1;
        break;
      case(GIRAR):
        Ordenes.push_back("GIRAR");
        cantMov[4]+=1;
        break;
    }
    if(ordenActual[i]!=GIRAR) actualizarEstado();
    x=0;
    y=0;
  }
}

void Trayectoria::actualizarEstado(){
  distanciaTotal += sqrt(x*x + y*y);
}

float Trayectoria::getDistanciaTotal(){
  return distanciaTotal;
}

string Trayectoria::getOrdenActual(){
  return ordenActual;
}

list<string> Trayectoria::getOrdenes(){
  return Ordenes;
}

void Trayectoria::getCantOrdenes(){
  cout << "Cantidad de movimientos:" << endl << 
    "IZQUIERDA: " << cantMov[0] << endl <<
    "DERECHA: " << cantMov[1] << endl << 
    "AVANZAR: " << cantMov[2] << endl <<
    "RETROCEDER: " << cantMov[3] << endl <<
    "GIRAR: " << cantMov[4] << endl; 
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
      break;
    }
  }
}