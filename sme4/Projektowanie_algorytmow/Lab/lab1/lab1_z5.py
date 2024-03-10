import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.Graph()
pos = {}
circles = []

# input
nodes_amount = int(input("Nodes amount: "))
x_l, x_h = map(float, input("Range of OX axis (two values separated with space): ").split())

while x_l >= x_h:
    x_l, x_h = map(float, input("First x value must be greater than second x value: ").split())

y_l, y_h = map(float, input("Range of OY axis (two values separated with space): ").split())

while y_l >= y_h:
    y_l, y_h = map(float, input("First y value must be greater than second y value: ").split())

r = float(input("radius: "))

# making of a graph
plt.figure(figsize=(6, 6))

for node_label in range(1, nodes_amount + 1):
    x = np.random.uniform(x_l, x_h)
    y = np.random.uniform(y_l, y_h) 

    plt.cla()
    G.add_node(node_label)
    pos[node_label] = (x, y)
    
    nx.draw_networkx_nodes(G, pos, node_size=200, node_color='orange')
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)
    
    circles.append(plt.Circle((x, y), r, color='black', fill=False))

    for circle in circles:
        plt.gca().add_patch(circle)

    plt.draw()
    plt.pause(0.5)

plt.show()