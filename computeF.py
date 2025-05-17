"""
ESTE ES EL EJERCICIO 3 DE LA TAREA
"""

from itertools import combinations, permutations

"""
    3.1

    Para este caso, definimos el problema de decisión auxiliar checkZ(G, perm), que verifica si
    una permutación de los vértices de G es un ciclo hamiltoniano.
    Esta función auxiliar retorna True si la permutación es un ciclo hamiltoniano y False en caso contrario.

    En el algoritmo, se generan todas las permutaciones de los vértices de G y se verifica si alguna
    de ellas es un ciclo hamiltoniano. Claramente, en caso de que alguna de ellas sea un ciclo hamiltoniano,
    entonces el grafo G es hamiltoniano.

    Si se encuentra una permutación que cumple la condición, se devuelve esa permutación.
    Si no se encuentra ninguna permutación que cumpla la condición, se devuelve None.
"""

def computeHAM(G):
    for perm in permutations(G.vertices):
        if checkZ(G, perm):  
            return perm
    return None




"""
    3.2

    Para este caso, definimos el problema de decisión auxiliar checkZ(G, k), que verifica si
    G tiene un k-clique. Esta función auxiliar retorna True si G tiene un k-clique y False en caso contrario.
"""

def computeMaxClique(G):
    """
    Retorna el clique de tamaño máximo en G utilizando checkZ(G, k).

    Entrada:
    - el grafo G: tupla (V, E), donde
        - V es un conjunto/lista de vértices
        - E es un conjunto de tuplas (u, v) representando aristas no dirigidas

    Salida:
    - Lista de vértices que forman un clique de tamaño máximo
    """
    V, E = G
    n = len(V)
    V_list = list(V)
    
    for k in range(n, 0, -1):
        if checkZ(G, k):
            # Buscar explícitamente una k-clique
            for subset in combinations(V_list, k):
                if is_clique(subset, E):
                    return list(subset)  # Clique encontrada
    return []  # No hay clique

def is_clique(nodes, E):
    """
    Verifica si el conjunto de nodos forma una clique en E.
    """
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            u, v = nodes[i], nodes[j]
            if (u, v) not in E and (v, u) not in E:
                return False
    return True



"""
    3.3

    Para este caso, definimos el problema de decisión auxiliar checkZ(G, k), que verifica si
    G tiene un vertex cover de tamaño k. Esta función auxiliar retorna True si G tiene un 
    vertex cover de tamaño k y False en caso contrario.
"""
def computeMinVC(G):
    """
    Retorna una cobertura de vértices mínima en G utilizando checkZ(G, k).

    Entrada:
    - el grafo G: tupla (V, E), donde:
        - V es un conjunto/lista de vértices
        - E es un conjunto de pares (u, v)

    Salida:
    - Lista de nodos que forman una cobertura mínima de vértices
    """
    V, E = G
    V = list(V)
    n = len(V)

    for k in range(1, n + 1):
        if checkZ(G, k):
            # Buscar una cobertura válida de tamaño k
            for subset in combinations(V, k):
                if is_vertex_cover(subset, E):
                    return list(subset)
    return []  # Grafo sin aristas => cobertura vacía

def is_vertex_cover(cover_set, E):
    """
    Verifica si 'cover_set' cubre todas las aristas en E.
    """
    cover = set(cover_set)
    for (u, v) in E:
        if u not in cover and v not in cover:
            return False
    return True