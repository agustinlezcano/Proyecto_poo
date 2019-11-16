#ifndef ARTICULACION_H
#define ARTICULACION_H

#include<iostream>
using namespace std;
#include<ctime>
#include<sstream>
#include<string>

int controlPinza(); //Ésto lo uso para el main

class Articulacion {
public:
	Articulacion ();
	~Articulacion ();

	void Inicio();
	void Abrir(int actual, int counter);
	void Cerrar(int actual, int counter);
	void Rotar(int actual, int counter);
	void Cambiar_Velocidad(float Nueva_velocidad, int actual, int counter);
	float getvelocidad();
	bool getEstado();
	void setEstado(bool Nuevo_Estado);
	string getEstadostr();
	int getciclos();
	void sumarciclos();
	string getOperacion();
	void parada();

private:
	float velocidad = 0;
	bool Estado; // Activo = FALSE; Inactivo = TRUE;
	string Estadostr;
	int ciclos_totales;
	string Operacion;
};

#endif /* ARTICULACION_H */