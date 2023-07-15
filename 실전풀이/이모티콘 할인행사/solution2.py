def solution(users, emoticons):
    answer = [-1,-1]
    dc=[0]*len(emoticons)

    def dfs(L=0):
        if L==len(emoticons):
            cnt,sales=0,0
            for r,p in users:
                bought=0
                for i in range(len(emoticons)):
                    if r<=dc[i]:
                        bought+=emoticons[i]*(100-dc[i])//100
                if p<=bought:
                    cnt+=1
                else:
                    sales+=bought
            if answer[0]<cnt or (answer[0]==cnt and answer[1]<sales):
                answer[0],answer[1]=cnt,sales
                        
        else:
            for i in range(4,0,-1):
                dc[L]=i*10
                dfs(L+1)
    dfs()
    return answer