'''
가장 많은 상금을 받은 사람의 상금을 출력

2차원 배열
각 사람이 주사위를 던져 나온 3개의 눈이 문자열로 담긴 배열 n
ex. ["x x x", "x x x"] => 2사람이 던져서 나온 3개의 주사위 눈 수

몇 개의 숫자가 같은지
같은 숫자가 뭔지
'''

def solution(n):
    a=[]
    for x in n:
        x=list(map(int, x.split()))
        c={}
        for m in x:
            c[m]=c.get(m, 0)+1
        # print(c)
        for num, count in c.items():
            if count == 3:
                sum=10000+num*1000
                break
            elif count ==2:
                sum=1000+100*num
                break
        else: sum=100*max(list(c.values()))
        a.append(sum)
    # print(str(max(a)))
    return str(max(a))
                
            



# print(solution('32 55 62 3700 250'))
# solution(['3 3 6', '2 2 2', '6 2 5'])

