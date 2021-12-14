# 구슬 탈출 2 (Baekjoon Online Judge ID: 13460)
# 
# Url: https://www.acmicpc.net/problem/13460
# 
# 
# 알고리즘 분류: 그리디 알고리즘


MIN_MOVE = 10
N, M = 0, 0
visited = list()


def move_upward(ry, rx, by, bx):
    wallflag, holeflag = False, False
    ret_ry, ret_by = 0, 0
    idx = 0
    
    for x in {rx, bx}:
        for y in range(len(table)):
            if table[y][x] == '#':
                wallflag = True
                idx = y

            if table[y][x] == 'O':
                holeflag = True
                idx = y

            if ry == y and rx == x:
                if wallflag:
                    ret_ry = idx+1
                    idx += 1
                if holeflag:
                    ret_ry = -1

            if by == y and bx == x:
                if wallflag:
                    ret_by = idx+1
                    idx += 1
                if holeflag:
                    ret_by = -1

    return ret_ry, rx, ret_by, bx


def find_min_move(table, ry, rx, by, bx, depth):
    if depth == 10:
        return -1

    ret = 11
    visited[10*ry+rx][10*by+bx] = True

    # 위로 이동
    nry, nrx, nby, nbx = move_upward(ry, rx, by, bx)

    if nry == -1:
        return depth + 1
    elif nby == -1:
        return -1
    else:
        if not visited[10*nry+nrx][10*nby+nbx]:
            ret = min(ret if ret != -1 else 11, find_min_move(table, nry, nrx, nby, nbx, depth+1))

    # 아래로 이동
    table = list(reversed(table))
    nry, nrx, nby, nbx = move_upward(ry, rx, by, bx)
    table = list(reversed(table))

    if nry == -1:
        return depth + 1
    elif nby == -1:
        return -1
    else:
        if not visited[10*(N-nry)+nrx][10*(N-nby)+nbx]:
            ret = min(ret if ret != -1 else 11, find_min_move(table, N-1-nry, nrx, N-1-nby, nbx, depth+1))
    
    # 오른쪽 이동
    table = list(reversed(table))
    table = [[table[y][x] for y in range(N)] for x in range(M)]
    nry, nrx, nby, nbx = move_upward(ry, rx, by, bx)
    table = [[table[y][x] for y in range(M)] for x in range(N)]
    table = list(reversed(table))

    if nry == -1:
        return depth + 1
    elif nby == -1:
        return -1
    else:
        if not visited[10*nrx+N-nry][10*nbx+N-nby]:
            ret = min(ret if ret != -1 else 11, find_min_move(table, nrx, N-1-nry, nbx, N-1-nby, depth+1))

    # 왼쪽 이동
    table = [[table[y][x] for y in range(N)] for x in range(M)]
    nry, nrx, nby, nbx = move_upward(ry, rx, by, bx)
    table = [[table[y][x] for y in range(M)] for x in range(N)]

    if nry == -1:
        return depth + 1
    elif nby == -1:
        return -1
    else:
        if not visited[10*nrx+nry][10*nbx+nby]:
            ret = min(ret if ret != -1 else 11, find_min_move(table, nrx, nry, nbx, nby, depth+1))
    
    return ret


if __name__ == "__main__":
    N, M = map(int, input().split())
    table = [[letter for letter in input()] for _ in range(N)]
    visited = [[False for _ in range(100)] for _ in range(100)]
    ry, rx, by, bx = 0, 0, 0, 0

    for y in range(N):
        for x in range(M):
            if table[y][x] == 'R':
                ry, rx = y, x
            if table[y][x] == 'B':
                by, bx = y, x
    
    # print(find_min_move(table, ry, rx, by, bx, 0))

    table = list(reversed(table))
    table = [[table[y][x] for y in range(N)] for x in range(M)]
    print('\n'.join([''.join(line) for line in table]))
    print(move_upward(ry, rx, by, bx))
