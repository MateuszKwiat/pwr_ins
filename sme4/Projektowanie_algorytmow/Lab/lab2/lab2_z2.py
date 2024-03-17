import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def draw_FSM(G, pos, current_node, final_node):
    nx.draw_networkx_nodes(G, pos, nodelist=final_node, node_size=1750, node_color='black')
    nx.draw_networkx_nodes(G, pos, node_size=1500, node_color='orange')
    nx.draw_networkx_nodes(G, pos, nodelist=[current_node], node_size=1500, node_color='red')
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={
        ('q0', 'q2') : 'a, b, c',
        ('q1', 'q0') : 'b',
        ('q1', 'q3') : 'c',
        ('q1', 'q4') : 'a',
        ('q2', 'q1') : 'a, b',
        ('q2', 'q6') : 'c',
        ('q3', 'q3') : 'a, b, c',
        ('q4', 'q0') : 'a',
        ('q4', 'q5') : 'b, c',
        ('q5', 'q4') : 'a, b, c',
        ('q6', 'q3') : 'a, b, c'
        })

def FSM(alphabet):
    print(alphabet)
    sigma = ['a', 'b', 'c']
    states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6']
    transitions = {
        'q0' : {'a' : 'q2', 'b' : 'q2', 'c' : 'q2'},
        'q1' : {'a' : 'q4', 'b' : 'q0', 'c' : 'q3'},
        'q2' : {'a' : 'q1', 'b' : 'q1', 'c' : 'q6'},
        'q3' : {'a' : 'q3', 'b' : 'q3', 'c' : 'q3'},
        'q4' : {'a' : 'q0', 'b' : 'q5', 'c' : 'q5'},
        'q5' : {'a' : 'q4', 'b' : 'q4', 'c' : 'q4'},
        'q6' : {'a' : 'q3', 'b' : 'q3', 'c' : 'q3'},
    }

    initial_state = 'q0'
    final_state = ['q4', 'q5']

    current_state = initial_state

    G = nx.DiGraph()
    
    G.add_nodes_from(states)
    G.add_edge('q0', 'q2')
    G.add_edge('q1', 'q0')
    G.add_edge('q1', 'q3')
    G.add_edge('q1', 'q4')
    G.add_edge('q2', 'q1')
    G.add_edge('q2', 'q6')
    G.add_edge('q3', 'q3')
    G.add_edge('q4', 'q0')
    G.add_edge('q4', 'q5')
    G.add_edge('q5', 'q4')
    G.add_edge('q6', 'q3')

    #pos = nx.spring_layout(G)

    pos = {
        'q0' : (0, 0),
        'q1' : (50, 0),
        'q2' : (50, 50),
        'q3' : (100, 0),
        'q4' : (50, -50),
        'q5' : (100, -50),
        'q6' : (100, 50)
    }

    plt.figure(figsize=(8, 6))

    for char in alphabet:
        current_state = transitions[current_state][char]
        draw_FSM(G, pos, current_state, final_state)
        plt.draw()
        plt.pause(0.5)
        plt.cla()

    draw_FSM(G, pos, current_state, final_state)
    plt.draw()
    plt.pause(1)
    plt.close()

    return True if current_state in final_state else False

alph = "abc"

print(FSM('ababa'))
print()
# print(FSM(''.join([alph[np.random.randint(0, 3)] for i in range(10)])))
# print()
# print(FSM(''.join([alph[np.random.randint(0, 3)] for i in range(10)])))
# print()
# print(FSM(''.join([alph[np.random.randint(0, 3)] for i in range(10)])))
# print()
# print(FSM(''.join([alph[np.random.randint(0, 3)] for i in range(10)])))
# print()
print(FSM('abaabbbabaccabbacc'))