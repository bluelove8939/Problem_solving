# 카드 정렬하기 (Baekjoon Online Judge ID: 11726)
# 
# Url: https://www.acmicpc.net/problem/11726
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


from sys import stdin
from queue import PriorityQueue


if __name__ == "__main__":
    N = int(input())
    cards = PriorityQueue()
    compare = 0
    
    # 우선순위 큐에 카드 뭉치들을 다 넣어놓는다
    for _ in range(N):
        cards.put(int(stdin.readline()))

    # 우선순위 큐에서 카드뭉치들을 빼면서 하나씩 계산한다
    for _ in range(N-1):
        pile = cards.get() + cards.get()
        compare += pile
        cards.put(pile)

    print(compare)