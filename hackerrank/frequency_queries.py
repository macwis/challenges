#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    dict = Counter()  # Value as key based counter
    freq = defaultdict(int)  # Frequency as key based dict
    res = []
    for q, v in queries:
        if q == 1:
            freq[dict[v]] = max(0, freq[dict[v]] - 1)
            dict[v] += 1
            freq[dict[v]] += 1
        elif q == 2:
            freq[dict[v]] = max(0, freq[dict[v]] - 1)
            dict[v] = max(0, dict[v] - 1)
            if dict[v] > 0:
                freq[dict[v]] += 1
        elif q == 3:
            if freq[v] > 0:
                res.append(1)
            else:
                res.append(0)
        #print(q, v)
        #print(dict)
        #print(freq)
    return res

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    exp = []
    r = True
    while True:
        try:
            r = int(input().strip())
            exp.append(r)
        except EOFError as e:
            break

    if ans != exp:
        print('RESULT: ', ans)
        print('WRONG! ', exp)
    else:
        print('OK')


    #fptr.write('\n'.join(map(str, ans)))
    #fptr.write('\n')

    #fptr.close()
