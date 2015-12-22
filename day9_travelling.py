#!/usr/bin/env python3
import re
import networkx as nx

puzzle_input = """AlphaCentauri to Snowdin = 66
AlphaCentauri to Tambi = 28
AlphaCentauri to Faerun = 60
AlphaCentauri to Norrath = 34
AlphaCentauri to Straylight = 34
AlphaCentauri to Tristram = 3
AlphaCentauri to Arbre = 108
Snowdin to Tambi = 22
Snowdin to Faerun = 12
Snowdin to Norrath = 91
Snowdin to Straylight = 121
Snowdin to Tristram = 111
Snowdin to Arbre = 71
Tambi to Faerun = 39
Tambi to Norrath = 113
Tambi to Straylight = 130
Tambi to Tristram = 35
Tambi to Arbre = 40
Faerun to Norrath = 63
Faerun to Straylight = 21
Faerun to Tristram = 57
Faerun to Arbre = 83
Norrath to Straylight = 9
Norrath to Tristram = 50
Norrath to Arbre = 60
Straylight to Tristram = 27
Straylight to Arbre = 81
Tristram to Arbre = 90"""

G = nx.Graph()
for line in puzzle_input.split('\n'):
    node1, node2, weight = re.compile(r'(\w+) to (\w+) = (\d+)').findall(line)[0]
    if node1 not in G:
        G.add_node(node1)
    if node2 not in G:
        G.add_node(node2)
    G.add_edge(node1, node2, weight=int(weight))

distances=[]
for source_node in G:
    for dest_node in G:
        for path in nx.shortest_simple_paths(G, source_node, dest_node):
            if len(path) == len(G):
                distance = 0
                for i in range(len(G)-1):
                    distance += G[path[i]][path[i+1]]['weight']
                distances.append(distance)

"Shortest: {}, longest: {}.".format(min(distances), max(distances))
