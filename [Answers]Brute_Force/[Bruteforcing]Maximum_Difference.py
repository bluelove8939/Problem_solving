# 차이를 최대로 (Baekjoon Online Judge ID: 10819)
# 
# Url: https://www.acmicpc.net/problem/10819
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


N = 0
seq = list()


def find_max_sum(priv, selected):
    if False not in selected:
        return 0

    res = 0
    
    for idx, num in enumerate(seq):
        if not selected[idx]:
            new_selected = selected[:]
            new_selected[idx] = True
            res = max(res, abs(priv - num) + find_max_sum(num, new_selected))
    
    return res


if __name__ == "__main__":
    N = int(input())
    seq = sorted(list(map(int, input().split())))
    
    res = 0

    for idx, num in enumerate(seq):
        selected = [False for _ in seq]
        selected[idx] = True
        res = max(res, find_max_sum(num, selected))
    
    print(res)
