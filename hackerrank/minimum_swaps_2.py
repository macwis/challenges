#!/bin/python3

import math
import os
import random
import re
import sys

import time

def checkEqual6502(lst):
    return not lst or [lst[0]]*len(lst) == lst

# Complete the minimumSwaps function below.
def minimumSwaps(arr):

    n = len(arr)
    c = 0
    for i in range(n):
        while arr[i] != i+1:
            print(arr)
            tmp = arr[i]
            arr[i], arr[tmp-1] = arr[tmp-1], arr[i]
            c += 1
    return c

    '''
    # PREV. VERSION SLOWER METHOD
    n = len(arr)
    des = [i for i in range(1,n+1)]
    diff = [i - j for i, j in zip(arr, des)]

    c = 0
    while(True):
        #print('+'*8, arr)
        #print('-'*8, diff)
        eq = checkEqual6502(diff)
        #print('='*8, eq)
        if eq == 1:
            break

        mem = [-math.inf, None, math.inf, None]
        for k, v in enumerate(diff):
            if v > mem[0]:
                mem[0] = v
                mem[1] = k
            if v < mem[2]:
                mem[2] = v
                mem[3] = k
        arr[mem[1]], arr[mem[3]] = arr[mem[3]], arr[mem[1]]  # swap
        diff[mem[1]] = arr[mem[1]] - des[mem[1]]
        diff[mem[3]] = arr[mem[3]] - des[mem[3]]
        c += 1
    return c
    '''


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumSwaps(arr)

    #fptr.write(str(res) + '\n')

    #fptr.close()

    expected = int(input())

    print('RESULT:', result)
    if result != expected:
        print('WRONG! ', expected)
    else:
        print('OK')
