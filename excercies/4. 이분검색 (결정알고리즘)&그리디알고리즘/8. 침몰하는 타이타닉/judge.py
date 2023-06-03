import sys
import time
import answer

case_num = 5
path="/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 4/8. 침몰하는 타이타닉"

def judge():
    start = time.time()
    for i in range(case_num):
        num = i+1
        input_path=path + "/in" + str(num) + ".txt"
        output_path=path +"/out" + str(num) + ".txt"
        output=open(output_path, 'r').readline()
        
        sys.stdin=open(input_path, 'rt')
        _,m=map(int, input().split())
        n=[int(x) for x in input().split()]
        a=answer.solution2(n, m)
        if not a == int(output): 
                print('answer wrong!')
                print('input: ', num)
                print('output: ', a)
                print('expected: ', output)
                break
    else: 
        end=time.time()
        print('success!')
        print(f"{end - start:.5f} sec")

judge()