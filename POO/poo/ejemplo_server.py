from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import IDL
import Comands
# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8080),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register an instance; all the methods of the instance are
    # published as XML-RPC methods 
    
    #if automatico 
        #pasar el reporte en el idl -> crear una lista de comandos -> ejecutar onecmd(list_cmd[i])
    #if manual

    server.register_instance(IDL)
    server.register_instance(Comands)
    # Run the server's main loop
    #server.serve_forever()
    if __name__ == "__main__":
        try:
            print("Sending...")
            server.serve_forever()
        except KeyboardInterrupt:
            print("Exiting")
