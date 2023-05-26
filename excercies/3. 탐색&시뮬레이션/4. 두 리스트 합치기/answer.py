'''
오름차순의 두 리스트 a, b
두 리스트를 오름차순으로 합친 리스트 n 반환
'''

def solution(a, b):
    n=a+b
    n.sort()
    return " ".join(list(map(str, n)))


# print(solution([1, 3, 5], [2,3,6,7,9]))
# solution('0 1 0 0 1 0 1 1 0 0')
