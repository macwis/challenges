#!/bin/python3

import math
import os
import random
import re
import sys
import json

from collections import defaultdict

class Grid:

    def __init__(self, n, m, grid):
        self.n = n  # number of rows
        self.m = m  # number of columns
        #print(n, m)
        self.grid = grid
        self.visited = [[False for i in range(0,m+2)] for j in range(0, n+2)]
        self.compounds = defaultdict(list)
        self.compounds_count = defaultdict(int)

    def neighbours(self, i, j):
        adjacent = [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1)
        ]
        adjs = []
        for di, dj in adjacent:
            ix = i + di
            jx = j + dj
            if ix >= 0 and ix <= self.n+1 and jx >= 0 and jx <= self.m+1:
                adjs.append(tuple((ix, jx)))
        #print('-'*10, f'row:{i}', adjs)
        return adjs

    def dfs(self, i = 0, j = 0, label = 0):
        #print(f'({i}, {j}, {self.grid[i][j]})', end=' ')
        self.visited[i][j] = True
        if self.grid[i][j] != 1:
            return

        self.compounds[label].append([i, j])
        self.compounds_count[label] += 1

        for ix, jx in self.neighbours(i, j):
            if self.visited[ix][jx] == False:
                self.dfs(ix, jx, label)

    def getMaxCompoundCount(self):
        return max(self.compounds_count.values())


# Complete the maxRegion function below.
def maxRegion(n, m, grid):
    g = Grid(n, m, grid)
    l = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if g.visited[i][j] == False:
                g.dfs(i, j, l)
                l += 1
    #print(l)
    #print(print(json.dumps(g.visited, indent=4)))
    #print(print(json.dumps(g.compounds, indent=4)))
    #print(json.dumps(g.compounds))
    #print(json.dumps(g.compounds_count))
    return g.getMaxCompoundCount()


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    grid = []

    grid.append([0 for x in range(m+2)])
    for _ in range(n):
        grid.append(list(map(int, ('0 ' + input() + ' 0').rstrip().split())))
    grid.append([0 for x in range(m+2)])

    res = maxRegion(n, m, grid)

    print(res)
