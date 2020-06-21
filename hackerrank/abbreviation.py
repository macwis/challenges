#!/bin/python3

import math
import os
import random
import re
import sys

import numpy as np

# Complete the abbreviation function below.
def abbreviation(a, b):
    len_a = len(a)
    len_b = len(b)
    c = [[0 for x in range(len_b+1)] for y in range(len_a+1)]

    for j in range(0,len_b):
        if j == 0:
            c[0][j] = 1
        else:
            c[0][j] = 0

    count = 0
    for k in range(1, len_a):
        i = k - 1
        if ord(a[i]) >= 65 and ord(a[i]) <= 90 or count == 1:
            count = 1
            c[k][0] = 0
        else:
            c[k][0] = 1

    for k in range(1, len_a + 1):
        i = k - 1
        for l in range(1, len_b + 1):
            j = l - 1
            print(np.matrix(c))
            #print(a[i], b[j])
            if a[i] == b[j]:
                c[k][l] = c[k-1][l-1]
                continue
            else:
                if a[i].upper() == b[j]:
                    c[k][l] = (c[k-1][l-1] | c[k-1][l])
                    continue
            if ord(a[i]) >= 65 and ord(a[i]) <= 90:
                c[k][l] = 0;
                continue;
            else:
                c[k][l] = c[k-1][l]
                continue;

    if c[-1][-1]:
        return 'YES'
    return 'NO'


def test_abbrevation():
    ins = ['daBcd ABC',
           'ddbb AABB',
           'AbCdFeGh ACFGH',
           'NNNooo No',
           'beFgH EFG']
    exp = 'YES NO YES NO NO'.rstrip().split()
    for i in range(len(ins)):
        inp = ins[i].rstrip().split()
        out = abbreviation(inp[0], inp[1])
        print('-'*5, inp[0], inp[1], exp[i], out)
        #assert exp[i] == out

if __name__ == '__main__':
    test_abbrevation()
