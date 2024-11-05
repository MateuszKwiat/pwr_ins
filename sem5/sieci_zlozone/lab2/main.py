import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network

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
plt.figure(figsize=(20, 20), dpi=80)
plt.axis('off')
fig = plt.figure(1)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=40)
nx.draw_networkx_edges(G, pos, width=0.25)

plt.show()

# zad4
net = Network()
net.from_nx(G)
net.toggle_physics(False)
# net.toggle_physics(True)
net.save_graph('net.html')