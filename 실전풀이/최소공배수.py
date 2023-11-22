from collections import Counter, defaultdict
from functools import reduce

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def prime_factorize(n):
    if n == 1:
        return Counter({1: 1})

    if isPrime(n):
        return Counter({n: 1})

    for i in filter(isPrime, range(n)):
        share, rest = divmod(n, i)
        if not rest:
            return Counter({i: 1}) + prime_factorize(share)

def fact_to_num(counters):
    res = 1
    for root, m in counters.items():
        res *= (root ** m)
    return res


def solution(arr):
    facts = reduce(lambda acc, cur: acc + (cur - acc), 
                   map(prime_factorize, arr))
    return fact_to_num(facts)