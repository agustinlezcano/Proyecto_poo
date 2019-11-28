from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import IDL
from Comands import Comands
import trayectoria as Trayectoria
# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Crear el servidor
with SimpleXMLRPCServer(('localhost', 8080),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
#Registrar
    server.register_instance(IDL)
    server.register_instance(Comands)
    # Run the server's main loop
    #server.serve_forever()
    if __name__ == "__main__":
        try:
            print("Sending...")
            orden='EA+40B-30C180P'
            prueba=Trayectoria()
            prueba.esOrdenValida(orden)
            print=("angulo 1 ", Trayectoria.anguloGiro[0])
            print=("angulo 2 ", Trayectoria.anguloGiro[1])
            print=("angulo 3 ", Trayectoria.anguloGiro[2])
            server.serve_forever()
        except KeyboardInterrupt:
            print("Exiting")
