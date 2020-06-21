#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    counter = {}
    for a in ar:
        if a not in counter.keys():
            counter[a] = 0
        counter[a] += 1
    all = 0
    for c in counter:
        all += math.floor(counter[c]/2)
    return all

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int('9')

    ar = list(map(int, '10 20 20 10 10 30 50 10 20'.rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
