import sys
import time
import answer

case_num = 1
path="/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 4/9. 증가수열 만들기"

def judge():
    start = time.time()
    for i in range(case_num):
        num = i+1
        input_path=path + "/in" + str(num) + ".txt"
        output_path=path +"/out" + str(num) + ".txt"
        
        sys.stdin=open(input_path, 'rt')
        input()
        n=[int(x) for x in input().split()]
        c,s=answer.solution(n)

        sys.stdin=open(output_path, 'rt')
        answer_length=int(input())
        answer_string=input()
        if not c == answer_length or not s == answer_string: 
                print('answer wrong!')
                print('input: ', num)
                print('output count: ', c)
                print('expected count: ', answer_length)
                print('output string: ', s)
                print('expected string: ', answer_string)
                break
    else: 
        end=time.time()
        print('success!')
        print(f"{end - start:.5f} sec")

judge()