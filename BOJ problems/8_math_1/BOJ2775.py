#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ2775.py
# 
#  Description:
#      Answer code for BOJ 2775
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

import math

CACHE_SIZ = 15
resident = [0 for _ in range(CACHE_SIZ)]

if __name__ == "__main__":
    for _ in range(int(input())):
        k, n = int(input()), int(input())
        for i in range(n): resident[i] = i + 1
        for _ in range(k):
            for i in range(n):
                resident[i] += resident[i - 1]
        print(resident[n-1])
