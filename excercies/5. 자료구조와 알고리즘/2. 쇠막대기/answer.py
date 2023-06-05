def solution(s):
    stack=[]
    sum=0
    for i in range(len(s)):
        x=s[i]
        if x=='(': 
            stack.append(x)
        elif s[i-1]=='(':
            stack.pop()
            sum+=len(stack)
        else:
            stack.pop()
            sum+=1
    return sum

print(solution('(((()(()()))(())()))(()())'))

