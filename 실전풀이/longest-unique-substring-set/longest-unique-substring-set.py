# https://docs.google.com/document/d/1kI0aOmsuok64NuGV4IF8yFV0HdBdJBtQm07G01Hllr4/edit

from typing import List
from collections import defaultdict, deque

def solution(s: str) -> List[str]:
    # 범위
    indices = defaultdict(list)
    for i, char in enumerate(s):
        indices[char].append(i)
    
    # merge
    ranges = sorted(((x[0], x[-1]) for x in indices.values()), key=lambda x: x[0])
    merged = [(0, ranges.pop(0)[1])]
    for start, end in ranges:
        prev_start, prev_end = merged.pop()
        new_end = max(prev_end, end) if start <= prev_end else prev_end
        merged.append((prev_start, new_end))
        
        if prev_end < start:
            merged.append((start, end))

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
else:
    print('success')