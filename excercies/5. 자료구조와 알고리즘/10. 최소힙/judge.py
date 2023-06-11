import sys
import time
import answer
import heapq

case_num = 5
path="/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 5/10. 최소힙"

def judge():
    start = time.time()
    for i in range(case_num):
        num = i+1
        input_path=path + "/in" + str(num) + ".txt"
        output_path=path +"/out" + str(num) + ".txt"
        
        sys.stdin=open(input_path, 'rt')
        res=[]
        heap=[]
        while True:
            n=int(input())
            if n==-1: break
            elif n==0: 
                if len(heap)==0: res.append(-1)
                else: res.append(heapq.heappop(heap))
            else: heapq.heappush(heap, n)

        expected=[int(x.strip()) for x in open(output_path, 'rt').readlines()]
        if not res==expected: 
                print('answer wrong!')
                print('input: ', num)
                print('output count: ', res)
                print('expected count: ', expected)
                break
    else: 
        end=time.time()
        print('success!')
        print(f"{end - start:.5f} sec")

judge()