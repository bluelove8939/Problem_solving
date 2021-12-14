# 단어 수학 (Baekjoon Online Judge ID: 1339)
# 
# Url: https://www.acmicpc.net/problem/1339
# 
# 
# 알고리즘 분류: 그리디 알고리즘


if __name__ == "__main__":
    N, M = map(int, input().split())
    current = [[int(letter) for letter in input()] for _ in range(N)]
    target = [[int(letter) for letter in input()] for _ in range(N)]
    cnt = 0

    # 3*3필터에서 우측 상단의 요소만 바뀐다고 가정하고 필터를 적용한다
    # 필터를 적용할 때 마다 cnt를 1 증가시킨다 
    for row in range(1, N-1):
        for col in range(1, M-1):
            if current[row-1][col-1] != target[row-1][col-1]:
                cnt += 1
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        current[row+i][col+j] = 0 if current[row+i][col+j] == 1 else 1
    
    identical = True
    
    # 필터의 적용이 끝난 뒤 두 행렬이 같은 지를 확인
    for row in range(N):
        for col in range(M):
            if current[row][col] != target[row][col]:
                identical = False

    # 같으면 cnt, 아니면 -1 출력
    print(cnt if identical else -1)
