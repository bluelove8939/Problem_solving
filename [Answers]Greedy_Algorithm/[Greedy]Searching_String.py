# 문서 검색 (Baekjoon Online Judge ID: 1543)
# 
# Url: https://www.acmicpc.net/problem/1543
# 
# 
# 알고리즘 분류: 그리디 알고리즘
#   
# Hint
# 1. 이 문제는 그리디 알고리즘을 이용하여 풀 수 있다.


from sys import stdin


if __name__ == "__main__":
    data = input()
    target = input()
    idx, cnt = 0, 0

    while idx < 1 + len(data) - len(target):
        if data[idx : idx+len(target)] == target:
            cnt += 1
            idx += len(target)
        else:
            idx += 1

    print(cnt)