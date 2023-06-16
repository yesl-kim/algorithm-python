N=3
m=2
n=list(range(1,N+1))
def dfs(L=0, res=''):
    if L==m:
        print(res.strip())
    else:
        L+=1
        for x in n:
            dfs(L, f"{res} {x}")

dfs()
print(N**m)