#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ10250.py
# 
#  Description:
#      Answer code for BOJ 10250
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

import math

if __name__ == "__main__":
    for _ in range(int(input())):
        H, W, N = map(int, input().split())

        room = math.floor(N/H)
        stories = N % H 

        if N % H == 0: stories += H
        else: room += 1

        print("{}{:02d}".format(stories, room))
