# 안전영역 (Baekjoon Online Judge ID: 1759)
# 
# Url: https://www.acmicpc.net/problem/1759
# 
#
# 알고리즘 분류: 브루트포스
#   
# Hint
# 1. 이 문제는 브루트포스 문제이다.
# 
#
# 풀이
# - 브루트포스


L, C = 0, 0
VOWELS = "aeiou"
characters = list()
wordlist = list()


def find_every_words(cursor, left, word):
    if cursor == C:
        cnt_vowel, cnt_consonant = 0, 0
        for letter in word:
            if letter in VOWELS:
                cnt_vowel += 1
            else:
                cnt_consonant += 1
        
        if cnt_vowel >= 1 and cnt_consonant >= 2:
            wordlist.append(word)
        
        return

    if cursor < C - left:
        find_every_words(cursor+1, left, word)
    if left > 0:
        find_every_words(cursor+1, left-1, word + characters[cursor])
    

if __name__ == "__main__":
    L, C = map(int, input().split())
    characters = sorted(input().split())
    wordlist = list()

    find_every_words(0, L, "")

    for word in sorted(wordlist):
        print(word)
