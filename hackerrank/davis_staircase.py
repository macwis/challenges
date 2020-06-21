#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    from collections import deque
    dq = deque()
    dq.append(4)
    dq.append(2)
    dq.append(1)
    steps = 0
    for i in range(4, n+1):
        steps = sum(list(dq))
        dq.pop()
        dq.appendleft(steps)
    return steps

    '''
    # SLOWER RECURSIVE VERSION
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)
    '''


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())
    result = []

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)
        result.append(res)

    for s_itr in range(s):
        expected = int(input())
        print('RESULT:', result[s_itr])
        if result[s_itr] != expected:
            print('WRONG! ', expected)
        else:
            print('OK')

        #fptr.write(str(res) + '\n')

    #fptr.close()
