#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ3052.py
# 
#  Description:
#      Answer code for BOJ 3052
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

if __name__ == "__main__":
    cache, cnt = [0 for _ in range(42)], 0
    for _ in range(10): cache[int(input()) % 42] += 1
    for i in cache: cnt += i
    print(cnt)