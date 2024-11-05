import networkx as nx

fh = open("congress.edgelist", "rb")
G = nx.read_edgelist(fh)
fh.close()
nx.set_edge_attributes(G, {(u, v): {'capacity' : 1} for u, v, ed in G.edges.data()})

print('Degree: ', G.number_of_nodes())
print('Edges: ', G.number_of_edges())
print('Density: ', nx.density(G))
print('Radius: ', nx.radius(G))
print('Average shortest path length: ', nx.average_shortest_path_length(G))