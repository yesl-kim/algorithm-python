import sys
import answer

case_num = 5
path="/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 2/3. k번째 큰 수"

def judge():
    for i in range(case_num):
        num = i+1
        input_path=path + "/in" + str(num) + ".txt"
        output_path=path +"/out" + str(num) + ".txt"
        input=open(input_path, "r").read().split('\n')
        output=open(output_path, 'r').read()

        [N, k]=list(map(int, input[0].split()))
        n=list(map(int, input[1].split()))
        # print(N, n, k)
        a=answer.solution(N, n, k)
        if not a == int(output): 
                print('answer wrong!')
                print('input: ', N, n, k)
                print('output: ', a)
                print('expected: ', output)
    else: 
        print('success!')

judge()