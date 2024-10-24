import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

fh = open("congress.edgelist", "rb")
G = nx.read_edgelist(fh)
fh.close()
nx.set_edge_attributes(G, {(u, v): {'capacity' : 1} for u, v, ed in G.edges.data()})

source = input("Source node: ")
target = input("Target node: ")
print('shortest path: ', nx.shortest_path(G, source=source, target=target))

G_eu = nx.complete_graph(G)
print('Is Eulerian: ', nx.is_eulerian(G_eu))
print('Eulerian path: ', next(nx.eulerian_path(G_eu)))
print('Max flow: ', nx.maximum_flow(G, _s=source, _t=target))