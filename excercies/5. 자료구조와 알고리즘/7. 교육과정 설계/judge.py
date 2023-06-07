import sys
import time
import answer

case_num = 5
path="/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 5/7. 교육과정 설계"

def judge():
    start = time.time()
    for i in range(case_num):
        num = i+1
        input_path=path + "/in" + str(num) + ".txt"
        output_path=path +"/out" + str(num) + ".txt"
        expecteds=[line.strip() for line in open(output_path, 'rt').readlines()]
        
        sys.stdin=open(input_path, 'rt')
        n=input()
        N=int(input())
        for i in range(N):
            m=input().strip()
            a=answer.solution(n,m)
            if not expecteds[i] == f"#{i+1} {a}":
                print('answer wrong!')
                print('input: ', num)
                print('output count: ', a)
                print('expected count: ', expecteds[i])
                break
    else: 
        end=time.time()
        print('success!')
        print(f"{end - start:.5f} sec")

judge()