#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ1002.py
# 
#  Description:
#      Answer code for BOJ 1002
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

import math

if __name__ == "__main__":
    for _ in range(int(input())):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        dist = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)
        if dist == 0:
            if r1 == r2: print(-1)
            else: print(0)
        elif dist > r1 + r2 or dist < abs(r1-r2): print(0)
        elif dist == r1 + r2 or dist == abs(r1-r2): print(1)
        else: print(2)
