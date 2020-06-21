#!/bin/python3

import math
import os
import random
import re
import sys

def check(s1, s2):
    # This could be optimized by comparing
    # chars count in the strings instead of sorting
    if len(s1)!=len(s2):
        return False
    if(sorted(s1)== sorted(s2)):
        return True
    else:
        return False

def searchAnagram(highstack, needle, initial_position):
    window = len(needle)
    i = 0
    c = 0
    while (i+window <= len(highstack)):
        frame = highstack[i:i+window]
        if i > initial_position and check(frame, needle):
            #print(frame, needle, initial_position)
            c = c + 1
        i = i + 1
    return c

def generateAnagrams(s):
    arr = []
    for i in range(0, len(s)):
        for j in range(i + 1, len(s)):
            arr.append((s[i:j],i))
    return arr

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    arr = generateAnagrams(s)
    c = 0
    for a, i in arr:
        c = c + searchAnagram(s, a, i)
    return c

if __name__ == '__main__':
    inputarr = ['ifailuhkqq', 'kkkk']
    q = len(inputarr)
    for q_itr in range(q):
        s = inputarr[q_itr]
        result = sherlockAndAnagrams(s)
        print("RESULT:", result)
