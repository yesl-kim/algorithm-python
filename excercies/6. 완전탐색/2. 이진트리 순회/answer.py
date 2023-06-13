# 이진트리 순회
# n: 이진트리 배열

n=[1,2,3,4,5,6,7]

# 전위순회
def preorder(n, i=0):
    l=len(n)
    if i>=l: return
    print(n[i], end=' ')
    lt,rt=i*2+1,i*2+2
    if lt<l and n[lt] is not None: preorder(n, lt)
    if rt<l and n[rt] is not None: preorder(n, rt)
        

# preorder(n)

# 1. 자식요소 확인
# 2. 형제요소 확인
def postorder(n, i=0):
    l=len(n)
    lt,sibling=i*2+1, i+1
    if lt<l and n[lt] is not None: postorder(n,lt)
    print(n[i], end=' ')
    if sibling<l and (sibling-1)//2 == (i-1)//2: postorder(n, sibling)

postorder(n)