import networkx as nx

def grafo():
    grafo = nx.DiGraph()

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

# def enlazar_grafo_bd():
#     grafo = grafo()  

#     # Enlazar los nodos del grafo a los nodos en la base de datos
#     for nodo_nombre in grafo.nodes():
#         try:
#             # Buscar si el nodo ya existe en la base de datos
#             nodo_bd, created = Nodo.objects.get_or_create(alias=nodo_nombre,)
#             if created:
#                 print(f"Se creó el nodo: {nodo_bd.nombre}")
#             else:
#                 print(f"El nodo ya existe: {nodo_bd.nombre}")
#         except Nodo.DoesNotExist:
#             print(f"Error al enlazar el nodo {nodo_nombre}")

    # # Enlazar las aristas del grafo a las rutas en la base de datos
    # for nodo_origen, nodo_destino, datos in grafo.edges(data=True):
    #     peso = datos['weight']

    #     try:
    #         # Obtener los nodos origen y destino desde la base de datos
    #         nodo_origen_bd = Nodo.objects.get(alias=nodo_origen)
    #         nodo_destino_bd = Nodo.objects.get(alias=nodo_destino)

    #         # Crear o actualizar la ruta en la base de datos
    #         ruta_bd, created = Ruta.objects.get_or_create(
    #             nodo_inicio=nodo_origen_bd,
    #             nodo_fin=nodo_destino_bd,
    #             # defaults={'peso': peso}
    #             tiempo= peso
    #         )
    #         if created:
    #             print(f"Se creó la ruta de {nodo_origen} a {nodo_destino} con peso {peso}")
    #         else:
    #             print(f"La ruta de {nodo_origen} a {nodo_destino} ya existe")
    #     except Nodo.DoesNotExist:
    #         print(f"Error: Nodo origen o destino no existe en la base de datos")

# Ejecutar la función para enlazar el grafo manual con los nodos y rutas en la base de datos
# enlazar_grafo_bd()
