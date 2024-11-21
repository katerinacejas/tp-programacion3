import time
import networkx as nx
import matplotlib.pyplot as plt

def mostrar_grafo(camino):
    G = nx.Graph()
    for pair in camino:
        if camino.index(pair) + 1 < len(camino):
            G.add_edge(pair,camino[camino.index(pair) + 1])

    nx.draw_networkx(G,arrows=True,with_labels=True)
    plt.show()