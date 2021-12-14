# 안전영역 (Baekjoon Online Judge ID: 2468)
# 
# Url: https://www.acmicpc.net/problem/2468
# 
# 
# 알고리즘 분류: 브루트포스
#   
# Hint
# 1. 이 문제는 브루트포스 문제이다.
# 
#
# 풀이
# - 브루트포스란 문제에서 제시하는 상황을 풀기 위해 해야하는 모든 작업을 프로그램의
#   형태로 그래도 옮기는 것을 의미한다. 대부분의 경우 브루트포스 문제들은 데이터셋의
#   크기가 작으므로 효율을 따질 필요가 없다.
#  
# - 브루트포스 


from sys import setrecursionlimit

setrecursionlimit(100000)


MAX_HEIGHT = 101


# 인접한 모든 배열의 요소를 동일한 값으로 변환하는 함수
def  fill_adjacent(arr, col, row, siz, value):
    arr[col][row] = value

    if col != 0:
        if arr[col-1][row] != value:
            fill_adjacent(arr, col-1, row, siz, value)
    if row != 0:
        if arr[col][row-1] != value:
            fill_adjacent(arr, col, row-1, siz, value)
    if col < siz-1:
        if arr[col+1][row] != value:
            fill_adjacent(arr, col+1, row, siz, value)
    if row < siz-1:
        if arr[col][row+1] != value:
            fill_adjacent(arr, col, row+1, siz, value)


if __name__ == "__main__":
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    res = 0

    # 모든 높이에 대해 동일한 알고리즘을 수행한다
    for height in range(MAX_HEIGHT):
        # 어떤 지역이 주어진 높이에서 안전지역인지를 판별한다
        safe = [[item > height for item in row] for row in area]
        cnt = 0

        for i in range(N):
            for j in range(N):
                # 만약 어떤 지역이 안전지역이면,
                if safe[i][j]:
                    # cnt를 1증가시키고
                    cnt += 1
                    # 인접한 모든 지역을 False로 한다
                    fill_adjacent(safe, i, j, N, False)

        res = max(res, cnt)

    print(res)
