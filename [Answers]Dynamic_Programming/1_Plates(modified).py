N, K, P = 0, 0, 0
beautySum = list()
cache = list()


def maxBeauty(cursor, left):
    if left == 0 or cursor == N:
        return 0;
    if cache[cursor][left] != 0:
        return cache[cursor][left]
    
    ret = 0;
    for idx in reversed(range(min(left+1, K+1))):
        ret = max(ret, beautySum[cursor][idx] + maxBeauty(cursor+1, left-idx))
    
    cache[cursor][left] = ret;

    return ret


if __name__ == "__main__":
    T = int(input())

    for t in range(1, T+1):
        N, K, P = map(int, input().split())
        beautySum = list()
        cache = [[0 for _ in range(1501)] for _ in range(51)]

        for _ in range(N):
            beautySum.append([0] + list(map(int, input().split())))
            for idx in range(1, K+1):
                beautySum[-1][idx] += beautySum[-1][idx-1]

        print("Case #{}: {}".format(t, maxBeauty(0, P)))