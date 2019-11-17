#include "leer.h"

void Leer::read(string archivo){
    string line;
    ifstream myfile (archivo);
    if (myfile.is_open())
    {
        while ( getline (myfile,line) )
        {
            //Por ahora orden es un string y no una lista.
            orden = line;
        }
        myfile.close();
    }

    else 
    {
        cout << "\nNo se pudo abrir el archivo..." << endl;
        cout << "Vuelva a intentarlo..." << endl;
        orden = "ERROR";
    }    
    
}

string Leer::get_orden(){
    return this->orden;
}