# search-algorithms
Research about different search algorithms: B&B, B&B with heuristics, DFS and BFS.

# Informe
Se compara entre dos algoritmos diferentes ramificación y salto, y ramificación y salto con subestimación. 

Se ha añadido al fichero utils.py las siguientes clases:

babg Basada en la estructura de la clase FIFOQueue modificando el método extend añadidiendo la ordenación de la lista por el path_cost.

babgsub Basada en la estructura de la clase FIFOQueue modificando el método extend añadidiendo la ordenación de la lista por  la suma del path_cost junto con de la heurística dada en la clase problem.

Se ha añadido al fichero search.py a la clase graph_search:
branch_and_bound y branch_and_bound_sud que devuelven la búsqueda del árbol correspondiente.

