# 타일 채우기 (Baekjoon Online Judge ID: 2133)
# 
# Url: https://www.acmicpc.net/problem/2133
# 
# 
# 알고리즘 분류: 동적계획법과 메모이제이션


cache = list()


def tiling(siz):
    if siz % 2 == 1:
        return 0

    if siz == 0:
        return 1

    if siz == 2:
        return 3
    
    if cache[siz] != -1:
        return cache[siz]

    ret = 3 * tiling(siz-2)

    for i in range(4, siz+1, 2):
        ret += 2 * tiling(siz - i)
    
    return ret


if __name__ == "__main__":
    N = int(input())
    cache = [-1 for _ in range(N+1)]

    print(tiling(N))