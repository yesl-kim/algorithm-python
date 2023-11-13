from collections import Counter, defaultdict

def solution(s: str, k: int) -> str:
    size = len(s)
    count = Counter(s)

    most_common_cnt = count[count.most_common()[0][0]]
    if size // k < most_common_cnt:
        return ''
    
    res = ''
    min_next_index = defaultdict(int)
    for i in range(len(s)):
        for x, _ in count.most_common():
            if min_next_index[x] <= i:
                res += x
                min_next_index[x] = i + k
                count[x] -= 1
                break
        else:
            return ''
    return res


# s = 'aabbcc'
# k = 3
# s = 'aaabc'
# k = 3
s = 'aaadbbcc'
k = 2
print(solution(s, k))