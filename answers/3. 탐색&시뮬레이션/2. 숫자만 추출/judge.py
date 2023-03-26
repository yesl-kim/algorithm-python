import sys
import answer

case_num = 5
path="/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 3/2. 숫자만 추출"

def judge():
    for i in range(case_num):
        num = i+1
        input_path=path + "/in" + str(num) + ".txt"
        output_path=path +"/out" + str(num) + ".txt"
        output=open(output_path, 'r').read()
        
        sys.stdin=open(input_path, "rt")
        n=input()
        
        a=answer.solution(n)
        if not a == output: 
                print('answer wrong!')
                print('input: ', n)
                print('output: ', a)
                print('expected: ', output)
                break
    else: 
        print('success!')

judge()