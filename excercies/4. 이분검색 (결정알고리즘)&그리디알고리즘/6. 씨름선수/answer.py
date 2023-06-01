'''
n=[h,w][]
h는 키, w는 몸무게
'''

# ❌ O(N 제곱)
# def solution(n):
#     n.sort(reverse=True)
#     c=0
#     for i in range(len(n)):
#         ww=n[i][1]
#         for j in range(0,i):
#             w=n[j][1]
#             if ww<=w: break
#         else: c+=1
#     return c

# ✅ O(N) (0.00167 sec)
def solution(n):
    n.sort(reverse=True)
    c=mw=0
    for [_,w] in n:
        if w>mw:
            c+=1
            mw=w
    return c
