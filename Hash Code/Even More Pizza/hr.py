#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def abbreviation(a,b):
    if a == b: return "YES"
    d = {}
    # print(a,b)
    for char in a:
        if char.isupper():
            if char not in b: return "NO"
            if a.count(char) > b.count(char): return "NO"
    
    index = len(a)
    c = a
    for char in b:
        if char.lower() not in c:
            if char not in c:
                return "NO"
            else: index = c.index(char)
        else:
            if char not in c: index = c.index(char.lower()) 
            else: 
                index = min(c.index(char),c.index(char.lower())) 
        if b.count(char) > a.count(char) + a.count(char.lower()):
            return "NO"
        j = c[:index]
        # for t in c[:index]:
        #     if t.isupper(): return "NO"
        c = c[index+1:]
        # print(c)
    return "YES"
    

if __name__ == '__main__':
    with open("textcase.txt", 'r') as f:     
        n = int(f.readline())
        for q_itr in range(n):
            a = f.readline()
            b = f.readline()

            result = abbreviation(a, b)
            print(result)
# YES
# YES
# YES
# YES
# YES
# YES
# YES
# NO
# YES
# NO