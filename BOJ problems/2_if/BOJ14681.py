#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ14681.py
# 
#  Description:
#      Answer code for BOJ 14681
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on Novenber 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

if __name__ == "__main__":
    x, y = int(input()), int(input())
    if x > 0:
        if y > 0: print(1)
        else: print(4)
    else:
        if y > 0: print(2)
        else: print(3)