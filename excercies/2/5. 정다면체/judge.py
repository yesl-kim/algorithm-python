import sys
import answer

case_num = 5
path="/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 2/5. 정다면체"

def judge():
    for i in range(case_num):
        num = i+1
        input_path=path + "/in" + str(num) + ".txt"
        output_path=path +"/out" + str(num) + ".txt"
        output=open(output_path, 'r').read()
        
        sys.stdin=open(input_path, "rt")
        [n, m]=list(map(int, input().split()))
        
        a=answer.solution(n, m)
        if not a == output: 
                print('answer wrong!')
                print('input: ', n, m)
                print('output: ', a)
                print('expected: ', output)
                break
    else: 
        print('success!')

judge()