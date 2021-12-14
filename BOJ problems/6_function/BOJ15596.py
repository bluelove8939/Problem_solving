#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ15596.py
# 
#  Description:
#      Answer code for BOJ 15596
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

def solve(a) -> int:
    ret = 0
    for num in a: ret += num
    return ret