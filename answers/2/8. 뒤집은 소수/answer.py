'''
뒤집은 소수

N개의 자연수 n
각 자연수를 뒤집은 수가 소수면 그 순서대로 출력
'''
def reverse(s):
    ss=''
    for x in s:
        ss = x+ss
    return ss

def isPrime(n):
    if n<2: return False
    for i in range(2, n):
        if n%i == 0: return False
    else: return True

def solution(n):
    n=list(map(int, list(map(reverse, n.split()))))
    a=[x for x in n if isPrime(x)]
    a=list(map(str, a))
    return " ".join(a)

# print(solution('32 55 62 3700 250'))