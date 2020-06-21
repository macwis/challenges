#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the gameOfThrones function below.
def gameOfThrones(s):
    pair_check = {}
    for i in range(len(s)):
        if s[i] not in pair_check:
            pair_check[s[i]] = 0
        pair_check[s[i]] += 1
    op = 0
    for k in pair_check:
        op += pair_check[k] % 2
    if len(s) % 2 == 0 and op == 0:
        return 'YES'
    if len(s) % 2 == 1 and op == 1:
        return 'YES'
    else:
        return 'NO'


def test_gameOfThrones():
    inputs = "aaabbbb cdefghmnopqrstuvw cdcdcdcdeeeef abs".rstrip().split()
    expected = "YES NO YES NO".rstrip().split()
    for i in range(len(inputs)):
        assert expected[i] == gameOfThrones(inputs[i])


if __name__ == '__main__':
    test_gameOfThrones()
