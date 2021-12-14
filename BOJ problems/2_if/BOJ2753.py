#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ2753.py
# 
#  Description:
#      Answer code for BOJ 2753
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on Novenber 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

if __name__ == "__main__":
    year = int(input())
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print('1')
    else: 
        print('0')