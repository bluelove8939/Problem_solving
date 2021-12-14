# 부분수열의 합 (Baekjoon Online Judge ID: 1182)
# 
# Url: https://www.acmicpc.net/problem/1182
# 
# 
# 알고리즘 분류: 동적계획법 (메모이제이션 적용하지 않음)


N = 0
seq = list()


def count_psum(cursor, target):
    if cursor == N:
        return 0
    
    cnt = 0

    if seq[cursor] == target:
        cnt += 1
    
    cnt += count_psum(cursor+1, target - seq[cursor]) + count_psum(cursor+1, target)

    return cnt


if __name__ == "__main__":
    N, S = map(int, input().split())
    seq = list(map(int, input().split()))

    print(count_psum(0, S))
