# 리모컨 (Baekjoon Online Judge ID: 1107)
# 
# Url: https://www.acmicpc.net/problem/1107
# 
#
# 알고리즘 분류: 브루트포스
#   
# Hint
# 1. 이 문제는 브루트포스 문제이다.
# 
#
# 풀이
# - 브루트포스


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    
    if M == 0:
        res = len(str(N))
    else:
        restraint = list(map(int, input().split()))

        # when it comes to press - button
        cnt = 0

        for idx, digit in enumerate(list(map(int, str(N)))):
            if digit in restraint:
                for target in reversed(range(0, digit)):
                    if target not in restraint:
                        cnt += N % (10 ** (len(str(N)) - idx))
                        break
                
                for d in range(0, 10):
                    if d not in restraint:
                        for factor in range(0, len(str(N)) - idx - 1):
                            cnt += d * (10 ** factor)

        # when it comes to press any button, starting from 100
        res = min(res, N - 100)
    
    print(res)
