# 저울 (Baekjoon Online Judge ID: 2437)
# 
# Url: https://www.acmicpc.net/problem/2437
# 
# 
# 알고리즘 분류: 그리디 알고리즘


if __name__ == "__main__":
    N = int(input())
    weights = list(map(int, input().split()))

    # 무게추를 오름차순으로 정렬한다
    weights.sort()
    num = 0

    # n개의 무게추로 만들 수 있는 무게의 상한을 계산한다
    # 만약 n+1번째 무게추가 (앞서 구한 상한) + 1보다 크면 중간에 비는 숫자가 생김  
    for w in weights:
        if w > num + 1:
            break
        else:
            num += w

    print(num + 1)
