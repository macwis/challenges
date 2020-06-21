#!/bin/python3
'''
Solution of HackerRank Challenge:
https://www.hackerrank.com/challenges/fraudulent-activity-notifications
'''

import math
import os
import random
import re
import sys

from collections import deque

MAX = 200

def median(counts, d):
    d_half_floored = d // 2
    median_low = 0
    median_high = 0
    traversed_elements = counts[0]
    idx = 1
    while traversed_elements <= d_half_floored:
        median_high = idx
        if traversed_elements < d_half_floored:
            median_low = idx  # still too low
        traversed_elements += counts[idx]
        idx += 1
    if d % 2 != 0:
        return median_high  # d is odd
    else:
        return (median_low + median_high) / 2  # d is even

def activityNotifications(expenditure, n, d):
    trailing_exps = deque([])
    counts = [0] * MAX
    notifications = 0
    med = 0
    for day in range(n):
        if day >= d:
            med = median(counts, d)
            if expenditure[day] >= 2 * med:
                notifications += 1
            counts[trailing_exps.popleft()] -= 1
        counts[expenditure[day]] += 1
        trailing_exps.append(expenditure[day])
    return notifications

def test_activityNotifications():
    # case 1
    n, d = tuple(map(int, '9 5'.split()))
    expenditure = list(map(int, '2 3 4 2 3 6 8 4 5'.split()))
    expected = 2
    assert activityNotifications(expenditure, n, d) == expected
    # case 2
    n, d = tuple(map(int, '5 4'.split()))
    expenditure = list(map(int, '1 2 3 4 4'.split()))
    expected = 0
    assert activityNotifications(expenditure, n, d) == expected


if __name__ == '__main__':
    n, d = tuple(map(int, input().rstrip().split()))
    expenditure = list(map(int, input().rstrip().split()))
    result = activityNotifications(expenditure, n, d)
    print(result)
