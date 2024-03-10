import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.Graph()
pos = {}
circles = []
counter = 0
counter_add = 0

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
    if counter > 9:
        break

    x = np.random.uniform(x_l, x_h)
    y = np.random.uniform(y_l, y_h) 

    G.add_node(node_label)
    pos[node_label] = (x, y)
    
    circles.append(plt.Circle((x, y), r, color='black', fill=False))

    nx.draw_networkx_nodes(G, pos, node_size=200, node_color='orange')
    nx.draw_networkx_labels(G, pos)
    

    for circle in circles:
        plt.gca().add_patch(circle)

    plt.draw()

    for i in range(1, node_label):
        if node_label in pos and i in pos:
            dist = np.sqrt((pos[i][0] - pos[node_label][0])**2 + (pos[i][1] - pos[node_label][1])**2)
            
            if dist < r * 2:
                G.remove_node(node_label)
                pos.pop(node_label)
                circles.pop(len(circles) - 1)
                counter_add = 1
                break
        
    if counter_add == 1:
        counter += 1
    else:
        counter = 0
    
    counter_add = 0
    
    print(counter)
    plt.pause(0.5)
    plt.cla()

nx.draw_networkx_nodes(G, pos, node_size=200, node_color='orange')
nx.draw_networkx_labels(G, pos)

for circle in circles:
    plt.gca().add_patch(circle)

plt.draw()
plt.show()