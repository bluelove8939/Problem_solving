# 제곱수의 합 (Baekjoon Online Judge ID: 1699)
# 
# Url: https://www.acmicpc.net/problem/1699
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
# - 동적계획법의 핵심은 점화식이다. 이 문제를 풀기 위한 재귀 시퀀스의
#   점화식은 다음과 같이 나타난다. f(n)은 n을 제곱수의 합으로 표현할 때
#   최소 항의 개수를 의미한다.
# 
#   f(n) = 1                                                                  if n == 1
#   f(n) = 임의의 정수 i에 대해 (n // (i ** 2)) + f(n % (i ** 2))중 최소값      otherwise
# 
# - 함수의 인수가 1개이므로 캐시는 1차원이다. 


from sys import setrecursionlimit

# 재귀의 깊이에 대한 제한을 없애주는 코드
setrecursionlimit(1000000)


cache = list()


def solve(num):
    # 탈출 조건
    if num == 1:
        return 1
    
    # 캐시에 저장된 값 확인
    if cache[num] != -1:
        return cache[num]

    # 점화식을 이용하여 값 계산
    ret, factor = num, 1

    while factor ** 2 <= num:
        ret = min(ret, num // (factor ** 2) + solve(num % (factor ** 2)))
        factor += 1 

    # 캐시에 계산한 값 저장
    cache[num] = ret

    # 계산한 값 리턴
    return ret


if __name__ == "__main__":
    N = int(input())

    # 캐시 초기화
    cache = [-1 for _ in range(N+1)]

    print(solve(N))