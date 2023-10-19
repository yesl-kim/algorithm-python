# https://school.programmers.co.kr/learn/courses/30/lessons/84512?language=python3

from itertools import product
from bisect import bisect_right

words = sorted(("".join(comb) for i in range(1,6) for comb in product('AEIOU', repeat=i)))

def solution(word):
    return bisect_right(words, word)
        