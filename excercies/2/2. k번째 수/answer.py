'''
N개의 숫자 배열 n
s번째부터 e번째까지의 수를 오름차순 정렬했을 때
k번째 수
'''

import sys

# sorted: 기존 리스트를 변경하지 않고 정렬된 새로운 리스트를 반환
# sort: 기존 리스트를 변경 후 반환하지 않음
def solution(n,s,e,k):
    a=sorted(n[s-1:e])
    return a[k-1]