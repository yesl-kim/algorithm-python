import heapq

def max_heappush(heap, n):
    heap.append(n)
    cur=len(heap)-1
    while cur>0:
        parent=(cur-1)//2
        if heap[cur]>heap[parent]:
            heap[cur],heap[parent]=heap[parent],heap[cur]
            cur=parent
        else:
            break

def max_heappop(heap):
    if not heap: return
    if len(heap)==1: return heap.pop()

    root,heap[0]=heap[0],heap.pop()
    cur,lt=0,1
    while lt<len(heap):
        child,rt=lt,lt+1
        if rt<len(heap) and heap[lt]<heap[rt]:
            child=rt
        if heap[cur]<heap[child]:
            heap[cur],heap[child]=heap[child],heap[cur]
            cur,lt=child,child*2+1
        else:
            break
    return root




