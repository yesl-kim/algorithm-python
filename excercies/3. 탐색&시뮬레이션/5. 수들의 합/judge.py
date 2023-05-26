import sys
import answer

case_num = 5
path="/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 3/5. 수들의 합"

def judge():
    for i in range(case_num):
        num = i+1
        input_path=path + "/in" + str(num) + ".txt"
        output_path=path +"/out" + str(num) + ".txt"
        output=open(output_path, 'r').read()
        
        sys.stdin=open(input_path, "rt")
        [_, b]=list(map(int, input().split()))
        n=list(map(int, input().split()))
        
        a=answer.solution(n, b)
        if not a == output: 
                print('answer wrong!')
                print('input: ',num, '. ', n, b)
                print('output: ', a)
                print('expected: ', output)
                break
    else: 
        print('success!')

judge()