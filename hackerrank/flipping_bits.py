#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    inv = ~n & 0xFFFFFFFF
    return int(inv)

if __name__ == '__main__':
    q = int(input())
    results = []
    reads = []
    for q_itr in range(q):
        n = int(input().rstrip())
        reads.append(n)
        results.append(flippingBits(n))

    for p_itr in range(q):
        expected = int(input().rstrip())
        if results[p_itr] != expected:
            print(f'RESULT ({reads[p_itr]}):', results[p_itr])
            print('WRONG!', expected)
        else:
            pass
