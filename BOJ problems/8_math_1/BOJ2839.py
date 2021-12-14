#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ2839.py
# 
#  Description:
#      Answer code for BOJ 2839
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

if __name__ == "__main__":
    N, bag = int(input()), 0

    while N % 5 != 0:
        N -= 3
        bag += 1

    if N < 0: print(-1)
    else: print(bag + int(N / 5))