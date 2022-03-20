if __name__ == '__main__':
    T = int(input())

    for casenum in range(1, T+1):
        I = input()
        P = input()
        res = 0
        idx = 0

        for letter in P:
            if idx < len(I):
                if I[idx] == letter:
                    idx += 1
                else:
                    res += 1
            elif idx == len(I):
                res += 1

        if idx != len(I):
            res = 'IMPOSSIBLE'

        print(f'Case #{casenum}: {res}')