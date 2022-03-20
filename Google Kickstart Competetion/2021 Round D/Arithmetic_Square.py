if __name__ == "__main__":
    T = int(input())

    for t in range(1, T+1):
        table = [list(map(int, input().split())) for _ in range(3)]
        res, cnt, center = 0, 0, 0

        if (table[0][0] + table[2][0]) / 2 == table[1][0]:
            res += 1
        
        if (table[0][0] + table[0][2]) / 2 == table[0][1]:
            res += 1
        
        if (table[2][0] + table[2][2]) / 2 == table[2][1]:
            res += 1

        if (table[0][2] + table[2][2]) / 2 == table[1][1]:
            res += 1

        value = []
        if (table[1][0] + table[1][1]) % 2 == 0:
            value.append((table[1][0] + table[1][1]) / 2)
        if (table[0][1] + table[2][1]) % 2 == 0:
            value.append((table[0][1] + table[2][1]) / 2)
        if (table[0][0] + table[2][2]) % 2 == 0:
            value.append((table[0][0] + table[2][2]) / 2)
        if (table[0][2] + table[2][0]) % 2 == 0:
            value.append((table[0][2] + table[2][0]) / 2)

        cnt = [value.count(val) for val in value]
        
        print(f"Case #{t}: {res + max(cnt)}")