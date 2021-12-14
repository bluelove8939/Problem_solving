#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ10818.py
# 
#  Description:
#      Answer code for BOJ 10818
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on Novenber 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

import sys

MAX = 1000000
MIN = -1000000

if __name__ == "__main__":
    N = int(input())
    num = map(int, sys.stdin.readline().split())
    mi, ma = MAX, MIN
    for i in num:
        mi = i if mi > i else mi
        ma = i if ma < i else ma
    print(mi, ma)