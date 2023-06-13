import sys
import time
import answer

case_num = 5
path="/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 6/1. 재귀함수란(이진수출력)"

def judge():
    start = time.time()
    for i in range(case_num):
        num = i+1
        input_path=path + "/in" + str(num) + ".txt"
        output_path=path +"/out" + str(num) + ".txt"
        
        sys.stdin=open(input_path, 'rt')
        n=int(input())
        a=answer.solution2(n)

        sys.stdin=open(output_path, 'rt')
        expected=input()
        if not a==expected: 
                print('answer wrong!')
                print('input: ', num)
                print('output count: ', a)
                print('expected count: ', expected)
                break
    else: 
        end=time.time()
        print('success!')
        print(f"{end - start:.5f} sec")

judge()