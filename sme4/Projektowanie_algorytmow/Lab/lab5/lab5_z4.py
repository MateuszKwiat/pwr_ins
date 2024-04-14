from collections import defaultdict 
import ast

def path_finding(edges_dict, start, end):
    if start == end:
        return [start]

    for nxt in edges_dict[start]:
        path = path_finding(edges_dict, nxt, end)
        if path is not None: 
            return [start] + path
            
def shortest_path(edges, start, end):
    edges_dict = defaultdict(list)
    for i,j in edges:
        edges_dict[i] += [j]

    return path_finding(edges_dict, start, end)

edges = None

with open('edges.txt') as file:
    line = file.readline()
    edges = ast.literal_eval(line)

path = shortest_path(edges, 0, 7)
print (path)