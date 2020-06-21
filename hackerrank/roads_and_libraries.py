#!/bin/python3

import math
import os
import random
import re
import sys
import logging
import json

from collections import defaultdict

class Graph:
    g = defaultdict(list)

    def reset(self, n):
        self.visited = {int(key):False for key in range(1,n+1)}
        self.c = 0

    def addVertices(self, n):
        self.g = {int(key):[] for key in range(1,n+1)}

    def addEdge(self, u, v):
        self.g[u].append(v)
        self.g[v].append(u)

    def dfs(self, v = 1):
        self.visited[v] = True
        for i in self.g[v]:
            if self.visited[i] == False:
                self.c += 1
                self.dfs(i)
        return self.c

    def __str__(self):
        return self.g


# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    m = len(cities)
    if m == 0 or c_lib < c_road:
        return n*c_lib
    g = Graph()
    g.addVertices(n)
    add = [g.addEdge(x, y) for x, y in cities]
    #print(json.dumps(g.g, indent=4))
    g.reset(n)
    roads = 0
    libs = 0
    for i in range(1,n+1):
        if g.visited[i] == False:
            roads = g.dfs(i)
            libs += 1
            #print('-'*10, roads, libs)
            #print(g.visited)
    cost = (roads * c_road) + (libs * c_lib)
    #print(cost)
    #print("="*20)
    return cost

if __name__ == '__main__':
    q = int(input())
    results = []
    for q_itr in range(q):
        nmC_libC_road = input().split()
        n = int(nmC_libC_road[0])
        m = int(nmC_libC_road[1])
        c_lib = int(nmC_libC_road[2])
        c_road = int(nmC_libC_road[3])
        cities = []
        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        results.append(roadsAndLibraries(n, c_lib, c_road, cities))

    for q_itr in range(q):
        expected = int(input())
        print('RESULT:', results[q_itr])
        if results[q_itr] != expected:
            print('WRONG! ', expected)
        else:
            print('OK')
