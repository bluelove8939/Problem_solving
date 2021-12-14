#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ1110.py
# 
#  Description:
#      Answer code for BOJ 1110
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on Novenber 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

if __name__ == "__main__":
    N = int(input())
    prv = N
    cycle = 0

    while True:
        nxt = 0
        for i in [int(digit) for digit in str(prv)]: nxt += i
        nxt = 10 * (prv % 10) + (nxt % 10)
        cycle += 1
        if nxt == N: break
        else: prv = nxt
        
    print(cycle)