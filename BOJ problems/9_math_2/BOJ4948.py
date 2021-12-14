#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ4948.py
# 
#  Description:
#      Answer code for BOJ 4948
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

MAX_N = 123456
cache = [True for _ in range(2 * MAX_N + 1)]

if __name__ == "__main__":
    while True:
        n, cnt = int(input()), 0
        if n == 0: break

        cache[1] = False
        for num in range(2, 2*n+1):
            if cache[num]:
                for i in range(2*num, 2*n+1, num):
                    cache[i] = False

        for num in range(n+1, 2*n+1):
            if cache[num]: cnt += 1

        print(cnt)