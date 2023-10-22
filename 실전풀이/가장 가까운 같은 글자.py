def solution(s):
    res = []
    last_index = {}
    for i, x in enumerate(s):
        try:
            res.append(i - last_index[x])
        except:
            res.append(-1)
        last_index[x] = i
    return res

s = 'banana'
print(solution(s))
            