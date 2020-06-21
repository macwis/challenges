#!/bin/python3

import math
import os
import random
import re
import sys


class Grid:

    def __init__(self, grid):
        self.grid = grid

    def getsum(self, i, j):
        adjacent = [
            (-1, -1),        (1, -1),
            (-1, 0),  (0, 0), (1, 0),
            (-1, 1),         (1, 1)
        ]
        sum = 0
        for di, dj in adjacent:
            ix = i + di
            jx = j + dj
            sum += self.grid[ix][jx]
        return sum


# Complete the hourglassSum function below.
def hourglassSum(arr):
    g = Grid(arr)
    sums = []
    for i in range(1, 5):
        for j in range(1, 5):
            sum = g.getsum(i, j)
            sums.append(sum)
    return max(sums)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
