#!/bin/python3

import math
import os
import random
import re
import sys
from timeit import Timer


def minimumBribes(q):
    c = 0
    for cur_pos, org_pos in enumerate(q):
        org_pos -= 1
        if org_pos - cur_pos > 2:
            return 'Too chaotic'
        for j in range(max(org_pos - 1, 0), cur_pos):
            if q[j] > org_pos:
                c += 1
    return c


'''
# TOO SLOW
def transition(arr, place_of_last, d):
    i = place_of_last
    # print(i)
    if d == 1:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        return 1
    elif d == 2:
        arr[i], arr[i + 1], arr[i + 2] = arr[i + 1], arr[i + 2], arr[i]
        return 2


# Complete the minimumBribes function below.
def minimumBribes(q):
    transitions = 0
    arr = q
    target = list(range(1, len(q)+1))
    numbers_list = list(range(1, len(q)+1))
    while(arr != target):
        if numbers_list == []:
            return 'Too chaotic'
        last = numbers_list.pop()  # largest number to put in place (1-n)
        place_of_last = arr.index(last)  # current place of this number (1-n)
        diff = last - 1 - place_of_last  # shift required
        if diff > 0 and diff <= 2:  # check if acceptable shift
            # if OK, swap elements
            # print(arr)
            # print(last, place_of_last, diff)
            transitions += transition(arr, place_of_last, diff)  # account number of bribes
            # print(arr)
            # print("--"*10)
        elif diff > 2:
            return 'Too chaotic'
    return transitions
'''

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        m = minimumBribes(q)
        print(m)
        # 2 1 5 3 4
        # 3

        # 2 5 1 3 4
        # Too chaotic
