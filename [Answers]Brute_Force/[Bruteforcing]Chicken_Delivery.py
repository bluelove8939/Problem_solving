# 치킨 배달 (Baekjoon Online Judge ID: 15686)
# 
# Url: https://www.acmicpc.net/problem/15686
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


INF = 2000
dist = list()


def find_min_dist(cursor, left, limit, chicken):
    if cursor == limit:
        return sum(chicken)
    
    ret = INF

    if cursor < limit - left:
        ret = min(ret, find_min_dist(cursor+1, left, limit, chicken))
    
    if left > 0:
        new_chicken = list()

        for idx in range(len(chicken)):
            new_chicken.append(min(chicken[idx], dist[idx][cursor]))

        ret = min(ret, find_min_dist(cursor+1, left-1, limit, new_chicken))

    return ret
    

if __name__ == "__main__":
    N, M = map(int, input().split())
    city = [input().split() for _ in range(N)]
    house, store, dist = list(), list(), list()

    for r in range(N):
        for c in range(N):
            if city[r][c] == '1':
                house.append((r, c))
            if city[r][c] == '2':
                store.append((r, c))

    dist = [[abs(s[0] - h[0]) + abs(s[1] - h[1]) for s in store] for h in house]

    print(find_min_dist(0, M, len(store), [INF for _ in house]))
