import networkx as nx
from networkx.linalg.graphmatrix import incidence_matrix

fh = open("congress.edgelist", "rb")
G = nx.read_edgelist(fh)
fh.close()
nx.set_edge_attributes(G, {(u, v): {'capacity' : 1} for u, v, ed in G.edges.data()})

# zad1
A = nx.incidence_matrix(G)
B = nx.adjacency_matrix(G)
print(A)
print('-'*40)
print(B)

# zad2
G1 = nx.from_numpy_array(B)

# zad3