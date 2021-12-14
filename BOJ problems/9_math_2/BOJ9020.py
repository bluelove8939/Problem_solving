#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ9020.py
# 
#  Description:
#      Answer code for BOJ 9020
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

MAX_N = 10000

cache = [True for _ in range(2 * MAX_N + 1)]
cache[1] = False

for num in range(2, MAX_N+1):
    if cache[num]:
        for i in range(2*num, MAX_N+1, num):
            cache[i] = False

if __name__ == "__main__":
    for _ in range(int(input())):
        n, gold = int(input()), 0

        for num in range(int(n/2), 1, -1):
            if cache[num] and cache[n-num]: 
                gold = num
                break

        print(gold, n-gold)