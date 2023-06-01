'''
N개의 회의 시간표 배열 n
n은 회의의 시작 시간(s)과 끝나는 시간(e)이 배열 형태 [s,e]로 담긴 2차원 배열

0.13929 sec
'''

def solution(n):
    c=0
    et=0
    for [s, e] in n:
        if et<=s: 
            et=e
            c+=1
    return c