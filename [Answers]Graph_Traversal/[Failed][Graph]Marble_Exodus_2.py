# 구슬 탈출 2 (Baekjoon Online Judge ID: 13460)
# 
# Url: https://www.acmicpc.net/problem/13460
# 
# 
# 알고리즘 분류: 그래프 탐색


N, M = None, None
hole = []
plate = []

MAX_DEPTH = 10


def dfs(red, blue, axis, direction, depth = 0):
    if depth >= MAX_DEPTH:
        return -1

    # if axis == 0 and direction == 0: move toward positive row direction
    # if axis == 0 and direction == 1: move toward negative row direction
    # if axis == 1 and direction == 0: move toward positive column direction
    # if axis == 1 and direction == 1: move toward negative column direction

    if red[axis] == blue[axis] and direction == 0:
        pre = "red" if red[abs(axis-1)] < blue[abs(axis-1)] else "blue"
        pos = "red" if red[abs(axis-1)] > blue[abs(axis-1)] else "blue"
    elif red[axis] == blue[axis] and direction == 1:
        pre = "red" if red[abs(axis-1)] > blue[abs(axis-1)] else "blue"
        pos = "red" if red[abs(axis-1)] < blue[abs(axis-1)] else "blue"
    else:
        pre, pos = "red", "blue"


    # 'pre' is precedent to 'pos' according to the given direction
    # so the position of 'pos' needs to be decided first
    # pre          pos         wall    =>                    pre pos wall
    # ---------------------------->         ---------------------------->

    pre_marvel = red if pre == "red" else blue
    pos_marvel = red if pos == "red" else blue


    # 1. find out the next positoin of 'pos'
    nxt_idx = pos_marvel[abs(axis-1)]

    while nxt_idx != hole[abs(axis-1)] and \
            (plate[nxt_idx][pos_marvel[1]] if axis == 0 else plate[pos_marvel[0]][nxt_idx]) != 1:
        if direction == 0:
            nxt_idx += 1
        else:
            nxt_idx -= 1

    if nxt_idx == hole[abs(axis-1)]:
        if pos == "blue":
            return -1
        else:
            return depth + 1
    else:
        pos_marvel[abs(axis-1)] = nxt_idx


    # 2. find out the next positoin of 'pos'
    nxt_idx = pre_marvel[abs(axis-1)]

    while nxt_idx != hole[abs(axis-1)] and \
            (plate[nxt_idx][pre_marvel[1]] if axis == 0 else plate[pre_marvel[0]][nxt_idx]) != 1 and \
            (nxt_idx != pos_marvel[abs(axis-1)] if red[axis] == blue[axis] else True):
        if direction == 0:
            nxt_idx += 1
        else:
            nxt_idx -= 1

    if nxt_idx == hole[abs(axis-1)]:
        if pre == "blue":
            return -1
        else:
            return depth + 1
    else:
        pre_marvel[abs(axis-1)] = nxt_idx

    print(f"ax {axis}  di {direction}  red {red}  blue {blue}")


    # Graph traversal
    red = pre_marvel if pre == "red" else pos_marvel
    blue = pre_marvel if pre == "blue" else pos_marvel

    ret = MAX_DEPTH

    for ax in range(2):       # axis can be 0 or 1
        for di in range(2):   # direction can be 0 or 1
            val = dfs(red, blue, axis=ax, direction=di, depth=depth+1)
            if val != -1:
                ret = min(ret, val)

    return ret


def solve(red, blue):
    ret = MAX_DEPTH

    for ax in range(2):      # axis can be 0 or 1
        for di in range(2):  # direction can be 0 or 1
            val = dfs(red, blue, axis=ax, direction=di, depth=0)
            if val != -1:
                ret = min(ret, val)

    return ret


if __name__ == '__main__':
    N, M = map(int, input().split())
    red  = [None, None]
    blue = [None, None]
    hole = [None, None]
    plate = []

    for ridx in range(N):
        plate.append([])
        for cidx, lt in enumerate(input()):
            if lt == 'R':
                red[0] = ridx
                red[1] = cidx
                plate[-1].append(0)

            elif lt == 'B':
                blue[0] = ridx
                blue[1] = cidx
                plate[-1].append(0)

            elif lt == 'O':
                hole[0] = ridx
                hole[1] = cidx
                plate[-1].append(0)

            elif lt == '#':
                plate[-1].append(1)

            else:
                plate[-1].append(0)

    print(solve(red, blue))
