import sys
import time

# 트럭 가용무게 c
# 바둑이의 몸무게 배열 n
path='/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 6/7. 동전교환'
num=3

input_path=path + "/in" + str(num) + ".txt"
sys.stdin=open(input_path, 'rt')
N=int(input())
n=[int(x) for x in input().split()]
n.sort(reverse=True)
total=int(input())
res=0
# ====================

def dfs(i=0):
    global total
    global res
    if total==0 or i==N:
        return
    else:
        print(f"{n[i]} * {total//n[i]}개")
        res+=total//n[i]
        total=total%n[i]
        print(f"총 {res}, 나머지: {total}")
        dfs(i+1)

# ====================

start=time.time()
dfs()
if total!=0: res+=1

output_path=path +"/out" + str(num) + ".txt"
sys.stdin=open(output_path, 'rt')
expected=int(input())
if not res==expected: 
        print('answer wrong!')
        print('output: ', res)
        print('expected: ', expected)
else:
    end=time.time()
    print('success!')
    print(f"{end - start:.5f} sec")


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
