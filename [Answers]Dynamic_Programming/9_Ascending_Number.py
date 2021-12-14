# 오르막 수 (Baekjoon Online Judge ID: 11057)
# 
# Url: https://www.acmicpc.net/problem/11057
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
# - 동적계획법을 이용하기 위해서는 점화식을 세워야 한다.
# 
# - 이 문제에서 오르막 수는 모든 자릿수가 오름차순으로 정렬되어있는 수를 의미한다.
#   N이 1일 때 N자리 오르막 수의 개수는 1일 것이다. 문제에서 수가 0으로 시작할 수
#   있다고 했으므로 N이 1인 경우를 제외한 N자리 오르막 수의 개수는 다음과 같이 정의된다:
# 
#   (N자리 오르막 수의 개수) = (0으로 시작하는 N-1자리의 오르막 수의 개수)
#                            + (1로 시작하는 N-1자리의 오르막 수의 개수)
#                            + (2로 시작하는 N-1자리의 오르막 수의 개수)
#                            + ... 
#                            + (9로 시작하는 N-1자리의 오르막 수의 개수)
# 
#   위의 점화식을 살짝만 변형하면 K로 시작하는 오르막 수의 개수를 나타내는 점화식을
#   유도할 수 있다. 
# 
# - 따라서 위 점화식을 위한 재귀 시퀀스는 총 두 개의 인수를 갖는다.
#   1) 수의 길이(siz)   2) 시작하는 숫자(st)
# 
# - 앞서 풀어본 동적계획법 문제들의 답안 코드와 동일한 형태로 함수를 구성한다.
#   첨언하자면 재귀 시퀀스의 인수가 2개 이므로, 캐시는 2차원이다. 


from sys import setrecursionlimit

# 재귀의 깊이에 대한 제한을 없애주는 코드
setrecursionlimit(10000)


MOD = 10007
cache = list()


def ascending_nums(siz, st):
    # 1. 탈출 조건
    if siz == 1:
        return 1
    
    # 2. 캐시에 저장되어있는 값 확인
    if cache[siz][st] != -1:
        return cache[siz][st]

    # 3. 점화식을 이용한 값 계산
    ret = 0
    
    for nxt_st in range(st, 10):
        ret += ascending_nums(siz-1, nxt_st)
    
    ret %= MOD
    
    # 4. 캐시에 값 저장
    cache[siz][st] = ret

    # 5. 계산한 값 리턴
    return ret


if __name__ == "__main__":
    N = int(input())

    # 캐시 초기화
    cache = [[-1 for _ in range(10)] for _ in range(N+1)]

    # 구현한 함수를 이용하여 정답 계산
    cnt = 0

    for st in range(10):
        cnt += ascending_nums(N, st)
    
    cnt %= MOD
    
    # 출력
    print(cnt)