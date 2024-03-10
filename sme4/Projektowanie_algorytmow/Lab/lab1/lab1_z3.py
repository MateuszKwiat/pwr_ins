import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.Graph()
pos = {}

nodes_amount = int(input("Nodes amount: "))
theta = 0
theta_move_value = (2 * np.pi) / nodes_amount

for node_label in range(1, nodes_amount + 1):
    G.add_node(node_label)
    pos[node_label] = (np.cos(theta), np.sin(theta))

    theta += theta_move_value

for i in range(1, nodes_amount):
    for j in range(i + 1, nodes_amount + 1):
        G.add_edge(i, j)

plt.figure(figsize=(6, 6))

nx.draw_networkx_nodes(G, pos, node_size=200, node_color='orange')
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)

plt.show()