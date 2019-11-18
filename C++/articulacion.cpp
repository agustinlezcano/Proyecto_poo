#include "articulacion.h"

Articulacion::Articulacion() {}
Articulacion ::~Articulacion() {}

void Articulacion::Inicio() {
	Articulacion::setEstado(true); // Inactivo
	cout << "Estado del efector final: " << Articulacion::getEstadostr() << endl;
	ciclos_totales = 0;
}

void Articulacion::Abrir(int actual, int counter) {
	Articulacion::setEstado(false); // Activo
	Operacion = "Abrir"; //Abre sus pinzas
	if (actual + 1 == counter) {
		Articulacion::setEstado(true); // Inactivo
	}
	ciclos_totales++;
}

void Articulacion::Cerrar(int actual, int counter) {
	Articulacion::setEstado(false); // Activo
	Operacion = "Cerrar"; //Cierra sus pinzas
	if (actual + 1 == counter) {
		Articulacion::setEstado(true); // Inactivo
	}
	ciclos_totales++;
}

void Articulacion::Rotar(int actual, int counter) {
	Articulacion::setEstado(false); // Activo
	Operacion = "Rotar" ;
	if (actual + 1 == counter) {
		Articulacion::setEstado(true); // Inactivo
	}
	ciclos_totales++;
}

void Articulacion::Cambiar_Velocidad(float Nueva_velocidad, int actual, int counter){
	Articulacion::setEstado(false); // Activo
	Operacion = "Cambiar Velocidad";
	velocidad = Nueva_velocidad;
	if (actual + 1 == counter) {
		Articulacion::setEstado(true); // Inactivo
	}
	ciclos_totales++;
}

float Articulacion::getvelocidad() {
	return this->velocidad;
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

int Articulacion::getciclos() {
	return this->ciclos_totales;
}

void Articulacion::sumarciclos() {
	this->ciclos_totales++;
}

string Articulacion::getOperacion() {
	return this->Operacion;
}

void Articulacion::parada() {
	Articulacion::setEstado(false); // Activo
}

//Empecé a modificar acá

bool Articulacion::esOrdenValida(string x){
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
