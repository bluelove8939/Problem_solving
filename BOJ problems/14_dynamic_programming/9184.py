cache = []

for i in range(21):
    cache.append([])
    for _ in range(21):
        cache[i].append([None for _ in range(21)])

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0: a, b, c = 0, 0, 0
    elif a > 20 or b > 20 or c > 20: a, b, c = 20, 20, 20

    if cache[a][b][c] is not None: return cache[a][b][c]

    if a == 0 and b == 0 and c == 0: ret = 1
    elif a < b and b < c: ret = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else: ret = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    cache[a][b][c] = ret

    return ret

if __name__ == "__main__":
    while True:
        a, b, c = map(int, input().split())
        if a == -1 and b == -1 and c == -1: break
        print(f"w({a}, {b}, {c}) = {w(a, b, c)}")