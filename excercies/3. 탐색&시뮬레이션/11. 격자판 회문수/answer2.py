def solution(n):
    c=0
    for i in range(3):
        for j in range(7):
            # 7행 확인
            x=n[j][i:i+5]
            if x == x[::-1]:c+=1
            # 7열 확인
            for k in range(2):
                # 하나의 열 안에서 5자리 회문수 확인
                # 가장자리 2자리만 비교하면 됨
                if n[i+k][j]!=n[i+5-1-k][j]: break
            else: c+=1