#include "trayectoria.h"

float x;
float y;
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
  medirtime();
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
        
        //Lo coloque acá solo para guardar valores de ángulos válidos.
        medirtime();
        posicion2d(anguloGiro[0],anguloGiro[1],anguloGiro[2]);
      break;
    }
  }
}

double Trayectoria::gettime() {
    return this->time;
}

void Trayectoria::settime(double Nuevo_time) {
    this->time = Nuevo_time;
}

double Trayectoria::gettime0() {
    return this->time0;
}

void Trayectoria::settime0(double Nuevo_time) {
    this->time0 = Nuevo_time;
}

void Trayectoria::medirtime(){
    double t = clock();
    Trayectoria::settime(t);
    stringstream ss;
    double segundos = (double(Trayectoria::gettime() - Trayectoria::gettime0()) / CLOCKS_PER_SEC);
    ss << "Instante de inicio orden: " << segundos << " seg" << endl;
    cout << ss.str() << endl;
}

double Trayectoria::setPosicionx(int angulo){
    const double PI = 3.141592; 
    //La librería cmath trabaja con radianes por eso hay que hacer la respectiva conversión.
    return (cos(angulo*PI/180));
}

double Trayectoria::setPosiciony(int angulo){
    //La librería cmath trabaja con radianes por eso hay que hacer la respectiva conversión.
    return (sin(angulo*PI/180));
}

void Trayectoria::posicion2d(int a, int b, int c){
    //Longitudes de cada brazo
    double d1=10,d2=5,d3=4.5;
    //Posición Brazo A en el plano.
    double p1x=d1*(Trayectoria::setPosicionx(a));
    double p1y=d1*(Trayectoria::setPosiciony(a));
    //Posición Brazo B en el plano.
    double p2x=d2*(Trayectoria::setPosicionx(b)) + p1x;
    double p2y=d2*(Trayectoria::setPosiciony(b)) + p1y;
    //Posición Brazo C en el plano.
    double p3x=d3*(Trayectoria::setPosicionx(c)) + p2x;
    double p3y=d3*(Trayectoria::setPosiciony(c)) + p2y;
}