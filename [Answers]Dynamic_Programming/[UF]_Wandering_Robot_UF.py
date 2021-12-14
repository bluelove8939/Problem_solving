W, H, L, U, R, D = 0, 0, 0, 0, 0, 0

def combination(n, r):
    ret = 1

    for i in range(n, n-r, -1):
        ret *= i
    
    for i in range(1, r+1):
        ret /= i
        
    return ret

if __name__ == "__main__":
    T = int(input())

    for t in range(1, T+1):
        W, H, L, U, R, D = map(int, input().split())
        probability = 0

        if (W == 1 or H == 1):
            probability = 1.0
        else:
            # rows
            if U != 1:
                for dx in range(L, R+1):
                    n = U + dx - 3
                    r = dx - 1
                    comb = combination(n, r)
                    probability += ((0.5) ** (n+1)) * comb

            # columns
            if L != 1:
                for dy in range(U, D+1):
                    n = L + dy - 3
                    r = L - 1
                    comb = combination(n, r)
                    probability += ((0.5) ** (n+1)) * comb

        print("Case #{}: {}".format(t, 1 - probability))