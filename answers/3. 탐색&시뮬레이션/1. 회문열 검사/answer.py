'''
ox 문제의 점수계산

채점 문자열 n

맞으면 1, 틀리면 0
연속 정답인경우 가산점
가산점까지 합한 총 점수 출력
'''

def is회문(s):
    s=s.lower()
    temp=''
    for x in s:
        temp=x+temp
    if s==temp: return 'YES'
    else: return 'NO'

def solution(n):
    a=[]
    for i in range(len(n)):
        aa="#{} {}".format(str(i+1), is회문(n[i]))
        a.append(aa)
    return a

# print(solution(['level', 'soon', 'gooG', 'moon']))
# solution('0 1 0 0 1 0 1 1 0 0')

