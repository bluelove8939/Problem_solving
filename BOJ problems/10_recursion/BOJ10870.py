#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ10870.py
# 
#  Description:
#      Answer code for BOJ 10870
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

def fibonacci(N):
    if N == 0: return 0
    if N == 1: return 1
    return fibonacci(N-1) + fibonacci(N-2)

if __name__ == "__main__":
    N = int(input())
    print(fibonacci(N))