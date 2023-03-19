def solution(s):
    n, k=map(int, s.split(' '))
    a=[i for i in range(1, int(n)+1) if n%i == 0]
    return a[int(k) -1]

print(solution(input()))
# print(input())
