# 단어 수학 (Baekjoon Online Judge ID: 1339)
# 
# Url: https://www.acmicpc.net/problem/1339
# 
# 
# 알고리즘 분류: 그리디 알고리즘
#   
# Hint
# 1. 이 문제는 그리디 알고리즘을 이용하여 풀 수 있다.
# 
#
# 풀이
# - None


if __name__ == "__main__":
    N = int(input())
    words = [input() for _ in range(N)]
    factor = [0 for _ in range(26)]
    res = 0

    # 각 알파벳에 대한 인수를 계산한다
    # 예를 들어 word = ABC이면 A의 인수는 100, B의 인수는 10, C의 인수는 1이다
    # 이 작업을 모든 단어에 대해 실행하고 각 인수들을 더해 최종적인 함수를 만든다
    # 
    # 참고: ord()는 해당 문자의 아스키코드 값을 리턴한다 
    for word in words:
        for idx, letter in enumerate(reversed(word)):
            factor[ord(letter) - ord('A')] += 10 ** (idx)
    
    # 인수의 크기를 기준으로 내림차순 정렬을 한다
    factor.sort(reverse=True)

    # 상위 10개의 요소에 숫자들을 할당하고 최종 답을 계산한다
    for idx, digit in enumerate(reversed(range(10))):
        res += factor[idx] * digit
    
    print(res)