#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ4673.py
# 
#  Description:
#      Answer code for BOJ 4673
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

cache = [False for _ in range(10001)]

def d(gen):
    cache[gen] = True
    ret = gen
    for i in [int(n) for n in str(gen)]: ret += i
    return ret

if __name__ == "__main__":
    for i in range(1, 10001):
        if not cache[i]:
            print(i)
            tmp = i
            while d(tmp) <= 10000: tmp = d(tmp)