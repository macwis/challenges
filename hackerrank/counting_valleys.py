#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    height = 0
    valley_counter = 0
    for symb in s:
        if symb == 'U':
            height += 1
        elif symb == 'D':
            height -= 1
        if symb == 'D' and height == -1:
            valley_counter += 1
    return valley_counter

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int('8')

    s = 'UDDDUDUU'

    result = countingValleys(n, s)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
