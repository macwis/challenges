#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findShortest function below.


bcolors = {
    0: '\033[95m',
    1: '\033[94m',
    2: '\033[92m',
    3: '\033[93m',
    4: '\033[91m',
    5: '\033[0m',
    6: '\033[1m',
    7: '\033[4m',
}

class Node:
    def __init__(self, id, color):
        self.id = id
        self.neighbours = set()
        self.color = color
        self.parent = None

    def connect(self, node):
        self.neighbours.add(node)
        node.neighbours.add(self)

    def __str__(self):
        neighbours = [v.id for v in self.neighbours]
        parent = None if not self.parent else self.parent.id
        return f'{bcolors[self.color%8]}ID:{self.id}\tCOLOR:\t{self.color}\tPARENT:{parent}\tNEIGHBOURS:{neighbours}'






#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#

from collections import deque

def findShortest(graph_nodes, graph_from, graph_to, ids, val):


    nodes = {i: Node(i, ids[i - 1]) for i in range(1, graph_nodes + 1)}
    for f, t in zip(graph_from, graph_to):
        nodes[f].connect(nodes[t])

    q = deque()
    discovered = {i: False for i in range(1, graph_nodes + 1)}
    path_len = {i: 0 for i in range(1, graph_nodes + 1)}

    for i, id in enumerate(ids):
        if id == val:
            discovered[i + 1] = True
            path_len[i + 1] = 0
            nodes[i + 1].parent = nodes[i + 1]
            q.append(nodes[i + 1])

    while q:
        v = q.popleft()
        print(v, path_len)

        for w in v.neighbours:
            if not discovered[w.id]:
                discovered[w.id] = True
                path_len[v.id] += 1
                w.parent = v
                q.append(w)
            else:
                if discovered[v.id] != v.parent:
                    return path_len[v.id] + 1
                else:
                    continue
    return -1




if __name__ == '__main__':

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    exp = int(input())

    print(f'\n\nExpected: {exp}\t Actual: {ans}')
    if exp == ans:
        print('OK!')
    else:
        print('FAILED!')
