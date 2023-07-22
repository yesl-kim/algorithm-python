import time

'''
s: string
dict: string[]
'''

def solution(s,dict):
    res=''
    n=len(s)
    ch=[0]*(n+1)
    for x in dict:
        end=0
        while end<n:
            start=s[end:].find(x)
            if start<0: break
            start+=end
            end=start+len(x)
            for i in range(start,end):
                ch[i]=1
    for i in range(n):
        temp=s[i]
        if ch[i]==1:
            if i==0 or ch[i-1]==0:
                temp='<b>'+temp
            if ch[i+1]==0:
                temp+='</b>'
        res+=temp
    return res

st=time.time()
print(solution('aaabbccaabc', ['aaa','aab','bc']))
end=time.time()
print(f"{end - st:.5f} sec")