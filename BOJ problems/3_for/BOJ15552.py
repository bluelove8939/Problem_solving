#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ15552.py
# 
#  Description:
#      Answer code for BOJ 15552
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on Novenber 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

import sys

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        A, B = map(int, sys.stdin.readline().split())
        print(A+B)