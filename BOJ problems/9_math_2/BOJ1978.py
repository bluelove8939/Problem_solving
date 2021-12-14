#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ1978.py
# 
#  Description:
#      Answer code for BOJ 1978
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

import sys

MAX_NUM = 1000
cache = [True for _ in range(MAX_NUM+1)]

if __name__ == "__main__":
    N, cnt = int(input()), 0
    
    cache[1] = False
    for num in range(2, MAX_NUM+1):
        if cache[num]:
            coef = 2
            while MAX_NUM >= num * coef:
                cache[num * coef] = False
                coef += 1

    for num in map(int, sys.stdin.readline().split()):
        if cache[num]: cnt += 1
    
    print(cnt)