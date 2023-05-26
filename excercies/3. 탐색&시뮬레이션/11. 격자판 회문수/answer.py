'''
n: str[][]
'''

# 0.00176 sec

def makeArr():
    return [[x for x in input().split()] for _ in range(7)]

def solution(n):
    c=0
    l=len(n)
    for i in range(l):
        x=[]
        y=[]
        for j in range(l):
            x.append(n[i][j])
            y.append(n[j][i])
            if len(x)<5: 
                continue
            if "".join(x)=="".join(list(reversed(x))):
                c+=1
            if "".join(y)=="".join(list(reversed(y))): 
                c+=1
            x.pop(0)
            y.pop(0)
    return c

# print(solution([['2', '4', '1', '5', '3', '2', '6'], ['3', '5', '1', '8', '7', '1', '7'], ['8', '3', '2', '7', '1', '3', '8'], ['6', '1', '2', '3', '2', '1', '1'], ['1', '3', '1', '3', '5', '3', '2'], ['1', '1', '2', '5', '6', '5', '2'], ['1', '2', '2', '2', '2', '1', '5']]))