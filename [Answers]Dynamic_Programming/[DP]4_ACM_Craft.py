# ACM Craft (Baekjoon Online Judge ID: 1005)
# 
# Url: https://www.acmicpc.net/problem/1005
# 
# 
# 알고리즘 분류: 동적계획법과 메모이제이션
# 
# Hint
# 1. input() 대신 sys.stdin.readline()을 사용할 것
# 2. sys.setrecursionlimit(10000000)을 코드 앞줄에 추가할 것


from sys import stdin, setrecursionlimit

INF = 10000000
setrecursionlimit(INF)


D = list()
link = list()
cache = list()


def build_time(target):
    if cache[target] != -1:
        return cache[target]

    ret = D[target]

    for idx, lnk in enumerate(link[target]):
        if lnk:
            ret = max(ret, D[target] + build_time(idx))
    
    cache[target] = ret

    return ret


if __name__ == "__main__":
    T = int(stdin.readline())

    for _ in range(T):
        N, K = map(int, stdin.readline().split())
        D = list(map(int, stdin.readline().split()))
        link = [[False for _ in range(N)] for _ in range(N)]
        cache = [-1 for _ in range(N)]

        for _ in range(K):
            x, y = map(int, stdin.readline().split())
            link[y-1][x-1] = True

        W = int(stdin.readline())

        print(build_time(W-1))