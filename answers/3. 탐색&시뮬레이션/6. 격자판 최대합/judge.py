import sys
import answer

case_num = 5
path="/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 3/6. 격자판 최대합"

def judge():
    for i in range(case_num):
        num = i+1
        input_path=path + "/in" + str(num) + ".txt"
        output_path=path +"/out" + str(num) + ".txt"
        output=open(output_path, 'r').read()
        
        sys.stdin=open(input_path, "rt")
        n=int(input())
        m=answer.makeArr(n)
        
        a=answer.solution(n, m)
        if not a == int(output): 
                print('answer wrong!')
                print('input: ',num)
                print('output: ', a)
                print('expected: ', output)
                break
    else: 
        print('success!')

judge()