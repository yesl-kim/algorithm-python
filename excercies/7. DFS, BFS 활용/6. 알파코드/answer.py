import sys
import time

start=time.time()
input_path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 7/6. 알파코드/in5.txt'
sys.stdin=open(input_path, 'rt')
code=input()
cnt=0
res=[]

# def dfs(L=0, s=''):
#     global cnt
#     if L==len(code):
#         print(s)
#         cnt+=1
#     else:
#         if code[L]=='0': return
#         dfs(L+1, s+chr(int(code[L])+64))
#         if L+1<len(code):
#             n=int(code[L]+code[L+1])
#             if n<27:
#                 dfs(L+2,s+chr(n+64))

def dfs(L=0):
    global cnt
    global res
    if L==len(code):
        print("".join([chr(x+64) for x in res]))
        cnt+=1
    else:
        if code[L]=='0': return
        res.append(int(code[L]))
        dfs(L+1)
        res.pop()
        if L+1<len(code):
            n=int(code[L]+code[L+1])
            if n<27:
                res.append(n)
                dfs(L+2)
                res.pop()
    

dfs()
print(cnt)
end=time.time()
print(f"{end - start:.5f} sec")