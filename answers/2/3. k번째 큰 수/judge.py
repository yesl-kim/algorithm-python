import answer

case_num = 1
inputPath="/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 2/2. k번째 수"
outputPath="/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 2/2. k번째 수"

def judge():
    for i in range(case_num):
        num = i+1
        filePath_input=inputPath + "/in" + str(num) + ".txt"
        filePath_output=outputPath +"/out" + str(num) + ".txt"
        input=open(filePath_input, "r").read().split('\n')
        output=open(filePath_output, 'r').read().split('\n')

        for c in range(int(input[0])):
            j=c*2+1
            [_, s, e, k] = map(int, input[j].split(' '))
            n=list(map(int, (input[j+1].strip().split(' '))))
            a=answer.solution(n,s,e,k)
            if not output[c].endswith(str(a)):
                print('answer wrong!')
                print('input: ', n, s, e, k)
                print('output: ', a)
                print('expected: ', output[c])
        else:
            print('success!')

judge()