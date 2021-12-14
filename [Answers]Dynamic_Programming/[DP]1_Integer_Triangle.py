# 정수 삼각형 (Baekjoon Online Judge ID: 1932)
# 
# Url: https://www.acmicpc.net/problem/1932
# 
# 
# 알고리즘 분류: 동적계획법과 메모이제이션


n = 0
triangle = list()
cache = list()


def largest_path(row, col):
    if row == n:
        return 0
    
    if cache[row][col] != -1:
        return cache[row][col]

    ret = triangle[row][col] + max(largest_path(row+1, col), largest_path(row+1, col+1))

    cache[row][col] = ret

    return ret


if __name__ == "__main__":
    n = int(input())
    triangle = [list(map(int, input().split())) for _ in range(n)]
    cache = [[-1 for _ in range(n)] for _ in range(n)]

    print(largest_path(0, 0))