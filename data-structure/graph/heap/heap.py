# heap: number[]
# data: number
import heapq

# 노드 추가
def heappush(heap, data):
    heap.append(data)
    current=len(heap)-1
    while current>0:
        parent=(current-1)//2
        if heap[parent]>heap[current]:
            heap[parent], heap[current]=heap[current], heap[parent]
            current=parent
        else:
            break
        

# 루트 노드 제거
def heappop(heap):
    if not heap: return "Empty Heap!"
    elif len(heap)==1: return heap.pop()
    
    root,heap[0]=heap[0],heap.pop()
    cur,lt=0,1
    while lt<len(heap):
        child,rt=lt,lt+1
        # 자식 요소 중 더 작은 값과 값교환을 하면 됨
        if rt<len(heap) and heap[lt]>heap[rt]:
            child=rt
        if heap[cur]>heap[child]:
            heap[child],heap[cur]=heap[cur],heap[child]
            cur,lt=child,child*2+1
        else: 
            break
    return root

import heapq
h = []
arr = [21, 33, 17, 27, 9, 11, 14]
for i in arr:
        heappush(h, i)

print(h)
while h:
        print(heappop(h), end = " ")

print()
print(heappop(h))