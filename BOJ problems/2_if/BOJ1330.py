#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ1330.py
# 
#  Description:
#      Answer code for BOJ 1330
#  
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on Novenber 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

if __name__ == "__main__":
    a, b = map(int, input().split())
    if a > b: print('>')
    elif a < b: print('<')
    else: print('==')