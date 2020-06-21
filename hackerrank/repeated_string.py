#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    #naive version
    '''
    gen = ''
    while(len(gen) < n):
        gen += s
        print(gen)
    return gen[0:n].count('a')
    '''
    #smarter version
    k = math.ceil(n / len(s))  # so many times we have to "generate" s
                               # to get n-th element
    total_len = (len(s) * k)
    tail = n % len(s)
    if tail == 0:
        a_count = s.count('a')*k
    else:
        a_count = s.count('a')*(k-1) + s[0:tail].count('a')
    print(total_len, tail, a_count)
    return a_count


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = 'abasdfsdfw'

    n = int('70')

    result = repeatedString(s, n)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
