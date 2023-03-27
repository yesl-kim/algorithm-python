import sys
import answer

case_num = 5
path="/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 3/3. 카드 역배치"

def judge():
    for i in range(case_num):
        num = i+1
        input_path=path + "/in" + str(num) + ".txt"
        output_path=path +"/out" + str(num) + ".txt"
        output=open(output_path, 'r').read()
        
        sys.stdin=open(input_path, "rt")
        n=list(range(1,21))
        for i in range(10):
            [a, b]=list(map(int, input().split()))
            n=answer.solution(a,b,n)

        a=list(map(str, n))    
        a=" ".join(a)
        if not a == output: 
                print('answer wrong!')
                print('input: ', num)
                print('output: ', a)
                print('expected: ', output)
                break
    else: 
        print('success!')

judge()