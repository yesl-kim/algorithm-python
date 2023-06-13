
# 0.00128 sec
def solution(n):
    if n//2==1: return f"{n//2}{n%2}"
    else: return solution(n//2)+str(n%2)


def solution2(n):
    if n==0: return ''
    else: return solution(n//2)+str(n%2)
    