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

# 주어진 배열이나 이진트리를 힙 구조로 "재배열"
def heapify(arr):
    for i in range(len(arr)):
        cur=len(arr)-1
        while (cur-1)//2>=i:
            if cur%2==0 and arr[cur]>arr[cur-1]: cur-=1
            parent=(cur-1)//2
            if arr[parent]>arr[cur]:
                arr[parent],arr[cur]=arr[cur],arr[parent]
            cur=cur-2 if cur%2==0 else cur-1
    return arr


def heapify2(arr): 
    last=len(arr)//2-1
    for cur in range(last, -1, -1):
        while cur<=last:
            child=cur*2+1
            sibling=child+1
            if sibling<len(arr) and arr[child]>arr[sibling]: child=sibling
            if arr[cur]>arr[child]:
                arr[cur],arr[child]=arr[child],arr[cur]
                cur=child
            else:
                break