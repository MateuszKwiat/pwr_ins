import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.Graph()
pos = {}

# input
nodes_amount = int(input("Nodes amount: "))
x_l, x_h = map(int, input("Range of OX axis (two values separated with space): ").split())

while x_l >= x_h:
    x_l, x_h = map(int, input("First x value must be greater than second x value: ").split())

y_l, y_h = map(int, input("Range of OY axis (two values separated with space): ").split())

while y_l >= y_h:
    y_l, y_h = map(int, input("First y value must be greater than second y value: ").split())

# making of a graph
for node_label in range(1, nodes_amount + 1):
    G.add_node(node_label)
    pos[node_label] = (np.random.uniform(x_l, x_h), np.random.uniform(y_l, y_h))

plt.figure(figsize=(6, 6))

nx.draw_networkx_nodes(G, pos, node_size=200, node_color='orange')
nx.draw_networkx_labels(G, pos)

plt.show()