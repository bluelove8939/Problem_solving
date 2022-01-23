def isprime(num):
    if num == 0 or num == 1:
        return False

    i = 2
    while i*i <= num:
        if num % i == 0: return False
        i += 1

    return True


def solution(n, k):
    answer, tmp, multiplier = 0, 0, 1

    while n != 0:
        remainder = n % k
        n = n // k
        if remainder != 0:
            tmp += remainder * multiplier
            multiplier *= 10
        else:
            if isprime(tmp):
                answer += 1
            tmp, multiplier = 0, 1

    if isprime(tmp):
        answer += 1

    return answer


# if __name__ == '__main__':
#     print(solution(437674, 3))
