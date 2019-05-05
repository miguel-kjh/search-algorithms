# Search methods

import search
import time
def printResult(Busqueda,node,end):
    print("\n" + Busqueda)
    print(node[0].path())
    print("Coste-->" + str(node[0].path_cost))
    print("Nodos Expandidos-->" + str(node[1]))
    print("Nodos generados-->" + str(node[2]))
    print("Tiempo de Busqueda-->" + str(end))

if __name__ == '__main__':
    origenes = ['A','R','N','G','T']
    destinos = ['B', 'E', 'O', 'L', 'H']
    for origen,destino in zip(origenes,destinos):
        print("\n#################### " + origen + "--" + destino + " #####################")
        ruta = search.GPSProblem(origen, destino, search.romania)
        st = time.time()
        node = search.branch_and_bound(ruta)
        end = time.time() - st
        printResult("Busqueda en Ramificación y Poda", node, end)

        st = time.time()
        node = search.branch_and_bound_Sub(ruta)
        end = time.time() - st
        printResult("Busqueda en Ramificación y Poda con subestimación", node, end)

