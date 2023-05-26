# 0.00200 s

def solution(n, m):
    hs=[]
    vs=[]
    x=y=0
    for i in range(n):
        s1=s2=0
        r=n-1-i
        x+=m[i][i]
        y+=m[r][r]
        for j in range(n):
            s1+=m[i][j]
            s2+=m[j][i]
        hs.append(s1)
        vs.append(s2)
    return max(hs+vs+[x,y])
    

'''
행의 합
0 0
0 1
0 2
0 3
0 4

1 0
1 1
...

열의 합
0 0
1 0
2 0
3 0
4 0

0 1
1 1
2 1
...

대각선
0 0
1 1
2 2
...

4 4
3 3
2 2
...
'''