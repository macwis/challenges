#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    a = [0]*(n+1)

    for s,e,v in queries:
        a[s-1] += v
        a[e] -= v

    max = 0
    sum = 0
    for v in a:
        sum += v
        if sum > max:
            max = sum
    return max


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    expected = int(input())

    result = arrayManipulation(n, queries)
    print('RESULT:', result)
    if result != expected:
        print('WRONG! ', expected)
    else:
        print('OK')

    #fptr.write(str(result) + '\n')

    #fptr.close()
