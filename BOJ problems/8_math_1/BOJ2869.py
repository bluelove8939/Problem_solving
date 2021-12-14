#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ2869.py
# 
#  Description:
#      Answer code for BOJ 2869
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

if __name__ == "__main__":
    a, b, v = map(int, input().split())
    lo, hi = 1, v
    while lo < hi:
        mid = int((lo + hi) / 2)
        if v <= mid * a - (mid - 1) * b: hi = mid
        else: lo = mid + 1
    print(lo)
