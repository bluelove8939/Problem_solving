#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ10952.py
# 
#  Description:
#      Answer code for BOJ 10952
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on Novenber 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

if __name__ == "__main__":
    while True:
        A, B = map(int, input().split())
        if A == 0 and B == 0: break
        else: print(A+B)