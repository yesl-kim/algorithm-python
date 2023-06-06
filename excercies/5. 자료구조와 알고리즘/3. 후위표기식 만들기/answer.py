# 0.00255 sec
def solution(s):
    stack=[]
    res=''
    for x in s:
        if x.isdecimal():
            res+=x
        else:
            if x=='(':
                stack.append(x)
            elif x=='*' or x=='/':
                while stack and (stack[-1]=='*' or stack[-1]=='/'):
                    res+=stack.pop()
                stack.append(x)
            elif x=='+' or x=='-':
                while stack and stack[-1]!='(':
                    res+=stack.pop()
                stack.append(x)
            elif x==')':
                while stack and stack[-1]!='(':
                    res+=stack.pop()
                stack.pop()
    while stack:
        res+=stack.pop()
    return res


# print(solution('3*(5+2)-9'))
