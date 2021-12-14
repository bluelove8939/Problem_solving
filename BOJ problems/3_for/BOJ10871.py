#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ10871.py
# 
#  Description:
#      Answer code for BOJ 10871
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on Novenber 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

if __name__ == "__main__":
    N, X = map(int, input().split())
    for i in map(int, input().split()):
        if i < X: print(i, end=" ")