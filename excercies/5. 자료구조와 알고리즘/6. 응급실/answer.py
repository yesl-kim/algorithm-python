from collections import deque

# 0.00278 sec
def solution(n, m):
    a=deque([])
    c=1
    for i in range(len(n)):
        a.append((i, n[i]))
    while True:
        x=a.popleft()
        for y in a:
            if y[1]>x[1]:
                a.append(x)
                break
        else:
            if x[0]==m: return c
            else: c+=1

def solution2(n, m):
    c=0
    print(n)
    a=[(i, v) for i, v in enumerate(n)]
    a=deque(a)
    print('a: ', a)
    while True:
        x=a.popleft()
        if any(y[1]>x[1] for y in a):
            a.append
        else:
            c+=1
            if x[0]==m: return c
        

print(solution2([60, 60, 90, 60, 60, 60],0))