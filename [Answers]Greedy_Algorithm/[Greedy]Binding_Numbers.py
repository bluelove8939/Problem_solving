# 수 묶기 (Baekjoon Online Judge ID: 1744)
# 
# Url: https://www.acmicpc.net/problem/1744
# 
# 
# 알고리즘 분류: 그리디 알고리즘


from sys import stdin


if __name__ == "__main__":
    N = int(input())
    pos, neg = list(), list()
    res = 0

    # 양수와 음수를 따로 입력받는다
    # 이때 0은 음수로 취급 
    for _ in range(N):
        num = int(stdin.readline())
        if num > 0:
            pos.append(num)
        else:
            neg.append(num)
    
    # 양수는 내립차순으로 정렬
    pos.sort(reverse=True)

    # 음수는 오름차순으로 정렬
    neg.sort(reverse=False)

    # 양수 배열에서 큰 수를 기준으로 두 개씩 묶어 더한다
    # 이때 묶으려는 수들 중 1이 있으면 묶으면 안된다 
    for idx in range(1, len(pos), 2):
        if pos[idx-1] == 1 or pos[idx] == 1:
            res += pos[idx-1] + pos[idx]
        else:
            res += pos[idx-1] * pos[idx]
    
    # 만약 하나가 남으면 그냥 더한다
    if len(pos) % 2 == 1:
        res += pos[-1]
    
    # 음수 배열에서 작은 수를 기준으로 두 개씩 묶어 더한다
    for idx in range(1, len(neg), 2):
        res += neg[idx-1] * neg[idx]
    
    # 만약 하나가 남으면 그냥 더하는 수 밖에 없다
    if len(neg) % 2 == 1:
        res += neg[-1]
    
    print(res)
