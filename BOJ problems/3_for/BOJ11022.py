#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ11022.py
# 
#  Description:
#      Answer code for BOJ 11022
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on Novenber 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

if __name__ == "__main__":
    T = int(input())
    for x in range(1, T+1):
        A, B = map(int, input().split())
        print("Case #{}: {} + {} = {}".format(x, A, B, A+B))