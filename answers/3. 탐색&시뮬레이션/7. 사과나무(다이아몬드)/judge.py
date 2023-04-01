import sys
import time
import answer
import answer2

case_num = 5
path="/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 3/7. 사과나무"

def judge():
    start = time.time()
    for i in range(case_num):
        num = i+1
        input_path=path + "/in" + str(num) + ".txt"
        output_path=path +"/out" + str(num) + ".txt"
        output=open(output_path, 'r').read()
        
        sys.stdin=open(input_path, "rt")
        n=int(input())
        m=answer.makeArr(n)
        # print(m)
        
        a=answer2.solution(n, m)
        if not a == int(output): 
                print('answer wrong!')
                print('input: ',num)
                print('output: ', a)
                print('expected: ', output)
                break
    else: 
        end=time.time()
        print('success!')
        print(f"{end - start:.5f} sec")

judge()