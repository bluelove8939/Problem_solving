# 캠핑 (Baekjoon Online Judge ID: 4796)
# 
# Url: https://www.acmicpc.net/problem/4796
# 
# 
# 알고리즘 분류: 그리디 알고리즘


from sys import stdin


if __name__ == "__main__":
    T = 1

    while True:
        L, P, V = map(int, stdin.readline().split())

        if L == 0:
            break

        print("Case {}: {}".format(T, (V // P) * L + min(L, V % P)))

        T += 1