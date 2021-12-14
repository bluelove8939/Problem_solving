#  Copyright (C) 2020 by Sungwook Kim, All rights reserved.
#
#  filename: BOJ2447.py
# 
#  Description:
#      Answer code for BOJ 2447
#
#  Written on November 08, 2020
#  Modification history:
#      1. Written by Sung Wook Kim on November 08, 2020
#
#  Compiler used: Python 3.7.8 [MSC v.1916 64 bit (AMD64)]

import math

MAX_N = int(math.pow(3, 8))
board = [[' ' for _ in range(MAX_N)] for _ in range(MAX_N)]

def draw_dot(N, x, y, siz):
    if siz == 1: 
        board[x][y] = '*'
        return

    nxt_siz = int(siz/3)
    
    draw_dot(N, x, y, nxt_siz)
    draw_dot(N, x + nxt_siz, y, nxt_siz)
    draw_dot(N, x + 2 * nxt_siz, y, nxt_siz)

    draw_dot(N, x, y + nxt_siz, nxt_siz)
    draw_dot(N, x + 2 * nxt_siz, y + nxt_siz, nxt_siz)

    draw_dot(N, x, y + 2 * nxt_siz, nxt_siz)
    draw_dot(N, x + nxt_siz, y + 2 * nxt_siz, nxt_siz)
    draw_dot(N, x + 2 * nxt_siz, y + 2 * nxt_siz, nxt_siz)

if __name__ == "__main__":
    N = int(input())
    draw_dot(N, 0, 0, N)
    for i in range(N):
        print("".join(board[i][:N]))