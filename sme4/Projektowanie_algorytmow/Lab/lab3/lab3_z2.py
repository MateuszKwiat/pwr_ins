import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def draw_TM(G, pos, current_state):
    node_size = 1500
    nx.draw_networkx_nodes(G, pos, nodelist=['q0', 'qa', 'qr1', 'qr2', 'qr3', 'qr4'], node_size=node_size + 200, node_color='black')
    nx.draw_networkx_nodes(G, pos, node_size=node_size, node_color='gray')
    nx.draw_networkx_nodes(G, pos, nodelist=['q0'], node_size=node_size, node_color='yellow')
    nx.draw_networkx_nodes(G, pos, nodelist=['qr1', 'qr2', 'qr3', 'qr4'], node_size=node_size, node_color='red')
    nx.draw_networkx_nodes(G, pos, nodelist=['qa'], node_size=node_size, node_color='green')
    nx.draw_networkx_nodes(G, pos, nodelist=[current_state], node_size=node_size, node_color='orange')
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={
        ('q0', 'q1') : '0, 1 -> L',
        ('q0', 'q2') : '0 -> 0/, R',
        ('q0', 'q3') : '1 -> 1/, R',
        ('q1', 'q1') : '',
        ('q1', 'qa') : '_ -> L',
        ('q1', 'qr1') : '0, 1 -> L',
        ('q2', 'qr1') : '_ -> R',
        ('q2', 'q2') : '',
        ('q2', 'q4') : 'b -> R',
        ('q3', 'q5') : 'b -> R',
        ('q3', 'q3') : '',
        ('q3', 'qr3') : '_ -> R',
        ('q4', 'q4') : '',
        ('q4', 'qr2') : '_, 1 -> R',
        ('q4', 'q6') : '0 -> 0/, L',
        ('q5', 'q6') : '1 -> 1/, L',
        ('q5', 'qr4') : '_, 0 -> R',
        ('q5', 'q5') : '',
        ('q6', 'q6') : '',
        ('q6', 'q7') : 'b -> L',
        ('q7', 'q7') : '',
        ('q7', 'q0') : '0/, 1/ -> R'
        })

def TM(alphabet):
    simga = ['0', '1', 'b', '_', '0/', '1/']
    states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'qa', 'qr1', 'qr2', 'qr3', 'qr4']
    transitions = {
        'q0' : {'b' : ['q1', 'b', 1], '0' : ['q2', '0/', 1], '1' : ['q3', '1/', 1]},
        'q1' : {'0/' : ['q1', '0/', 1], '1/' : ['q1', '1/', 1], '_' : ['qa', '_', -1], '0' : ['qr1', '0', -1], '1' : ['qr1', '1', -1]},
        'q2' : {'_' : ['qr1', '_', 1], '0' : ['q2', '0', 1], '1' : ['q2', '1', 1], 'b' : ['q4', 'b', 1]},
        'q3' : {'b' : ['q5', 'b', 1], '0' : ['q3', '0', 1], '1' : ['q3', '1', 1], '_' : ['qr3', '_', 1]},
        'q4' : {'0/' : ['q4', '0/', 1], '1/' : ['q4', '1/', 1], '_' : ['qr2', '_', 1], '1' : ['qr2', '1', 1], '0' : ['q6', '0/', -1]},
        'q5' : {'1' : ['q6', '1/', -1], '_' : ['qr4', '_', 1], '0' : ['qr4', '0', 1], '0/' : ['q5', '0/', 1], '1/' : ['q5', '1/', 1]},
        'q6' : {'0/' : ['q6', '0/', -1], '1/' : ['q6', '1/', -1], 'b' : ['q7', 'b', -1]},
        'q7' : {'0' : ['q7', '0', -1], '1' : ['q7', '1', -1], '0/' : ['q0', '0/', 1], '1/' : ['q0', '1/', 1]}
    }

    initial_state = 'q0'
    current_state = initial_state
    head = 0

    G = nx.DiGraph()
    
    G.add_nodes_from(states)
    G.add_edge('q0', 'q1')
    G.add_edge('q0', 'q2')
    G.add_edge('q0', 'q3')
    G.add_edge('q1', 'q1')
    G.add_edge('q1', 'qa')
    G.add_edge('q1', 'qr1')
    G.add_edge('q2', 'qr1')
    G.add_edge('q2', 'q2')
    G.add_edge('q2', 'q4')
    G.add_edge('q3', 'q5')
    G.add_edge('q3', 'q3')
    G.add_edge('q3', 'qr3')
    G.add_edge('q4', 'q4')
    G.add_edge('q4', 'qr2')
    G.add_edge('q4', 'q6')
    G.add_edge('q5', 'q6')
    G.add_edge('q5', 'qr4')
    G.add_edge('q5', 'q5')
    G.add_edge('q6', 'q6')
    G.add_edge('q6', 'q7')
    G.add_edge('q7', 'q7')
    G.add_edge('q7', 'q0')

    #pos = nx.spring_layout(G)

    pos = {
        'q0' : (0, 0),
        'q7' : (75, 0),
        'q6' : (150, 0),
        'q1' : (-50, 50),
        'qr1' : (0, 50),
        'q2' : (50, 50),
        'q4' : (100, 50),
        'qr2' : (150, 50),
        'qa' : (-50, 100),
        'qr3' : (0, -50),
        'q3' : (50, -50),
        'q5' : (100, -50),
        'qr4' : (150, -50)
    }

    plt.figure(figsize=(10, 6))


    while current_state not in ['qr1', 'qr2', 'qr3', 'qr4'] and current_state != 'qa':
        operations = transitions[current_state][alphabet[head]]
        current_state = operations[0]
        alphabet[head] = operations[1]
        head += operations[2]

        draw_TM(G, pos, current_state)
        plt.draw()
        plt.pause(0.25)
        plt.cla()

        if head < 0:
            head = 0

        if head >= len(alphabet):
            alphabet.append('_')

    draw_TM(G, pos, current_state)
    plt.draw()
    plt.pause(2)
    plt.close()

    return True if current_state == 'qa' else False


print(TM(['0', '0', '1', 'b', '0', '0', '1', '_']))
alphabet = [*input()]
print(TM(alphabet))