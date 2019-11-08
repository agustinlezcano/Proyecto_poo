#include "trayectoria.h"

float x;
float y;
enum dir{Norte,Oeste,Sur,Este};
int direccion=Norte;
void moverIzq(char);
void moverDer(char);
void avanzar(char);
void retroceder(char);
void girar(char);

Trayectoria::Trayectoria(){}
Trayectoria::~Trayectoria(){}

bool Trayectoria::esOrdenValida(string o){
//Casos de orden invalida:
//1- No comienza con C o termina con P
//2- Hay caracteres invalidos
//3- El siguiente caracter de I,D,A,R es distinto de un nro
//4 -El siguiente caracter de G(giro) es distinto de 1(antih) o 2(horario)
  for(int i=0;i<o.length();i++){
    if (((o[0]!='C' || o[o.length()-1]!='P'))
      || ((i!=0 && i!=o.length()-1)&&(o[i]!='I' && o[i]!='D' && o[i]!='A' &&
          o[i]!='R' && o[i]!='G' && o[i]!='E')&&(o[i]-'0'>9 || o[i]-'0'<0))
      || ((o[i-1]=='I' || o[i-1]=='D' ||o[i-1]=='A' || o[i-1]=='R')&&
          (o[i]-'0'>9 || o[i]-'0'<0))
      || (o[i-1]=='G' && ((o[i]-'0' !=1)&&(o[i]-'0' !=2))))
         return false; //x -'0' (x del tipo char) convierte a int teniendo como referencia '0' de ASCII a 0 como entero 
  }
  return true;
}

void Trayectoria::setOrdenActual(string ordenActual){
  this->ordenActual = ordenActual;
}

void Trayectoria::ejecutarOrden(){
  for(int i=1;i<ordenActual.length()-1;i+=2){ //saltea los numeros
    switch (ordenActual[i]){
      case(IZQUIERDA):
        moverIzq(ordenActual[i+1]);
        Ordenes.push_back("IZQUIERDA");
        cantMov[0]+=1;       
        break;
      case(DERECHA):
        moverDer(ordenActual[i+1]);
        Ordenes.push_back("DERECHA");
        cantMov[1]+=1;
        break;
      case(AVANZAR):
        avanzar(ordenActual[i+1]);
        Ordenes.push_back("AVANZAR");
        cantMov[2]+=1;
        break;
      case(RETROCEDER):
        retroceder(ordenActual[i+1]);
        Ordenes.push_back("RETROCEDER");
        cantMov[3]+=1;
        break;
      case(GIRAR):
        girar(ordenActual[i+1]);
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

void moverIzq(char unidades){
    x -=  4.25*float(unidades-'0');
}
void moverDer(char unidades){
    x += 4.25*float(unidades-'0');
}
void avanzar(char unidades){
    y += 4.25*float(unidades-'0');
}
void retroceder(char unidades){
    y -= 4.25*float(unidades-'0');
}
void girar(char sentido){
  if(sentido-'0' == 1){
    if(direccion <= Este) direccion--;
    if(direccion == Norte) direccion = Este;
  }
  if(sentido-'0' == 2){
    if(direccion>=Norte) direccion++;
    if(direccion==Este) direccion = Norte;
  }
}
