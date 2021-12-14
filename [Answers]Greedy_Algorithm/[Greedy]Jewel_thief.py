# 보석 도둑 (Baekjoon Online Judge ID: 1202)
# 
# Url: https://www.acmicpc.net/problem/1202
# 
# 
# 알고리즘 분류: 그리디 알고리즘
#   
# Hint
# 1. 이 문제는 그리디 알고리즘을 이용하여 풀 수 있다.


from sys import stdin
from queue import PriorityQueue as pqueue


if __name__ == "__main__":
    # 입력 받기
    N, K = map(int, input().split())
    jewel = [list(map(int, stdin.readline().split())) for _ in range(N)]
    baggage = [int(stdin.readline()) for _ in range(K)]

    # 특정 가방에 넣을 후보들을 넣어놓기 위한 우선순위 큐
    candidate = pqueue()
    value, idx = 0, 0

    # 보석은 무게에 대해 오름차순으로 정렬하고
    # 가방은 무게의 상한선에 따라 오름차순 정렬한다 
    jewel.sort(key=lambda x: x[0])
    baggage.sort()

    # 편의를 위해 추가한 더미데이터
    jewel.append([100000001, 0])

    # 그리디 알고리즘을 이용한 보석 할당
    for bag in baggage:
        while jewel[idx][0] <= bag:
            candidate.put(-1 * jewel[idx][1])
            idx += 1

        if not candidate.empty():
            value -= candidate.get()
    
    print(value)