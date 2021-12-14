#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ1712.py
# 
#  Description:
#      Answer code for BOJ 1712
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

import math

if __name__ == "__main__":
    A, B, C = map(int, input().split())
    bep = -1 if C <= B else math.floor(A / (C - B)) + 1
    print(bep)