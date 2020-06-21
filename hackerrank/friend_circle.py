#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxCircle function below.
def maxCircle(queries):

    # inspired by https://www.hackerearth.com/practice/notes/disjoint-set-union-union-find/
    arr = {}
    size = {}

    s = set()
    for a, b in queries:
        s.add(a)
        s.add(b)

    def initialize():
        for e in s:
            arr[e] = e
            size[e] = 1

    def root(i):
        if i not in arr.keys():
            return i
        while arr[i] != i:  # chase parent of current element until it reaches root.
            i = arr[i];
        return i;


    def weighted_union(a, b, max_size):
        root_a = root(a);
        root_b = root(b);
        if root_a != root_b:
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a
            arr[root_b] = arr[root_a];
            size[root_a] += size[root_b];
            max_size = max(max_size, size[root_a])
        return max_size

    res = []
    max_size = 2
    initialize()
    for a, b in queries:
        #print(a, b)
        max_size = weighted_union(a, b, max_size)
        #print(max_size)
        #print(arr)
        #print(size)
        res.append(max_size)

    return res

    '''
    # SUBOPTIMAL, TOO SLOW
    stx = defaultdict(set)  # formed cicles of friends as sets
    idx = defaultdict(int)  # each person to the set reference
    cnt = defaultdict(int)  # count for each set
    res = []

    for a, b in queries:
        if a > b:
            a, b = b, a
        label = idx[a]
        if not label:
            label = a

        rm_label = idx[b]
        if rm_label:
            c = len(stx[rm_label])
            cnt[label] += c
            for e in stx[rm_label]:
                idx[e] = label
                stx[label].add(e)
            stx.pop(rm_label)
            cnt.pop(rm_label)

        stx[label] |= {a, b}
        cnt[label] = len(stx[label])
        idx[a] = label
        idx[b] = label

        res.append(max(cnt.values()))
    #print(stx)
    #print(idx)
    #print(cnt)
    return res
    '''



if __name__ == '__main__':

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    exp = []
    r = True
    while True:
        try:
            r = int(input().strip())
            exp.append(r)
        except EOFError as e:
            break

    if ans != exp:
        print('RESULT: ', ans)
        print('WRONG! ', exp)
    else:
        print('OK')
