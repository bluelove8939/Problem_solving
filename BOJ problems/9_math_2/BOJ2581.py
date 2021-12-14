#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ2581.py
# 
#  Description:
#      Answer code for BOJ 2581
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

MAX_NUM = 10000
cache = [True for _ in range(MAX_NUM+1)]

if __name__ == "__main__":
    M, N, p_sum, p_min = int(input()), int(input()), 0, 0

    cache[1] = False
    for num in range(2, N+1):
        if cache[num]:
            coef = 2
            while N >= num * coef:
                cache[num * coef] = False
                coef += 1

    for num in range(M, N+1):
        if cache[num]:
            p_sum += num
            p_min = num if p_min == 0 else p_min
    
    if p_sum == 0: print(-1)
    else: print("{}\n{}".format(p_sum, p_min))