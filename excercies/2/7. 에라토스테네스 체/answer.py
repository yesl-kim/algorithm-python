'''
자연수 n
1~n 까지의 소수의 개수
'''
def isPrime(n):
    if n < 2: return False
    for x in range(2, n):
        if n%x == 0:
            return False
    else: return True

def solution(m):
    a=[x for x in range(1, m+1) if isPrime(x)]
    # print(a)
    # print(len(a))
    return len(a)
    

# solution(20)
