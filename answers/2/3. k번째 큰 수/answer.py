'''
N장의 카드, 그 중에 3장의 카드를 뽑아서 만들 수 있는 모든 경우의 숫자 (3카드값의 합)
n = N장의 카드값 (N = len(n))
모든 경우의 합의 숫자 중 k번째 큰 수
'''


# sorted: 기존 리스트를 변경하지 않고 정렬된 새로운 리스트를 반환
# sort: 기존 리스트를 변경 후 반환하지 않음
def solution(n,k):
    n.sort(reverse=True)
    return n[k]

solution(list(map(int, '13 15 34 23 45 65 33 11 26 42'.split(' '))), 3)