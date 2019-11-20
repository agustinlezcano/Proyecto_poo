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
	bool getEstado();
	void setEstado(bool Nuevo_Estado);
	string getEstadostr();
        
        bool esOrdenValida(string,string);
        void guardarAngulo(string);

private:
	float velocidad = 0;
	bool Estado; // Activo = FALSE; Inactivo = TRUE;
	string Estadostr;
        
        int anguloGiro[3];
};

#endif /* ARTICULACION_H */