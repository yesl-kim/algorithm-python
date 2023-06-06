from collections import deque

# 0.01094 sec
# def solution(n, k):
#     a=list(range(1, n+1))
#     q=[]
#     c=0
#     i=0
#     while len(q)<n-1:
#        idx=i%n
#        if a[idx]==None: 
#           i+=1
#        else:    
#             if c%k==k-1:
#                 q.append(a[idx])
#                 a[idx]=None
#                 i+=1
#                 c=0
#             else: 
#                 c+=1
#                 i+=1
#     for x in a:
#        if x!=None: return x
        


def solution(n,k):
    a=deque(list(range(1, n+1)))
    c=1
    while(len(a)>1):
      if c%k==0:
        a.popleft()
        c=1
      else:
        a.append(a.popleft())
        c+=1
    return a[0]

print(solution(8,3))