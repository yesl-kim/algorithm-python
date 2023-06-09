def heappush(heap, data):
    heap.append(data)
    cur=len(heap)-1
    while cur>0:
        p=(cur-1)//2
        if heap[p]>heap[cur]:
            heap[p],heap[cur]=heap[cur],heap[p]
            cur=p
        else:
            break