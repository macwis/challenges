#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the isBalanced function below.
def isBalanced(s):
    opens = ['[', '{', '(']
    closes = {
        ']': '[',
        '}': '{',
        ')': '('
    }
    stack = deque()
    for c in s:
        if c in opens:
            stack.append(c)
        else:
            if not stack:
                return 'NO'
            prev = stack.pop()
            if prev != closes[c]:
                return 'NO'
    if stack:
        return 'NO'
    return 'YES'



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #t = int(input())

    cases = list('{[()]} {[(])} {{[[(())]]}} {{{}}'.rstrip().split())
    expected = list('YES NO YES'.rstrip().split())
    t = len(cases)

    for t_itr in range(t):
        #s = input()
        s = cases[t_itr]

        result = isBalanced(s)
        print(result)

        #fptr.write(result + '\n')

    #fptr.close()
