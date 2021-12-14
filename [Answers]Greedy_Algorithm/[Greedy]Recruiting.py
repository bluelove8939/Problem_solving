# 신입사원 (Baekjoon Online Judge ID: 1946)
# 
# Url: https://www.acmicpc.net/problem/1946
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


if __name__ == "__main__":
    T = int(stdin.readline())

    for _ in range(T):
        N = int(stdin.readline())
        scores = list()
        applicant = list()
        cache = [0 for _ in range(N)]
        cnt, minimum = 0, N+1

        for idx in range(N):
            scores.append(list(map(int, stdin.readline().split())))
        
        # 서류 순위에 대해 오름차순으로 정렬
        scores.sort(key=lambda x: x[0])
        applicant.append([s[0] for s in scores])

        # 하나씩 순회하면서 면접 순위가 내림차순이면 카운트
        # 아니면 카운트 하지 않는다  
        for i in range(N):
            if scores[i][1] < minimum:
                cnt += 1
                minimum = scores[i][1]

        print(cnt)