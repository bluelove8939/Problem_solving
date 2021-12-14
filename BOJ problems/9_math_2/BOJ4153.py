#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ4253.py
# 
#  Description:
#      Answer code for BOJ 4253
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

if __name__ == "__main__":
    while True:
        le = list(map(int, input().split()))
        if le[0] == 0 and le[1] == 0 and le[2] == 0: break
        le.sort()
        print("right" if le[0] ** 2 + le[1] ** 2 == le[2] ** 2 else "wrong")