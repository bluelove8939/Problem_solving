#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ1546.py
# 
#  Description:
#      Answer code for BOJ 1546
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

import sys

if __name__ == "__main__":
    N = int(input())
    num = map(int, sys.stdin.readline().split())
    avg, ma = 0, 0
    for n in num:
        avg += n
        ma = n if ma < n else ma
    print(avg / N / ma * 100)