# Sticker (Baekjoon Online Judge ID: 9465)
# 
# Url: https://www.acmicpc.net/problem/9465
# 
# 
# 알고리즘 분류: 동적계획법과 메모이제이션
#   
# Hint
# 1. 이 문제는 모든 경우의 수를 순회하며 풀어야 한다.
# 2. 데이터셋의 크기가 매우 크므로 (N < 100000) 메모이제이션을 적용한다. 
# 
#
# 풀이
# - 기본적인 동적계획법 문제이나 바로 동적계획법이 떠오르지 않을 수 있다.
#   모든 경우의 수를 다 순회해야 하는 문제들의 경우 종종 동적계획법을
#   이용하여 쉽게 풀 수 있다.
# 
# - 문제에서 제시된 상황을 보다 간단하게 정리하면 다음과 같다:
#
#   1) 같은 열의 두 스티커는 선택할 수 없다.
#   2) 같은 행의 스티커를 연속으로 선택할 수 없다.
# 
#   위의 두 규칙에 유의하여 동적계획법을 위한 재귀함수를 작성한다.
#   아래 코드에서 find_max_comb() 함수가 이에 해당한다.
# 
# - find_max_comb(cursor, restraint)
#   주어진 스티커 배열에서 cursor번째 열부터 끝까지 잘라냈을 때 얻을 수 있는 
#   최대값을 계산한다. 이때 restraint는 cursor번째 열에서 선택해서는 안되는 행을
#   의미한다. (만약 restraint가 2이면 두 행을 다 선택할 수 있다고 가정하자)
#   예를 들어 find_max_comb(2, 0)의 경우 주어진 스티커 배열의 2번째 열부터 끝까지
#   잘라냈을 때, 2열 0행의 스티커를 선택하지 않으면서 얻을 수 있는 최대 값을 리턴한다.
# 
# - 해당 함수의 점화식은 다음과 같다 (S는 스티커 배열, N은 열의 개수이다):
#   f(c, r) = 0                                                         ... if c == N
#   f(c, r) = max(S[0][c] + f(c+1, 0), S[1][c] + f(c+1, 1), f(c+1, 2))  ... otherwise
# 
#   만약 함수의 형태가 바로 떠오르지 않는다면 점화식을 세워보는 것도 좋다.
#   위 점화식의 의미는 단순하다. 함수 내부의 분기는 크게 세가지로 분류된다:
# 
#   1) 현재 cursor에서 0번 행의 스티커를 선택했다
#      -> 다음 열에서는 0번 행의 스티커를 선택할 수 없다
#      -> S[0][c] + f(c+1, 0)
# 
#   2) 현재 cursor에서 1번 행의 스티커를 선택했다
#      -> 다음 열에서는 1번 행의 스티커를 선택할 수 없다
#      -> S[1][c] + f(c+1, 1)
# 
#   3) 현재 cursor에서 아무 스티커도 선택하지 않았다
#      -> 다음 열에서는 어떠한 스티커도 선택할 수 있다
#      -> f(c+1, 2)
#   
#   함수 내부적으로는 세가지의 분기 중 최대값을 리턴하면 된다.
#   (문제에서 요구하는 값이 최대값이기 때문)
# 
# - 점화식이 세워졌으면 재귀함수를 구성하는 것은 크게 어려운 일이 아니다.
# 
# - 이 문제는 데이터셋이 굉장히 크므로 메모이제이션을 적용하는 것이 좋다.
#   다행이도 위에서 구성한 재귀함수는 시간적으로 독립적이다. 시간적 독립성의
#   의미는 상대적으로 이전에 실행되는 부분문제가 이후에 실행되는 부분문제의 답에
#   영향을 미치지 않는다는 것이다.
# 
# - 예를 들어 아래 두 부분문제를 살펴보자.
#   
#   1) find_max_comb(3, 2)
#   2) find_max_comb(4, 1)
# 
#   위의 두 부분문제 중 2번 함수가 시간적으로 좀 더 나중에 발생하는 부분문제이다.
#   이때 2번 문제의 답은 1번 문제가 달라진다고 해서 달라지지 않는다.
#   (위에서 제시한 이 함수의 정의를 보면서 이해하면 쉽다)
# 
# - 만약 시간적으로 뒤에 일어나는 부분문제가 앞에서 실행된 모든 부분문제에 독립적이고,
#   이것이 무조건 보장된다면, 메모이제이션을 적용할 수 있다. 함수의 인수가 2개 이므로
#   캐시는 2차원이다.
# 
# - 메오이제이션을 적용하는 방법은 아주 간단하다. 원래 함수에 몇 줄의 코드만 추가하면
#   된다. 재귀함수의 탈출 조건 바로 아래에서 함수값을 계산하기 전에 캐시에 이 부분문제에
#   대한 답이 저장되어 있다면, 이 값을 바로 리턴한다. 만약 저장되어있지 않다면, 답을
#   계산하고 이를 캐시에 저장한다.
# 
# - 동적계획법과 메오이제이션을 사용하는 코드들은 거의 대부분 비슷한 구조를 갖늗다.
#   코드를 구조적으로 파악하는 것이 좋다. 
# 
# - 여담으로 아래 코드는 최적화할 수 있는 방법이 하나 있다.   


from sys import setrecursionlimit

# 재귀의 깊이에 대한 제한을 없애주는 코드
setrecursionlimit(1000000)


N = 0
sticker, cache = list(), list()


def find_max_comb(cursor, restraint):
    # 재귀 함수의 탈출 조건
    if cursor == N:
        return 0

    # 캐시에 해당 부분문제에 대한 답이 저장되어있는지를 확인한다
    if cache[cursor][restraint] != -1:
        return cache[cursor][restraint]

    # 해당 부분문제에 대한 답을 계산한다
    # 이때 재귀 함수의 분기가 일어난다 
    ret = 0

    #  분기 1: cursor번째 열에서 0번 행의 스티커를 선택한 경우
    #      -> 다음 열에서는 0번 행의 스티커를 선택할 수 없다 
    if restraint != 0:
        ret = max(ret, sticker[0][cursor] + find_max_comb(cursor + 1, 0))
    
    #  분기 2: cursor번째 열에서 1번 행의 스티커를 선택한 경우
    #      -> 다음 열에서는 1번 행의 스티커를 선택할 수 없다
    if restraint != 1:
        ret = max(ret, sticker[1][cursor] + find_max_comb(cursor + 1, 1))

    #  분기 2: cursor번째 열에서 아무 스티커도 선택하지 않은 경우
    #      -> 다음 열에서는 어떠한 스티커도 선택할 수 있다
    ret = max(ret, find_max_comb(cursor + 1, 2))

    # 부분문제의 답을 구했으니 이를 캐시에 저장한다
    cache[cursor][restraint] = ret

    # 부분문제의 답을 리턴한다
    return ret


if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        N = int(input())
        sticker = [list(map(int, input().split())) for _ in range(2)]

        # 재귀 함수를 사용하기 전 캐시를 초기화한다 -> 값이 저장되어있지 않다면 -1
        # 재귀 함수의 인수가 두 개이므로 캐시는 2차원
        cache = [[-1 for _ in range(3)] for _ in range(N)]

        print(find_max_comb(0, 2))