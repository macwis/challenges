#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    prev_c = None
    count = 0
    for c in s:
        if c != prev_c:
            prev_c = c
        else:
            count += 1
    return count


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #q = int(input())
    q = 1
    for q_itr in range(q):
        s = 'ABBABABBBBABABBBABABBAAA'  #input()

        result = alternatingCharacters(s)
        print(result)
        #fptr.write(str(result) + '\n')

    #fptr.close()
