#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ2439.py
# 
#  Description:
#      Answer code for BOJ 2439
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on Novenber 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

if __name__ == "__main__":
    N = int(input())
    for i in range(N): print(' '*(N-i-1)+'*'*(i+1))