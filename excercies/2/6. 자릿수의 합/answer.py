'''
n개의 자연수 m
자릿수의 합이 가장 큰 수 반환
'''
def solution(m):
    max=-1
    m=m.split()
    for s in m:
        sum=0
        for n in s:
            # print(n)
            sum+=int(n)
        if max < sum:
            max=sum
            x=s
    return x
    # print(x)

# solution('125 15232 97')
