#!/bin/python3

import math
import os
import random
import re
import sys
import time


# Complete the countInversions function below.
def countInversions(arr):

    c = 0
    new = []
    new_len = 0
    arr_len = len(arr)
    i = 0
    while (i < arr_len):
        #print("NOW: ", arr[i])
        done = False
        k = 0
        while (k < new_len and not done):
            if arr[i] < new[k]:
                #print(arr[i], " less than ", new[k])
                c += 1
            else:
                # put arr[i] in 'new' before k-th
                #print(f"inserting {arr[i]} into {k}-th place")
                #new.insert(k, arr[i])
                new = new[:k] + [arr[i]] + new[k:]
                new_len += 1
                done = True
            k += 1
            #time.sleep(1)
        if not done:
            #print(f"inserting {arr[i]} at the end")
            new.append(arr[i])
            new_len += 1
        i += 1
    return c

    '''
    #2 1 3 1 2
    #arr[1] -> arr[0], 1 2 3 1 2 # 1
    #arr[3] -> arr[1], 1 2 1 3 2, 1 1 2 3 2 # 2
    #arr[4] -> arr[3], 1 1 2 2 3 # 1
    #return: 1 + 2 + 1 = 4

    prev_i = None
    prev_v = None
    c = 0
    i = 0
    while (i < len(arr)):
        v = arr[i]
        if prev_i != None:
            if v < prev_v:
                #print(arr)
                #print(f"prev=({prev_v}, {prev_i}), now=({v}, {i})")
                swap(arr, i, prev_i)
                #print(arr)
                c += 1
                i = 0
                prev_v, prev_i = None, None
                continue
        prev_v, prev_i = v, i
        i += 1
        #time.sleep(1)
    return c
    '''


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #t = int(input())
    t = 1

    for t_itr in range(t):
        #n = int(input())


        #arr = list(map(int, input().rstrip().split()))
        arr = list(map(int, '5 2 1 3 1 2 4 1'.rstrip().split()))
        n = len(arr)

        result = countInversions(arr)
        print(result)

        #fptr.write(str(result) + '\n')

    #fptr.close()
