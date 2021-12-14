#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ2577.py
# 
#  Description:
#      Answer code for BOJ 2577
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on Novenber 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

if __name__ == "__main__":
    num = 1
    for _ in range(3): num *= int(input())
    res = [0 for _ in range(10)]
    for digit in str(num): res[int(digit)] += 1
    for i in res: print(i)
