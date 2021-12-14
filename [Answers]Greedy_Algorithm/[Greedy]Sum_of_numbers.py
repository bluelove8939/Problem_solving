# 수들의 합 (Baekjoon Online Judge ID: 1789)
# 
# Url: https://www.acmicpc.net/problem/1789
# 
# 
# 알고리즘 분류: 그리디 알고리즘
#   
# Hint
# 1. 이 문제는 그리디 알고리즘을 이용하여 풀 수 있다.
# 
#
# 풀이
# - None


if __name__ == "__main__":
    S = int(input())
    num, psum = 0, 0

    while psum <= S:
        num += 1
        psum += num

    print(num-1)
