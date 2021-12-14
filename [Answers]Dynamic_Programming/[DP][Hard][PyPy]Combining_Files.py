# 파일 합치기 (Baekjoon Online Judge ID: 11066)
# 
# Url: https://www.acmicpc.net/problem/11066
# 
# 
# 알고리즘 분류: 동적계획법 (메모이제이션 적용하지 않음)


INF = 50000000
K = 0
psum = list()
cache = list()
psum = list()


def min_cost(left, right):
    if right - left == 1:
        return 0

    if right - left == 2:
        return psum[right] - psum[left]
    
    if cache[left][right] != -1:
        return cache[left][right]

    cost = INF

    for center in range(left + 1, right):
        cost = min(cost, psum[right] - psum[left] + min_cost(left, center) + min_cost(center, right))
    
    cache[left][right] = cost

    return cost
            

if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        K = int(input())
        psum = [0] + list(map(int, input().split()))
        cache = [[-1 for _ in range(K+1)] for _ in range(K+1)]

        for idx in range(K):
            psum[idx+1] += psum[idx]

        print(min_cost(0, K))
