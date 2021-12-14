#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ1011.py
# 
#  Description:
#      Answer code for BOJ 1011
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

if __name__ == "__main__":
    for _ in range(int(input())):
        x, y = map(int, input().split())

        dist, cnt = y - x, 0
        while dist > cnt ** 2 + cnt: cnt += 1

        if dist > cnt ** 2: cnt *= 2
        else: cnt = 2 * cnt - 1

        print(cnt)