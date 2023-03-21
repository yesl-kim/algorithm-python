'''
N명의 학생의 수학점수 배열 n
평균 점수에 가장 가까운 학생은 몇번째인지
'''

import statistics

def solution(n):
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
                if e[0] > x[0]:
                    e=x
    return "{} {}".format(aver, e[0] + 1)
