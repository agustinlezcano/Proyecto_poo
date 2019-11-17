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
