import sys
import time
import answer

case_num = 5
path="/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 4/7. 창고 정리"

def judge():
    start = time.time()
    for i in range(case_num):
        num = i+1
        input_path=path + "/in" + str(num) + ".txt"
        output_path=path +"/out" + str(num) + ".txt"
        output=open(output_path, 'r').readline()
        
        sys.stdin=open(input_path, 'rt')
        input()
        n=[int(x) for x in input().split()]
        m=int(input())
        a=answer.solution(n, m)
        if not a == int(output): 
                print('answer wrong!')
                print('input: ', num)
                print('output: ', a)
                print('expected: ', output)
                break
    else: 
        end=time.time()
        print('success!')
        print(f"{end - start:.5f} sec")

judge()