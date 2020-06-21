#!/bin/python3

import math
import os
import random
import re
import sys
import pytest


def palidrome(s):
    if s == s[::-1]:
        return True
    else:
        return False


# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    #print("="*10, s)
    if palidrome(s):
        return 0
    leng = len(s)
    i = 0
    sum = 0
    while(i < leng/2):
        c = ord(s[leng-1-i]) - ord(s[i])
        #print(s[i], s[leng-1-i], c)
        i += 1
        sum += abs(c)
    #print(sum)
    return sum


def test_theLoveLetterMystery():
    cases = ['abcba','abc','abcd', 'cba']
    expected = [0, 2, 4, 2]
    q = len(cases)
    for q_itr in range(q):
        s = cases[q_itr]
        result = theLoveLetterMystery(s)
        assert result == expected[q_itr]


if __name__ == '__main__':
    test_theLoveLetterMystery()
    quit()
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #q = int(input())
    cases = ['abc','abcba','abcd', 'cba']
    expected = [2, 0, 4, 2]
    q = len(cases)

    for q_itr in range(q):
        s = cases[q_itr]

        result = theLoveLetterMystery(s)

        #fptr.write(str(result) + '\n')

    #fptr.close()
