import sys
import time
import answer

case_num = 5
path="/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 5/5. 공주구하기"

def judge():
    start = time.time()
    for i in range(case_num):
        num = i+1
        input_path=path + "/in" + str(num) + ".txt"
        output_path=path +"/out" + str(num) + ".txt"
        
        sys.stdin=open(input_path, 'rt')
        n,k=map(int, input().split())
        output=answer.solution(n,k)

        sys.stdin=open(output_path, 'rt')
        expected=int(input())
        if not output==expected: 
                print('answer wrong!')
                print('input: ', num)
                print('output count: ', output)
                print('expected count: ', expected)
                break
    else: 
        end=time.time()
        print('success!')
        print(f"{end - start:.5f} sec")

judge()