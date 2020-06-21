#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

# Complete the commonChild function below.
def commonChild(s1, s2):

    len1 = len(s1)
    len2 = len(s2)
    c = [[0 for x in range(len1)] for y in range(len2)]

    for i in range(len1):
        for j in range(len2):
            #print(s1[i], s2[j])
            if s1[i] == s2[j]:
                i_m = i - 1 if i > 0 else 0
                j_m = j - 1 if j > 0 else 0
                c[i][j] = c[i_m][j_m] + 1
            else:
                c[i][j] = max(c[i][j-1], c[i-1][j])
            #print(np.matrix(c))
            #print("="*10)
    #print(np.matrix(c))
    return c[len1-1][len2-1]



def test_commonChild():
    ins = ['HARRY SALLY',
           'AA BB',
           'SHINCHAN NOHARAAA',
           'ABCDEF FBDAMN']
    exp = list(map(int, '2 0 3 2'.rstrip().split()))
    for i in range(len(ins)):
        inp = ins[i].rstrip().split()
        out = commonChild(inp[0], inp[1])
        print('-'*5, exp[i], out)
        assert exp[i] == out


if __name__ == '__main__':
    test_commonChild()
