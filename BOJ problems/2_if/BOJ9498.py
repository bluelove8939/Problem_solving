#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ9498.py
# 
#  Description:
#      Answer code for BOJ 9498
#  
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on Novenber 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

if __name__ == "__main__":
    score = int(input())
    if score >= 90: print('A')
    elif score >= 80: print('B')
    elif score >= 70: print('C')
    elif score >= 60: print('D')
    else: print('D')