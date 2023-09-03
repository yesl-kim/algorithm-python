from itertools import product
from functools import reduce
import math

def check(x, y, k, d):
    return (x*k)**2 + (y*k)**2 <= (d) ** 2

def count(x, k, d):
    l, r = 0, d + 1
    while l < r:
        mid = (l + r - 1) // 2
        if check(x, mid, k, d):
            l = mid + 1
        else:
            r = mid
    return r

def solution(k, d):
    cnt = 0
    for a, b in product(range(d + 1), repeat=2):
        print(a, b, '=', (a + b) * k, end=' ')
        if (a*k)**2 + (b*k)**2 <= (d) ** 2:
            cnt += 1
            print('✔️', cnt)
        else:
            print()
        
    return cnt

# k=1
# d=5
k=2
d=4
# print(solution(k, d))
print(count(3, k, d))