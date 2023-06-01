import sys
import time
import answer

case_num = 5
path="/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 4/5. 회의실 배정"

def judge():
    start = time.time()
    for i in range(case_num):
        num = i+1
        input_path=path + "/in" + str(num) + ".txt"
        output_path=path +"/out" + str(num) + ".txt"
        output=open(output_path, 'r').readline()
        
        sys.stdin=open(input_path, 'rt')
        N=int(input())
        n=[[int(x) for x in input().split()] for _ in range(N)]
        n.sort(key=lambda x: (x[1], x[0]))
        a=answer.solution(n)
        if not a == int(output): 
                print('answer wrong!')
                print('input: ', n)
                print('output: ', a)
                print('expected: ', output)
                break
    else: 
        end=time.time()
        print('success!')
        print(f"{end - start:.5f} sec")

judge()