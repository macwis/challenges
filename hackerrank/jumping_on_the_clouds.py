#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(n, c):
    jumps = 0
    p = 0
    while(p < n-1):
        if p+2 < n and c[p+2] == 0:
            p += 2
        else:
            p += 1
        jumps += 1
        print(p, n, jumps)
    return jumps


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int('12')

    c = list(map(int, '0 0 1 0 1 0 1 0 0 0 1 0'.rstrip().split()))

    result = jumpingOnClouds(n, c)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
