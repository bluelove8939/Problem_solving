#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ2292.py
# 
#  Description:
#      Answer code for BOJ 2292
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

if __name__ == "__main__":
    N = int(input())
    route = 1
    while N > 3 * (route ** 2) - 3 * route + 1: route += 1
    print(route)