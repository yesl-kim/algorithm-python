# https://docs.google.com/document/d/1kI0aOmsuok64NuGV4IF8yFV0HdBdJBtQm07G01Hllr4/edit

from typing import List
from collections import defaultdict, deque

def solution(s: str) -> List[str]:
    # 범위
    indices = defaultdict(list)
    for i, char in enumerate(s):
        indices[char].append(i)
    
    # merge
    # ranges = sorted(indices.values(), key=lambda x: x[0])
    # merged = [(0, ranges.pop(0)[-1])]
    # for r in ranges:
    #     start, end = merged.pop()
    #     if r[0] <= end:
    #         end = max(end, r[-1])
    #     merged.append((start, end))
    #     if r[0] > end:
    #         merged.append((r[0], r[-1]))
    
    ranges = sorted(indices.values(), key=lambda x: x[0])
    merged = [(0, ranges.pop(0)[-1])]
    for cur in ranges:
        prev = merged.pop()
        if cur[0] <= prev[1]:
            r = [(prev[0], max(cur[-1], prev[1]))]
        else:
            r = [prev, (cur[0], cur[-1])]
        merged += r

    # 부분문자열로 반환
    substrings = []
    for start, end in merged:
        substrings.append(s[start: end+1])
    return substrings



def solution2(s: str) -> List[str]:
    last_index = {x: i for i, x in enumerate(s)}
    subs = []
    start, end = 0, last_index[s[0]]
    for i, x in enumerate(s):
        if i <= end:
            end = max(end, last_index[x])
        else:
            subs.append(s[start: end+1])
            start, end = i, last_index[x]
    


inputs = ['abcbedfed', 'abcdefg', 'abmowodfsxadejihgepczpc']
expected = [["a", "bcb", "edfed"], ['a', 'b', 'c', 'd', 'e', 'f', 'g'],  ["abmowodfsxad", "ejihge", "pczpc"]
]
            
for i, input in enumerate(inputs):
    # print(solution(input))
    e, o = expected[i], solution(input)
    if e != o:
        print(f"{i+1}. wrong")
        print(f"input: {input}")
        print(f"output: {o}")
        print(f"expected: {e}")
        break
print('success')