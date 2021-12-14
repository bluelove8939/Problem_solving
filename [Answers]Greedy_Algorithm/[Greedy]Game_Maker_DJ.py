# 게임을 만든 동준 (Baekjoon Online Judge ID: 2847)
# 
# Url: https://www.acmicpc.net/problem/2847
# 
# 
# 알고리즘 분류: 그리디 알고리즘


if __name__ == "__main__":
    N = int(input())
    scores = [int(input()) for _ in range(N)]
    priv = scores[-1]
    cnt = 0

    for s in reversed(scores[:-1]):
        if priv <= s:
            cnt += s - priv + 1
            priv = priv - 1
        else:
            priv = s
    
    print(cnt)
