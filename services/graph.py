import networkx as nx

def grafo():
    grafo = nx.Graph()

    nodos = ["TACN", "AQP", "MADI", "AYAC","UCAY","LIM","SANM","TUM","LOR"]
    grafo.add_nodes_from(nodos)

    aristas = [
        ("TACN", "AQP", 6),
        ("TACN", "MADI", 18),
        ("AQP", "MADI", 17),
        ("AQP", "AYAC", 7),
        ("AYAC", "UCAY", 10),
        ("AYAC", "LIM", 8),
        ("LIM", "MADI", 24),
        ("LIM", "SANM", 24),
        ("LIM", "TUM", 18),
        ("SANM", "TUM", 10),
        ("SANM", "LOR", 15),
        ("SANM", "UCAY", 10),
    ]
    grafo.add_weighted_edges_from(aristas)

    return grafo