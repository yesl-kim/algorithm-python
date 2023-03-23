import sys
import answer

case_num = 5
path="/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 2/9. 주사위 게임"

def judge():
    for i in range(case_num):
        num = i+1
        input_path=path + "/in" + str(num) + ".txt"
        output_path=path +"/out" + str(num) + ".txt"
        output=open(output_path, 'r').read()
        
        sys.stdin=open(input_path, "rt")
        m=int(input())
        n=[]
        for _ in range(m):
            x=input()
            n.append(x)
        
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