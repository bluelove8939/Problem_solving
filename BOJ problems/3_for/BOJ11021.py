#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ11021.py
# 
#  Description:
#      Answer code for BOJ 11021
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on Novenber 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

if __name__ == "__main__":
    T = int(input())
    for i in range(1, T+1):
        A, B = map(int, input().split())
        print("Case #{}: {}".format(i, A+B))