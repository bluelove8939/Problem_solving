# 정수 삼각형 (Baekjoon Online Judge ID: 1149)
# 
# Url: https://www.acmicpc.net/problem/1149
# 
# 
# 알고리즘 분류: 동적계획법과 메모이제이션
# 
# Hint
# 1. sys.setrecursionlimit(10000000)을 코드 앞줄에 추가할 것 


from sys import setrecursionlimit

INF = 10000000
setrecursionlimit(INF)


N = 0
house = list()
cache = list()


def min_cost(cursor, restraint):
    if cursor == N:
        return 0
    
    if cache[cursor][restraint] != -1:
        return cache[cursor][restraint]

    ret = INF

    if restraint != 0:
        ret = min(ret, house[cursor][0] + min_cost(cursor+1, 0))

    if restraint != 1:
        ret = min(ret, house[cursor][1] + min_cost(cursor+1, 1))

    if restraint != 2:
        ret = min(ret, house[cursor][2] + min_cost(cursor+1, 2))

    cache[cursor][restraint] = ret

    return ret


if __name__ == "__main__":
    N = int(input())
    house = [list(map(int, input().split())) for _ in range(N)]
    cache = [[-1 for _ in range(3)] for _ in range(N)]

    print(min_cost(0, -1))