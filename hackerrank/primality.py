#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the primality function below.
def primality(n):
    # OPTIMIZED VERSION
    if n < 2:
        return 'Not prime'
    if n <= 3:
        return 'Prime'
    if n % 2 == 0 or n % 3 == 0:
        return 'Not prime'
    for i in range(1, math.ceil(math.sqrt(n)) + 1, 2):
        if i == 1:
            continue
        if n % i == 0:
            return 'Not prime'
    return 'Prime'

    '''
    # Full AKS
    c = 1
    for i in range(n//2 + 1):
        c = c * (n - i)//(i + 1)
        if c % n:
            return 'Not prime'
    return 'Prime'
    '''


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input())

    results = []
    reads = []
    for p_itr in range(p):
        n = int(input())
        reads.append(n)
        results.append(primality(n))

    for p_itr in range(p):
        expected = input().rstrip()

        if results[p_itr] != expected:
            print(f'RESULT ({reads[p_itr]}):', results[p_itr])
            print('WRONG!', expected)
        else:
            pass
            #print('OK')

        #fptr.write(result + '\n')

    #fptr.close()
