# 멀티탭 스케쥴링 (Baekjoon Online Judge ID: 1700)
# 
# Url: https://www.acmicpc.net/problem/1700
# 
# 
# 알고리즘 분류: 그리디 알고리즘


if __name__ == "__main__":
    N, K = map(int, input().split())
    order = list(map(int, input().split()))
    current = set()
    cnt = 0

    for idx, item in enumerate(order):
        if item not in current:
            if len(current) == N:
                popidx, popitem = -1, 0
                
                for cur in current:
                    if cur in order[idx:]:
                        if popidx < order[idx:].index(cur):
                            popidx = order[idx:].index(cur)
                            popitem = cur
                    else:
                        popitem = cur
                        break

                current.remove(popitem)
                cnt += 1

            current.add(item)
            
    print(cnt)
