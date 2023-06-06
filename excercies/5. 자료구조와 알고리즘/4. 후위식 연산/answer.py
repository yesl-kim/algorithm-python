def solution(s):
    stack=[]
    for x in s:
        if x.isdigit():
            stack.append(int(x))
        else:
            y=stack.pop()
            if x=='*': res=stack.pop()*y
            elif x=='/': res=stack.pop()/y
            elif x=='+': res=stack.pop()+y
            elif x=='-': res=stack.pop()-y
            stack.append(res)
    return stack[0]

print(solution('352+*9-'))