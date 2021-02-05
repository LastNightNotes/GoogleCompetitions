"""
Google Code Jam 2020 Round 1B Problem A

Author  : chaotic_iak
Language: Python 3.8.2
"""

################################################### SOLUTION

def initialize_solution():
    pass

def main():
    x,y = read()
    if x%2 == y%2: return "IMPOSSIBLE"
    s = ""
    while x != 0 or y != 0:
        if abs(x)+abs(y) == 1:
            if x == 1: return s+"E"
            if x == -1: return s+"W"
            if y == 1: return s+"N"
            if y == -1: return s+"S"
        if x%2 == 1:
            y //= 2
            if (y%2 == 1 and x%4 == 1) or (y%2 == 0 and x%4 == 3):
                x = (x-1)//2
                s += "E"
            else:
                x = (x+1)//2
                s += "W"
        else:
            x //= 2
            if (x%2 == 1 and y%4 == 1) or (x%2 == 0 and y%4 == 3):
                y = (y-1)//2
                s += "N"
            else:
                y = (y+1)//2
                s += "S"

########################################## PROBLEM CONSTANTS

OUTPUT_PREFIX = "Case #{}: "
INTERACTIVE = False
INTERACTIVE_WRONG_ANSWER = ""

#################################################### HELPERS

import sys

def read(callback=int, split=True):
    ipt = input().strip()
    if INTERACTIVE and ipt == INTERACTIVE_WRONG_ANSWER:
        sys.exit()
    if split:
        return list(map(callback, ipt.split()))
    else:
        return callback(ipt)

def write(value, end="\n"):
    if value is None: return
    try:
        if not isinstance(value, str):
            value = " ".join(map(str, value))
    except:
        pass
    print(value, end=end)
    if INTERACTIVE:
        sys.stdout.flush()

def solve_testcase():
    result = main()
    if result is not None:
        write(result)

if OUTPUT_PREFIX is None:
    solve_testcase()
else:
    initialize_solution()
    TOTAL_CASES, = read()
    for CASE_NUMBER in range(1, TOTAL_CASES+1):
        write(OUTPUT_PREFIX.format(CASE_NUMBER), end="")
        solve_testcase()
