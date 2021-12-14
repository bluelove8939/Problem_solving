#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ3053.py
# 
#  Description:
#      Answer code for BOJ 3053
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

import math

if __name__ == "__main__":
    r = int(input())
    print("{:.6f}".format(r * r * math.pi))
    print("{:.6f}".format(r * r * 2))