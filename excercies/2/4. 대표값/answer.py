'''
N명의 학생의 수학점수 배열 n
평균 점수에 가장 가까운 학생은 몇번째인지
'''

import statistics

def solution_(n):
    aver=round(statistics.mean(n))
    e=None
    for x in enumerate(n):
        if e == None:
            e=x
            continue
        
        if abs(aver-e[1]) < abs(aver-x[1]):
            continue
        elif abs(aver-e[1]) > abs(aver-x[1]):
            e=x
        else:
            if e[1] > x[1]:
                continue
            elif e[1] < x[1]:
                e=x
            else:
                if e[0] > x[0]: # 앞 순서부터 순회를 돌기 때문에 이럴 경우는 없음
                    e=x
    return "{} {}".format(aver, e[0] + 1)

def solution(n):
    ave=sum(n)/len(n)
    ave=int(ave+0.5)
    min=99999999999999999 #차이
    for i,x in enumerate(n):
        tmp=abs(ave-x)
        if tmp<min:
            min=tmp
            score=x
            res=i
        elif tmp==min:
            if score<x:
                score=x
                res=i
    return "{} {}".format(ave, res+1)
        

def test():
    print(int(3.4))
    print(int(3.5))
    print(int(3.6))
    print(int(4.5))

test()