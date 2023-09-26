# ~세번째 풀이
# from collections import defaultdict
# from functools import reduce
# from operator import mul

# def solution(clothes):
#     hash = defaultdict(list)
#     for name, kind in clothes:
#         hash[kind].append(name)

#     return reduce(mul, [len(x) + 1 for x in hash.values()], 1) - 1

# 최종
from collections import Counter
from functools import reduce
from operator import mul

def solution(clothes):
    clothes = Counter([kind for _, kind in clothes])
    return reduce(mul, [x + 1 for x in clothes.values()], 1) - 1


'''
난이도: level 2, 소요시간: 40~50분...
1. dfs (product)
    - 해시맵 계산 ({ 의상종료: [의상, ...] })
    - 각 의상별 조합의 개수 반환 (product 활용)
    => 의상을 하나만 입어도 되기 때문에 오답

2. 각 의상 종류당 의상을 입지 않는 경우 추가
    - hash = defaultdict(lambda: [''])
    - 동일하게 product 활용
    => 시간초과

3. 조합 x 경우의 수만 계산
    - 리스트의 길이 활용하여 계산 (의상종류별 <의상 개수+1>의 누적곱)
    => 정답

4. 생각해보니 리스트 필요 x -> 의상 요소도 개수만 카운팅하도록 수정

'''