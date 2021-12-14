#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ10872.py
# 
#  Description:
#      Answer code for BOJ 10872
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

def factorial(N):
    if N == 0: return 1;
    return N * factorial(N-1)

if __name__ == "__main__":
    N = int(input())
    print(factorial(N))