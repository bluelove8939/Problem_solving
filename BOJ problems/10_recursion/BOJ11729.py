#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ11729.py
# 
#  Description:
#      Answer code for BOJ 11729
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

log = list()

def hanoi(plt, cur, dest, rem):
    if plt == 1:
        log.append("{} {}".format(cur, dest))
        return 1
    
    result = 0

    result += hanoi(plt-1, cur, rem, dest)
    result += hanoi(1, cur, dest, rem)
    result += hanoi(plt-1, rem, dest, cur)

    return result

if __name__ == "__main__":
    N = int(input())
    print(hanoi(N, 1, 3, 2))
    for line in log: print(line)