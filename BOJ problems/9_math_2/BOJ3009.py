#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ3009.py
# 
#  Description:
#      Answer code for BOJ 3009
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

if __name__ == "__main__":
    pt = [list(map(int, input().split())) for _ in range(3)]
    x, y = list(), list()

    for p in pt:
        if p[0] in x: x.remove(p[0])
        else: x.append(p[0])
        if p[1] in y: y.remove(p[1])
        else: y.append(p[1])

    print(x[0], y[0])