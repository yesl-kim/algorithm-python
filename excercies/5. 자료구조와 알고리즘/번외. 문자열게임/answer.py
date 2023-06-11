import heapq

# 1차 시도
def solution(scoville, k):
    c=0
    scoville.sort(reverse=True)
    while min(scoville)<=k:
        scoville.append(scoville.pop()+(scoville.pop()*2))
        c+=1
    return c

# 2차 시도 (최소 힙 사용)
def solution(scoville, k):
    c=0
    heapq.heapify(scoville)
    while scoville[0]<k:
        heapq.heappush(scoville, heapq.heappop(scoville)+ heapq.heappop(scoville)*2)
        c+=1
    return c
    
# 정답 풀이: 예외 처리 추가
def solution(scoville, k):
    c=0
    heapq.heapify(scoville)
    while scoville[0]<k:
        try:
            heapq.heappush(scoville, heapq.heappop(scoville)+ heapq.heappop(scoville)*2)
            c+=1
        except:
            return -1
    return c


print(solution([1,2, 3, 9, 10, 12],7))