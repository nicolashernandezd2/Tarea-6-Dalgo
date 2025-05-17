"""
ESTE ES EL EJERCICIO 2.2 DE LA TAREA
"""

def translate2(G, k):
    """
    Realiza la reducción de CLIQUE a VERTEX-COVER.

    Observe que esta reducción es solo hallar el complemento del grafo y calcular el tamaño del vertex cover.

    Entradas:
    - G: tupla (V, E), donde
        - V es un conjunto/lista de nodos,
        - E es un conjunto/lista de pares (u, v), con u ≠ v
    - k: tamaño del clique buscado en G

    Salida:
    - (G_complemento, k_vc): tupla con el grafo complemento y el tamaño del vertex cover
    """

    V, E = G
    V = list(V)  # Asegurarse de poder indexar
    E_set = set(E)
    
    # Construir el complemento de G
    E_complemento = set()
    for i in range(len(V)):
        for j in range(i + 1, len(V)):
            u, v = V[i], V[j]
            if (u, v) not in E_set and (v, u) not in E_set:
                E_complemento.add((u, v))
    
    # Tamaño del vertex cover correspondiente
    k_vc = len(V) - k
    
    return (V, E_complemento), k_vc