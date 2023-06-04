'''
1~N까지의 역수열 n
0.00340 sec
'''

def solution(n, arr):
    res=[0]*(n)
    for i in range(n):
        # 자연수는 i+1
        # 자연수 앞에 있는 자연수의 개수는 n[i]
        c=0
        for j in range(n):
            if not res[j]==0:
                continue
            if c==arr[i]:
                res[j]=i+1
                break
            c+=1
    return res

# print(solution(8,[5,3,4,0,2,1,1,0]))