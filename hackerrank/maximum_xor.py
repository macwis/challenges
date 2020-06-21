#!/bin/python3

import math
import os
import random
import re
import sys

import pprint
import json

class BinaryTrie:
    next = {'val': ''}

    def append(self, no):
        current = preview = self.next
        q = f"{no:032b}"
        for bit in q:
            bit = int(bit)
            if bit not in current:
                current[bit] = {'val': current['val'] + str(bit)}
            preview = current
            current = current[bit]
        current['*'] = True

    def closest_max(self, query):
        current = self.next
        q = f"{query:032b}"
        #print(f'query: {b}')
        closest_max = ''

        tmp_q = q
        c = 32
        for k, bit in enumerate(q):
            bit = int(bit)
            opp = bit ^ 1
            if opp in current:
                #print(f' turn: {c}, {l}->{opp}')
                tmp_q = tmp_q[:k] + str(opp) + tmp_q[k+1:]
                #print(f'query: {b}')
                #print(f' tmpq: {tmp_b}')
                #print(f"  val: {current['val'].ljust(32)}\n")
                bit = opp
            current = current[bit]
            closest_max += str(bit)
            #print(f'     _ {closest_max.ljust(32)}')
            c -= 1
        #print(f'  ret: {closest_max}')
        return int(closest_max, 2)

    def __str__(self):
        return str(self.next)


# Complete the maxXor function below.
def maxXor(arr, queries):
    bt = BinaryTrie()
    results = []
    for a in arr:
        bt.append(a)
    #print(json.dumps(d.next, indent=1))
    for q in queries:
        results.append(q ^ bt.closest_max(q))
        #print(results)
    return results

    '''
    # NAIVE SOLUTION
    max = [-math.inf]*len(queries)
    for k, q in enumerate(queries):
        for a in arr:
            r = q ^ a
            if r > max[k]:
                max[k] = r
    #print(max)
    return max
    '''

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    queries = []

    for _ in range(m):
        queries_item = int(input())
        queries.append(queries_item)

    result = maxXor(arr, queries)

    for s_itr in range(m):
        expected = int(input())
        print('RESULT:', result[s_itr])
        if result[s_itr] != expected:
            print('WRONG! ', expected)
        else:
            print('OK')
