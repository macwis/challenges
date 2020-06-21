#!/bin/python3
'''
Solution of HackerRank Challenge:
https://www.hackerrank.com/challenges/mark-and-toys
'''

import math
import os
import random
import re
import sys

def maximumToys(prices, k):
    ps = sorted(prices)
    c = 0
    for p in ps:
        if k - p >= 0:
            k -= p
            c += 1
        else:
            break
    return c

def test_maximumToys():
    n, k = tuple(map(int, '7 50'.rstrip().split()))
    prices = list(map(int, '1 12 5 111 200 1000 10'.rstrip().split()))
    expected = 4
    assert maximumToys(prices, k) == expected


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    print(result)
