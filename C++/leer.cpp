#include "leer.h"

string Leer::read(string archivo){
    string line;
    string orden;
    ifstream myfile (archivo);
    if (myfile.is_open())
    {
        while ( getline (myfile,line) )
        {
            //Por ahora orden es un string y no una lista.
            orden = line;
            //get_orden(orden);
        }
        myfile.close();
    }

    else 
    {
        cout << "\nNo se pudo abrir el archivo..." << endl;
        cout << "Vuelva a intentarlo..." << endl;
        orden = "ERROR";
    }
    return orden;
}
