def solution(s):
    res = []
    last_index = {}
    for i, x in enumerate(s):
        j = last_index.get(x, i + 1)
        res.append(i - j)
        last_index[x] = i
    return res

s = 'banana'
print(solution(s))
            