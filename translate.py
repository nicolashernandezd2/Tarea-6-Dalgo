class Grafo:
    def __init__(self):
        self.nodos = set()
        self.aristas = []

    def agregar_nodo(self, nodo):
        self.nodos.add(nodo)

    def agregar_arista(self, nodo1, nodo2):
        self.aristas.append((nodo1, nodo2))

"""
    Explicación del input:
    - El input es una lista de literales, donde cada literal es una cadena de texto.
    - Los literales pueden ser variables (ej: p1, p2) o sus negaciones (ej: ¬p1, ¬p2).
    - La lista con los literales está ORDENADA, es decir, entre los literales 1 y 2 la operacion es OR,
      entre los literales 2 y 3 la operacion es OR, entre los literales 3 y 4 la operacion es AND, 
      entre los literales 4 y 5 la operacion es OR, entre los literales 5 y 6 la operacion es OR, 
      entre los literales 6 y 7 la operacion es AND y así sucesivamente (porque es una 3-CNF).

    Explicación del algoritmo:
    - Se crea un grafo vacío.
    - Se añaden nodos al grafo, cada nodo representa un literal. Si un literal aparece varias veces, se generan varios vértices distintos.
    - Se añaden aristas entre los nodos según las reglas:
        1. No conectar nodos que pertenecen a la misma cláusula (ej: p1 y p2).
        2. No conectar literales complementarios (ej: p1 y ¬p1).
"""
def translate(literals):
    # Crear grafo
    G = Grafo()
    n = len(literals)
    
    # Añadir nodos (cada literal es un nodo único, identificado por su índice)
    for i in range(n):
        G.agregar_nodo(literals[i])
    
    # Conectar nodos según reglas
    for i in range(n):
        for j in range(i + 1, n):
            # Obtener cláusulas de i y j
            clausula_i = i // 3
            clausula_j = j // 3
            
            # Regla 1: No conectar nodos de la misma cláusula
            if clausula_i == clausula_j:
                continue
            
            # Regla 2: No conectar literales complementarios
            lit_i = literals[i]
            lit_j = literals[j]
            
            # Verificar si son complementarios (ej: p1 y ¬p1)
            if (lit_i == f"¬{lit_j}") or (lit_j == f"¬{lit_i}"):
                continue
            
            # Si pasa ambas reglas, crear arista
            G.agregar_arista(literals[i], literals[j])
    
    return G