import numpy as np
import networkx as nx

def part1(input_file):
    file = open(input_file, 'r')
    junction_boxes = np.array([list(map(int, line.strip().split(","))) for line in file.readlines()])

    dists = np.linalg.norm(junction_boxes[:, np.newaxis] - junction_boxes, axis=2)
    np.fill_diagonal(dists, np.inf)
    d_list = []
    for i in range(len(dists)):
        for j in range(i+1, len(dists)):
            d_list.append([dists[i, j], i, j])
    d_list.sort()

    G = nx.Graph()
    connections = 1000
    for i in range(connections):
        G.add_edge(d_list[i][1], d_list[i][2])

    lengths = [len(cluster) for cluster in sorted(nx.connected_components(G), key=len, reverse=True)]
    
    return np.prod(lengths[:3])

def part2(input_file):
    file = open(input_file, 'r')
    junction_boxes = np.array([list(map(int, line.strip().split(","))) for line in file.readlines()])

    dists = np.linalg.norm(junction_boxes[:, np.newaxis] - junction_boxes, axis=2)
    np.fill_diagonal(dists, np.inf)
    d_list = []
    for i in range(len(dists)):
        for j in range(i+1, len(dists)):
            d_list.append([dists[i, j], i, j])
    d_list.sort()

    G = nx.Graph()
    G.add_nodes_from(range(len(junction_boxes)))

    i = -1
    while nx.number_connected_components(G) > 1: 
        i += 1
        G.add_edge(d_list[i][1], d_list[i][2])

    return junction_boxes[d_list[i][1]][0] * junction_boxes[d_list[i][2]][0]

if __name__ == "__main__":
    input_file = "day8/input.txt"
    print("Part 1:", part1(input_file))
    print("Part 2:", part2(input_file))