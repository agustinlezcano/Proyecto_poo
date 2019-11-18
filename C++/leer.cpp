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

void Leer::crear_rutina(){
    ofstream fout;
    ifstream fin;
    
    string archivo, orden;
    cout << "Ingrese nombre del archivo a crear: " <<endl;
    cin >> archivo;
    
    int op=1;
    cout << endl << "Escriba GUARDAR una vez terminado de cargar de ordenes" << endl;
    cout << "Ingrese orden nueva: " << endl;
    
    while (op==1){
        fin.open(archivo);
        fout.open(archivo,ios::app);
        cin >> orden;
    
        if ((orden != "GUARDAR")and(fin.is_open())){
            fout << "\n";
            fout << orden;
        }
    
        if ((orden == "GUARDAR")or(orden == "guardar")){
            op=0;
            cout << "Rutina guardada exitosamente" <<endl;
        
        }
        fin.close();
        fout.close();
    }
}