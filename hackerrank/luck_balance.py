#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    luck = 0
    for contest in sorted(contests, reverse=True):
        if contest[1] == 0:
            luck += contest[0]
        elif k > 0:
            luck += contest[0]
            k -= 1
        else:
            luck -= contest[0]
    return luck


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ins = [[6, 3, [[5,  1],
                   [2,  1],
                   [1,  1],
                   [8,  1],
                   [10, 0],
                   [5,  0]]]]

    for i in ins:

        n = int(i[0])

        k = int(i[1])

        contests = []

        for l in range(n):
            contests.append(list(map(int, i[2][l])))

        result = luckBalance(k, contests)
        print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
