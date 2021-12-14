# 2048(easy) (Baekjoon Online Judge ID: 12100)
# 
# Url: https://www.acmicpc.net/problem/12100
#
#   
# Hint
# 1. 때로는 무식하게 짜는 것도 한 방법이다
# 
#
# 풀이
# - 문제에 제시된 상황을 그대로 구현하는 것을 브루트 포스(Brute Force)라 한다.
# 
# - 이 문제는 크게 두 가지의 문제로 나눌 수 있다:
#   1) 2048게임을 구현하는 것
#   2) 5번 이동했을 때 최대값을 찾는 것
# 
# - 2048 게임의 규칙은 문제를 참고한다. 이동할 수 있는 방향이 위, 아래, 좌, 우의 
#   4가지 이므로 현재 상태에서 각 방향으로 이동했을 때, 결과를 계산하는 함수가
#   총 4개 필요하다.
# 
# - 그러나 함수를 4개 만드는 것은 까다롭고 코드를 복잡하게 만드므로 좀 더 간단하게
#   코드를 짜기 위해 함수는 위로 이동했을 때 결과를 리턴하는 함수 하나만 작성하는
#   것으로 한다. 이 함수 만으로도 모든 방향으로 이동했을 때의 결과를 도출할 수 있다.
# 
# - 아래로 이동: 현재 상태를 상하 반전한 후 위로 이동 
#               -> 결과도 상하 반전된 상태
#   우측으로 이동: 상하 반전된 상태에서 전치(transpose)한 후 위로 이동
#                 -> 결과도 전치 후 상하 반전된 상태
#   좌측으로 이동: 현재 상태를 전치한 후 위로 이동
#                 -> 결과도 전치된 상태
# 
# - 테이블의 상하 반전은 reversed() 내장메소드를 이용하면 쉽게 구현할 수 있다.
# 
# - 테이블의 전치(transpose)는 파이썬에서 제공되는 list comprehension을 이용하면
#   쉽게 구현할 수 있다.
# 
# - 상하 반전 혹은 전치를 하지 않고 각 방향으로 이동하는 경우를 전부 함수로 구현해도
#   알고리즘 상 문제는 없다. 시간은 오히려 감소할 수도 있다. 
# 
# - 다음으로는 각 상태에서 어디로 이동했을 때 최대값이 나오는지를 확인하는 알고리즘이
#   필요하다.
# 
# - 알고리즘 개요:
#   1) 먼저 각 방향으로 이동했을 때 다음 상태를 정의한다. 앞서 소개한 대로 하면 된다.
#   2) 어느 방향으로 이동했을 때 최대값을 얻을 수 있는지를 확인한다.
#   3) 반복횟수가 5가 될 때 까지 반복한다.
#   4) 반복횟수가 5가 되면 최대값을 계산한 후 리턴한다. 
# 
# - 위와 같이 모든 상태공간을 순회하는 알고리즘을 그래프의 완전탐색 알고리즘이라 한다.
#   다만, 이 문제는 완전탐색 문제의 일반적인 형태는 아니므로 여기서는 다루지 않는다.


def move_upward(table, siz):  # 위로 이동했을 때 결과를 리턴하는 함수
    # 리턴하고자 하는 리스트를 정의한다
    moved = [[0 for _ in range(siz)] for _ in range(siz)]
    
    # 이동을 구현한 부분
    # 사람마다 구현하는 방식이 다르니 참고만 할 것 (인터넷 검색 ㄱㄱ) 
    for col in range(siz):
        cursor = 0
        for row in range(siz):
            if table[row][col] != 0:
                if moved[cursor][col] == 0:
                    moved[cursor][col] = table[row][col]
                elif moved[cursor][col] == table[row][col]:
                    moved[cursor][col] *= 2
                    cursor += 1
                else:
                    cursor += 1
                    moved[cursor][col] = table[row][col]

    return moved


def find_max_num(table, siz, iter):
    ret = 0
    
    # 반복 횟수가 다한 경우 -> 최대값을 계산한다
    if iter == 0:
        for line in table:
            for num in line:
                ret = max(ret, num)
        return ret
    
    # 위로 이동한 경우의 최대값을 계산하는 부분
    # 최대값은 재귀적으로 계산된다 
    moved = move_upward(table, siz)
    ret = max(ret, find_max_num(moved, siz, iter-1))
    
    # 아래로 이동한 경우의 최대값을 계산하는 부분
    # 현재 상태를 상하 반전한 후 위로 이동한다 
    table = list(reversed(table))  # 상하 반전
    moved = list(reversed(move_upward(table, siz)))  # 결과 역연산
    ret = max(ret, find_max_num(moved, siz, iter-1))
    
    # 우측으로 이동한 경우의 최대값을 계산하는 부분
    # 현재 상태를 상하 반전한 것을 전치(transpose)한 후 위로 이동한다
    # 위에서 이미 현재 상태가 상하 반전 되어있음에 유의한다
    table = [[table[j][i] for j in range(siz)] for i in range(siz)]  # 전치
    moved = list(reversed(move_upward(table, siz)))                  # 결과 역연산
    moved = [[moved[j][i] for j in range(siz)] for i in range(siz)]  # 결과 역연산
    ret = max(ret, find_max_num(moved, siz, iter-1))

    # 죄측으로 이동한 경우의 최대값을 계산하는 부분
    # 현재 상태를 전치한 후 위로 이동한다
    # 위에서 현재 상태가 상하 반전된 후 전치되어 있음에 유의한다
    # 상하 반전 연산과 전치는 교환법칙이 성립하고 상하 반전의 역연산은 상하 반전 이므로
    # 위에서 사용한 현재 상태에 상하 반전만 다시 한 번 적용하면 된다
    table = list(reversed(table))  # 상하 반전(현재 transpose 된 상태이므로 좌우가 반전됨)
    moved = move_upward(table, siz)
    moved = [[moved[j][i] for j in range(siz)] for i in range(siz)]  # 결과 역연산
    ret = max(ret, find_max_num(moved, siz, iter-1))

    # 참고:
    # 코드를 보면 이동한 결과에 역연산을 진행하는 것을 볼 수 있다
    # 그러나 알고리즘적으로 보면 굳이 역연산을 수행할 필요는 없다
    # 그 이유는 무엇일까?

    return ret


if __name__ == "__main__":
    N = int(input())

    # 입력을 받는 부분
    # list comprehension으로 간편하게 테이블 형태의 입력을 받을 수 있다
    table = [list(map(int, input().split())) for _ in range(N)]

    print(find_max_num(table, N, 5))
    