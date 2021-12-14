# 이항 계수 2 (Baekjoon Online Judge ID: 11051)
# 
# Url: https://www.acmicpc.net/problem/11051
# 
# 
# 알고리즘 분류: 동적계획법과 메모이제이션
#   
# Hint
# 1. 이 문제는 모든 경우의 수를 순회하며 풀어야 한다.
# 2. 메모이제이션을 적용한다. 
# 
#
# 풀이
# - 이항 계수는 동적계획법을 이용하여 구할 수 있는 대표적인 함수이다.
# 
# - 이항 계수의 점화식은 다음과 같다:
#   
#   f(n, k) = 1                           if k == 0 or n == k
#   f(n, k) = f(n-1, k-1) + f(n-1, k)     otherwise
# 
# - 재귀 시퀀스의 인수가 2개이므로 캐시는 2차원이다. 


from sys import setrecursionlimit

# 재귀의 깊이에 대한 제한을 없애주는 코드
setrecursionlimit(1000000)


MOD = 10007
cache = list()


def bin_coef(n, k):
    # 탈출 조건
    if k == 0 or n == k:
        return 1

    # 캐시에 저장된 값 확인
    if cache[n][k] != -1:
        return cache[n][k]

    # 점화식을 이용하여 값 계산
    ret = (bin_coef(n-1, k-1) + bin_coef(n-1, k)) % MOD

    # 캐시에 계산한 값 저장
    cache[n][k] = ret

    # 계산한 값 리턴
    return ret


if __name__ == "__main__":
    N, K = map(int, input().split())

    # 캐시 초기화
    cache = [[-1 for _ in range(K+1)] for _ in range(N+1)]

    print(bin_coef(N, K))
    