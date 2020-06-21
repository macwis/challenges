#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    count = {}
    for i in range(len(s)):
        if s[i] not in count:
            count[s[i]] = 0
        count[s[i]] += 1
    #print(count)
    op = count[s[0]]
    diff = 0
    used_switch = 0

    inv_count = {}
    for k, v in count.items():
        inv_count[v] = inv_count.get(v, [])
        inv_count[v].append(k)

    if len(inv_count) == 1:
        return 'YES'

    if len(inv_count) == 2:
        max_key = max(inv_count.keys())
        min_key = min(inv_count.keys())
        # print(min_key, max_key, len(inv_count[max_key]))
        if (len(inv_count[max_key]) == 1 and (max_key - min_key) == 1):
            return 'YES'
        if (len(inv_count[min_key]) == 1):
            return 'YES'

    return 'NO'





def test_isValid():
    inputs = "aabb aaaaaaaaaaaaaaac aabbcd aabbccddeefghi abcdefghhgfedecba".rstrip().split()
    expected = "YES YES NO NO YES".rstrip().split()
    for i in range(len(inputs)):
        out = isValid(inputs[i])
        print(expected[i], out)
        assert expected[i] == out




if __name__ == '__main__':
    test_isValid()
