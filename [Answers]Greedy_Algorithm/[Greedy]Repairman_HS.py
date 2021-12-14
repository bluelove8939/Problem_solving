# 수리공 항승 (Baekjoon Online Judge ID: 1449)
# 
# Url: https://www.acmicpc.net/problem/1449
# 
# 
# 알고리즘 분류: 그리디 알고리즘
#   
# Hint
# 1. 이 문제는 그리디 알고리즘을 이용하여 풀 수 있다.


from sys import stdin


if __name__ == "__main__":
    N, L = map(int, input().split())
    leak = list(map(int, input().split()))
    coverage, cnt = 0, 0

    leak.sort()

    for pt in leak:
        if coverage < pt:
            coverage = pt + L - 0.5
            cnt += 1
        
    print(cnt)