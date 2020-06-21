#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):

    nav2 = defaultdict(int)
    nav3 = defaultdict(int)
    c = 0
    for a in arr:
        c += nav3[a]
        nav3[a*r] += nav2[a]
        nav2[a*r] += 1
    return c

    '''
    # BRUTE FORCE
    c = 0
    sequences = []
    for k1, a in enumerate(arr):
        k2s = [i for i, x in enumerate(arr[k1:]) if x == a*r]
        for k2 in k2s:
            #print(k2, arr[k1+k2])
            k3s = [i for i, x in enumerate(arr[k2:]) if x == a*r*r]
            for k3 in k3s:
                #print(k3, arr[k2+k3])
                #print(arr[k1],
                #      arr[k1+k2],
                #      arr[k2+k3])
                sequences.append((k1, k1+k2, k2+k3))
    return len(sequences)
    '''


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    expected = int(input().rstrip())
    if expected == ans:
        print('OK')
    else:
        print(f'expected: {expected}\nactual: {ans}')

    #fptr.write(str(ans) + '\n')

    #fptr.close()
