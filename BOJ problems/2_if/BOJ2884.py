#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ2884.py
# 
#  Description:
#      Answer code for BOJ 2884
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on Novenber 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

if __name__ == "__main__":
    H, M = map(int, input().split())
    if M >= 45: M -= 45
    else:
        M += 15
        H -= 1
        if H < 0: H += 24
    print(H, M)