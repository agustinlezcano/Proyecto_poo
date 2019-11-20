#include "articulacion.h"

Articulacion::Articulacion() {}
Articulacion ::~Articulacion() {}

void Articulacion::Inicio() {
	Articulacion::setEstado(true); // Inactivo
	cout << "Estado del efector final: " << Articulacion::getEstadostr() << endl;
}

bool Articulacion::getEstado() {
	return this->Estado;
}

void Articulacion::setEstado(bool Nuevo_Estado) {
	this->Estado = Nuevo_Estado;
}

string Articulacion::getEstadostr() {
	if (this->Estado == true) {
		return "INACTIVO (libre)";
	} else {
		return "ACTIVO (en proceso)";
	}
}

bool Articulacion::esOrdenValida(string x, string tipoEfector){
  cout << "Efector: " << tipoEfector << endl;
//Casos de orden invalida:
//no comienza con E o termina con P
//hay caracteres invalidos
//el siguiente caracter de A y V es distinto de +,-
//el siguiente caracte de +,- es distinto de un nro
  for(int i=0;i<x.length();i++){
    if ((x[0]!='E' || x[x.length()-1]!='P')
      || ((i!=0 && i!=x.length()-1)&&(x[i]!='A' && x[i]!='V' && x[i]!='R'  
          && x[i]!='+' && x[i]!='-' && (x[i]-'0'>9 || x[i]-'0'<0)))
      || ((x[i-1]=='A' || x[i-1]=='V'||x[i-1]=='R')&&(x[i]!='-' && x[i]!='+'))
      || ((x[i-1]=='+' || x[i-1]=='-')&&(x[i]-'0'>9 || x[i]-'0'<0)))
      return false; 
  }
  guardarAngulo(x);
  //Tiempo una vez ya guardado los ángulos
  //medirtime();
  //Tiempo::medirtime();
  return true;
}

void Articulacion::guardarAngulo(string x){
  int index;
  
  for(int i=1;i<x.length()-1;i++){
    string aux;
    switch(int(x[i])){
      case(65):
      case(86):
      case(82):
        index=i;
        while(x[i+1]!='A' && x[i+1]!='V'&& x[i+1]!='R'&& x[i+1]!='P'){
          aux += x[i+1];
          i++;
        }
        if(x[index]=='A') istringstream(aux)>>anguloGiro[0];
        if(x[index]=='V') istringstream(aux)>>anguloGiro[1];
        if(x[index]=='R') istringstream(aux)>>anguloGiro[2];
        
        //Lo coloque acá solo para guardar valores de ángulos válidos.
        //medirtime();
        //Tiempo::medirtime();
        //posicion2d(anguloGiro[0],anguloGiro[1],anguloGiro[2]);
      break;
    }
  }
}

void Articulacion::setAcciones(string x){
    string accion = "[Empezar";
    for(int index=1;index<x.length()-1;index++){
        if ((x[index]=='A')and(x[index+1]=='+')){
            accion.append(" Abrir");
          }
            if ((x[index]=='A')and(x[index+1]=='-')){
            accion.append(" Cerrar");
          }
            if (x[index]=='V'){
            accion.append(" Cambiar_velocidad");
          }
            if (x[index]=='R'){
            accion.append(" Rotar");
          }
    }
    accion.append(" Parar]");
    acciones = accion;
}

void Articulacion::getAcciones(Articulacion * obj){
    acciones = obj->acciones;
}
