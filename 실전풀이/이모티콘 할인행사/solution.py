def solution(users, emoticons):
    answer = [0,0]
    dc=[0]*len(emoticons)
    
    _max=0
    _min=50
    for r,_ in users:
        _max=max(_max,r)
        _min=min(_min,r)
    _min=int(round(_min+5,-1))

    def dfs(L=0):
        if L==len(emoticons):
            cnt,sales=0,0
            for r,p in users:
                bought=0
                for i in range(len(emoticons)):
                    if r<=dc[i]:
                        bought+=emoticons[i]*(1-dc[i]/100)
                if p<=bought:
                    cnt+=1
                else:
                    sales+=bought
            print(dc)
            print(cnt, sales)
            print()
            if answer[0]<cnt or (answer[0]==cnt and answer[1]<sales):
                answer[0],answer[1]=cnt,sales
                        
        else:
            for discount in range(_max,_min-1,-10):
                dc[L]=discount
                dfs(L+1)
    dfs()
    print('------')
    return answer

print(solution(	[[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))