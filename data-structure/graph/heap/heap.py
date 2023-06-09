# heap: number[]
# data: number
import heapq

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
        

h1 = [3, 4, 6, 8, 5, 7]
h2 = [3, 4, 6, 8, 5, 7]
heappush(h1, 2)
heapq.heappush(h2, 2)
print("구현한 함수의 결과: ", h1)
print("heapq 메서드의 결과:", h2)
heappush(h1, 3)
heapq.heappush(h2, 3)
print("구현한 함수의 결과: ", h1)
print("heapq 메서드의 결과:", h2)