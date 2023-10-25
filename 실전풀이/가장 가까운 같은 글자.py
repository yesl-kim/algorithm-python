def solution(s):
    res = []
    last_index = {}
    for i, x in enumerate(s):
        j = last_index.get(x, -1)
        if j < 0:
            res.append(-1)
        else:
            res.append(i - j)
        last_index[x] = i
    return res

s = 'banana'
print(solution(s))
            