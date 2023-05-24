# 0.00180 sec

def makeArr():
    return [[int(x) for x in input().split()] for _ in range(9)]

def solution(n):
    z=[]
    for i in range(len(n)):
        a=b=0
        for j in range(len(n)):
            if a==n[i][j] or b==n[j][i]: return 'NO'
            else: 
                a=n[i][j]
                b=n[j][i]
            if i%3==0:
                for k in range(3):
                    z.append(n[i+k][j])
            else: continue
            if j%3 ==2:
                if not len(set(z)) == 9: return 'NO'
                z=[]
    return 'YES'
            

        
    
# a=move([[10, 13, 10, 12, 15], [12, 39, 30, 23, 11], [11, 25, 50, 53, 15], [19, 27, 29, 37, 27], [19, 13, 30, 13, 19]], [2,0,3])
# a=move(a, [5, 1, 2])
# a=move(a, [3, 1, 4])
# print(count(a))