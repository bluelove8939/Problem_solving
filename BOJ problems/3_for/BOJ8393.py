#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ8393.py
# 
#  Description:
#      Answer code for BOJ 8393
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on Novenber 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

if __name__ == "__main__":
    n = int(input())
    sum = 0
    for i in range(1, n+1): sum += i
    print(sum)