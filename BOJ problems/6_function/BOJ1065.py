#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ1065.py
# 
#  Description:
#      Answer code for BOJ 1065
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

def isHan(num):
    if num < 100: return True

    digit = [int(n) for n in str(num)]
    priv, post = digit[0], digit[1]
    diff = priv - post

    for i in digit[2:]:
        priv, post = post, i
        if diff != priv - post: return False

    return True

if __name__ == "__main__":
    N, cnt = int(input()), 0
    for i in range(1, N+1):
        if isHan(i): cnt += 1
    print(cnt)