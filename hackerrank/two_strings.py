#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    shadow = defaultdict(int)
    for c1 in s1:
        shadow[c1] += 1
    for c2 in s2:
        if shadow[c2]:
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input().rstrip()

        s2 = input().rstrip()

        result = twoStrings(s1, s2)
        print(result)

        #fptr.write(result + '\n')

    #fptr.close()
