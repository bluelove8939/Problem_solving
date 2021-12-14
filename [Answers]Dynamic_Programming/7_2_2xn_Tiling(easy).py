# 2xn 타일링 (Baekjoon Online Judge ID: 11726)
# 
# Url: https://www.acmicpc.net/problem/11726
# 
# 
# 알고리즘 분류: 동적계획법과 메모이제이션
#   
# Hint
# 1. 이 문제는 7번 문제의 좀 더 쉬운 버전이다. 만약 7번 문제를 풀지 않았으면
#    7번 문제를 먼저 보는 것을 추천한다. 만약 7번 문제가 어렵다면 이 문제를 먼저
#    풀고, 그 다음에 7번 문제를 풀 것을 권장한다. 
# 2. 이 문제는 모든 경우의 수를 순회하며 풀어야 한다.
# 3. 데이터셋의 크기가 작지만 분기가 지수적으로 증가하는 경우 메모이제이션을
#    적용하는 것이 바람직하다. 
# 
#
# 풀이
# - 6번 문제와 매우 유사한 형태의 문제이다. 동적계획법과 메모이제이션을 활용하면
#   쉽게 풀 수 있다.
# 
# - 동적계획법을 사용함에 있어 가장 중요한 것은 점화식이 어떻게 나타나는지를 확인하는
#   것이다. 이 문제의 점화식이 어떤 형태로 나타나는지를 확인한 후 아래 식과 비교해보자.
#   이 문제의 점화식은 놀랍게도 피보나치 수열의 점화식과 정확하게 일치한다.
# 
#   아래 점화식에서 f(n)은 타일의 크기가 2xn일때 만들 수 있는 경우의 수를 구하는
#   부분문제이다. 이때 점화식은 다음과 같다: 
#   
#   f(n) = 1                  if n == 0 or n == 1 
#   f(n) = f(n-1) + f(n-1)    otherwise
# 
# - 메모이제이션을 적용하는 부분은 6번 문제와 동일하다. 다만 캐시 메모리의 크기가
#   (n+1)임에 주의하자. 
# 
# - 답의 크기가 매우 큰 경우, 이 문제처럼 정답을 어떤 숫자로 나눈 나머지를 요구하는
#   경우가 있다. 파이썬에서는 일반적으로 변수가 가질 수 있는 값의 제한이 없거나 굉장히
#   크므로 이것이 문제가 되는 경우가 잘 없지만, 하드웨어 친화적인 다른 언어들(이를테면
#   C나 C++과 같은 언어들)에서는 메모리 오버플로우(overflow)가 발생할 수 있다. 따라서
#   답을 구하는 중간중간에 미리 나머지 연산을 수행하여 값의 크기를 제한하는 것이
#   바람직한다. 아래 코드에서도 이런 방식을 적용했으니 참고할 것. 
# 
# - 아래 코드에서 solve() 함수의 내부 구조를 잘 확인한다. 모든 동적계획법 문제는 아래와
#   같은 코드 구조를 갖는다. 만약 어떤 문제를 풀 때 동적계획법을 사용하고자 한다면 아래와
#   같은 순서로 동일한 형태의 코드를 구현한다.
# 
#   1) 점화식을 세운다.
#   2) 해당 점화식을 의미하는 재귀 시퀀스에서의 탈출 조건을 확인힌다.
#   3) 함수를 구현한다. 이때 함수의 기본적인 구조는 아래 코드와 완전히 동일해야 한다.
#   4) 필요하다면 메모이제이션을 적용한다. 


from sys import setrecursionlimit

# 재귀의 깊이에 대한 제한을 없애주는 코드
setrecursionlimit(1000000)


MOD = 10007
cache = list()


def solve(siz):
    # 1. 탈출조건
    if siz in [0, 1]:
        return 1

    # 2. 캐시에 저장되어있는 값 확인
    if cache[siz] != -1:
        return cache[siz]
    
    # 3. 점화식을 이용한 값 계산
    ret = (solve(siz-1) + solve(siz-2)) % MOD

    # 4. 캐시에 값 저장
    cache[siz] = ret

    # 5. 계산한 값 리턴
    return ret


if __name__ == "__main__":
    n = int(input())

    # 캐시 초기화
    cache = [-1 for _ in range(n+1)]

    print(solve(n))