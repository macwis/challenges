#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    dict = defaultdict(int)
    for m in magazine:
        dict[m] += 1
    for n in note:
        if n not in dict.keys():
            return 'No'
        if dict[n] == 0:
            return 'No'
        dict[n] -= 1
    return 'Yes'

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    exp = input().rstrip()

    res = checkMagazine(magazine, note)

    print(f'expected: {exp}\nactual: {res}')
