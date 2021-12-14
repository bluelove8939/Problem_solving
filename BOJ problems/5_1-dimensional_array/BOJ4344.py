#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ4344.py
# 
#  Description:
#      Answer code for BOJ 4344
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

import sys

if __name__ == "__main__":
    C = int(input())
    for _ in range(C):
        scores, avg, cnt = list(map(int, sys.stdin.readline().split())), 0, 0
        for sc in scores[1:]: avg += sc
        for sc in scores[1:]: cnt = cnt+1 if sc > avg/scores[0] else cnt
        print("{:<.3f}%".format(cnt/scores[0]*100))