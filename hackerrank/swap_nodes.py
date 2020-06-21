#!/bin/python3

import os
import sys

'''
g = {
    1: {'l': 2, 'r': 3, 'done': False, 'saw': False},
    2: {'l': -1, 'r': 4, 'done': False, 'saw': False},
    3: {'l': -1, 'r': 5, 'done': False, 'saw': False},
    4: {'l': -1, 'r': -1, 'done': False, 'saw': False},
    5: {'l': -1, 'r': -1, 'done': False, 'saw': False}
}
g = {
    1: {'l': 2, 'r': 3, 'done': False, 'saw': False},
    2: {'l': -1, 'r': -1, 'done': False, 'saw': False},
    3: {'l': -1, 'r': -1, 'done': False, 'saw': False}
}
'''

#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    from collections import deque
    import copy

    g = {k+1:{'l':v[0], 'r': v[1]} for (k,v) in enumerate(indexes)}
    done_reset = {k+1:False for (k,v) in enumerate(indexes)}
    saw_reset = {k+1:False for (k,v) in enumerate(indexes)}
    swap_reset = [False]*(1+len(indexes)*2)

    all_orders = []
    for k in queries:
        done = copy.copy(done_reset)
        saw = copy.copy(saw_reset)
        swap = copy.copy(swap_reset)
        #print(f"\n{g}\n{done}\n{saw}")
        stack = deque()
        cur = 1
        lvl = 1
        order = []
        while(True):
            #print('='*5, cur, g[cur], lvl, lvl % k, done[cur], saw[cur], swap[cur])
            if lvl % k == 0 and not swap[cur]:
                # perform left-right swap
                swap[cur] = True
                g[cur]['l'], g[cur]['r'] = g[cur]['r'], g[cur]['l']
            if g[cur]['l'] != -1 and not done[g[cur]['l']]:
                stack.append(cur)
                cur = g[cur]['l']
                lvl += 1
                continue
            if not saw[cur]:
                #print("-"*10, cur)
                saw[cur] = True
                order.append(cur)
            if g[cur]['r'] != -1 and not done[g[cur]['r']]:
                #print(cur)
                stack.append(cur)
                cur = g[cur]['r']
                lvl += 1
                continue
            else:
                done[cur] = True
                if stack:
                    cur = stack.pop()
                    lvl -= 1
                    continue
                else:
                    break;
        all_orders.append(order)
    return all_orders


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    expected = []
    for _ in range(queries_count):
        expected.append(list(map(int, input().rstrip().split())))

    result = swapNodes(indexes, queries)

    print('RESULT:', result)
    if result != expected:
        print('WRONG! ', expected)
    else:
        print('OK')

    #fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    #fptr.write('\n')

    #fptr.close()
