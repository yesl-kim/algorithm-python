import sys
import time

# 트럭 가용무게 c
# 바둑이의 몸무게 배열 n
path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 6/8. 순열 구하기'
num=5

input_path=path + "/in" + str(num) + ".txt"
sys.stdin=open(input_path, 'rt')
N,m=map(int, input().split())
# ====================

n=list(range(1, N+1))
ch=[False]*N
c=0
def dfs(L=0):
    global c
    if L==m:
        c+=1
        print(" ".join([str(n[i]) for i,v in enumerate(ch) if v]))
    else:
        for i in range(N):
            if ch[i]: continue
            ch[i]=True
            dfs(L+1)
            ch[i]=False

# ====================

start=time.time()
dfs()
print(c)

# output_path=path +"/out" + str(num) + ".txt"
# sys.stdin=open(output_path, 'rt')
# expected=int(input())
# if not res==expected: 
#         print('answer wrong!')
#         print('output: ', res)
#         print('expected: ', expected)
# else:
#     end=time.time()
#     print('success!')
#     print(f"{end - start:.5f} sec")


# for i in range(1, num+1):
#     input_path=path + "/in" + str(num) + ".txt"
#     sys.stdin=open(input_path, 'rt')
#     N=int(input())
#     n=[int(x) for x in input().split()]
#     total=int(input())
    
#     # =====================
#     n.sort(reverse=True)
#     res=0
#     start=time.time()
#     dfs()
#     if total!=0: res+=1
#     # =====================


#     output_path=path +"/out" + str(num) + ".txt"
#     sys.stdin=open(output_path, 'rt')
#     expected=int(input())
#     if not res==expected: 
#             print('answer wrong!')
#             print('output: ', res)
#             print('expected: ', expected)
#             break
# else:
#     end=time.time()
#     print('success!')
#     print(f"{end - start:.5f} sec")
