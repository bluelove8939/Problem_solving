# 가장 큰 증가 부분수열 (Baekjoon Online Judge ID: 11055)
# 
# Url: https://www.acmicpc.net/problem/11055
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
# - 증가하는 부분수열들 중 합이 가장 큰 부분수열의 합을 묻는 문제이다.
# 
# - 부분문제 f(n, s)를 다음과 같이 정의한다:
# 
#   f(n, s): s보다 큰 숫자로 시작하며, n번째 숫자부터 증가하는 부분수열의 합들 중
#            최대값을 구한다
#   
#   예를 들어 f(2, 4)는 두 번째 숫자(A[2])부터 증가하는 부분수열들의 합 중 최대값을
#   구하되, 수열이 4보다 큰 수로 시작되야한다.
# 
#   이 함수를 이용하여 점화식을 구성한다. 점화식은 다음과 같이 나타난다:
# 
#   f(n, s) = 0                                      if n == N
#   f(n, s) = f(n+1, s)                              if n != N and s >= A[n]
#   f(n, s) = max(A[n] + f(n+1, A[n]), f(n+1, s))    if n != N and s < A[n]
# 
# - 메모이제이션 또한 어렵지 않게 적용할 수 있다. 아래 코드에서 largest_sum(cursor, st)
#   함수의 인수가 두 개이므로 캐시는 2차원이다. 이때 st의 상한이 1000으로 문제에서
#   주어졌으므로 어렵지 않게 캐시를 구성할 수 있다.


from sys import setrecursionlimit

# 재귀의 깊이에 대한 제한을 없애주는 코드
setrecursionlimit(10000)


MAXIMUM = 1000
N = 0
A = list()
cache = list()


def largest_sum(cursor, st):
    # 탈출 조건
    if cursor == N:
        return 0
    
    # 캐시에 저장되어있는 값 확인
    if cache[cursor][st] != -1:
        return cache[cursor][st]

    # 점화식을 통해 값을 계산
    ret = 0

    if A[cursor] > st:
        ret = A[cursor] + largest_sum(cursor+1, A[cursor])
    
    ret = max(ret, largest_sum(cursor+1, st))

    # 캐시에 값 저장
    cache[cursor][st] = ret

    # 계산한 값 리턴
    return ret


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))

    # 캐시 초기화
    cache = [[-1 for _ in range(MAXIMUM+1)] for _ in range(N)]

    # 재귀 시퀀스를 이용하여 정답 계산
    print(largest_sum(0, 0))