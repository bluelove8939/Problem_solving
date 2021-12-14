#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ8958.py
# 
#  Description:
#      Answer code for BOJ 8958
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

import sys

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        res, score, rep = sys.stdin.readline().strip(), 0, 0
        for i in res:
            rep = 0 if i == 'X' else rep + 1
            score += rep
        print(score)