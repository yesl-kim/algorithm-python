# https://docs.google.com/document/d/1kI0aOmsuok64NuGV4IF8yFV0HdBdJBtQm07G01Hllr4/edit

from typing import List
from collections import defaultdict, deque

def solution(s: str) -> List[str]:
    # 범위
    indices = defaultdict(list)
    for i, char in enumerate(s):
        indices[char].append(i)
    
    # merge
    ranges = sorted(indices.values(), key=lambda x: x[0])
    first = ranges.pop(0) # 🤔
    merged = [(first[0], first[-1])]
    for r in ranges:
        start, end = merged[-1]
        if r[0] < end:
            merged[-1] = (start, max(r[-1], end))
        else:
            merged.append([r[0], r[-1]])

    # 부분문자열로 반환
    substrings = []
    for start, end in merged:
        substrings.append(s[start: end+1])
    return substrings

    


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