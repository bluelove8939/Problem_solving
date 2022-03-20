def solve(value):
    if int(value) < 9:
        return 9 - int(value)
    elif int(value) == 9:
        return 0

    digitSum = str(sum(list(map(int, list(value)))))
    return solve(digitSum)


if __name__ == '__main__':
    T = int(input())

    for casenum in range(1, T+1):
        N = input()
        rem = solve(N)
        pos = 0
        res = list(N)

        for digit in N:
            if rem != 0:
                if int(digit) <= rem:
                    pos += 1
                else:
                    break
            else:
                pos = 1

        res.insert(pos, str(rem))
        res = ''.join(res)
        print(f'Case #{casenum}: {res}')