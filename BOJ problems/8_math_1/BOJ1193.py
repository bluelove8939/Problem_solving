#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ1193.py
# 
#  Description:
#      Answer code for BOJ 1193
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

if __name__ == "__main__":
    X, lv = int(input()), 1
    while X > lv * (lv + 1) / 2: lv += 1
    X -= int(lv * (lv - 1) / 2)
    if lv % 2 == 0: print("{}/{}".format(X, lv-X+1))
    else: print("{}/{}".format(lv-X+1, X))
