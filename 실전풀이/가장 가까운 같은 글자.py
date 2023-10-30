def solution(s):
    res = []
    last_index = {}
    for i, x in enumerate(s):
        j = last_index.get(x, None)
        res.append(i-j if j is not None else -1)
        last_index[x] = i
    return res

s = 'banana'
print(solution(s))
            