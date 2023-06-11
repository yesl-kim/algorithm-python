import heapq
    
def solution2(s,k):
    ht={}
    for x in s:
        ht[x]=ht.get(x,0)+1
    h=[]
    for v in ht.values():
        heapq.heappush(h, -v)
    for _ in range(k):
        heapq.heappush(h, heapq.heappop(h)+1)
    sum=0
    for x in h:
        sum+=(x*x)
    return sum
    

print(solution2('aabcbcbcabcc',3))