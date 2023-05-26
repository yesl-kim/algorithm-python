import sys
sys.stdin=open("/Users/kimyeseul/dev/algorithm/algorithm-python/answers/2/1.첫번째약수/input.txt", "rt")
s=input()
# print(n)

# 6 3 => 3
# a = [1, 2, 3, 6] => a[k -1]

def solution(s):
    n, k=map(int, s.split(' '))
    a=[i for i in range(1, n+1) if n%i == 0]
    if len(a) < k-1:
        return -1
    else:
       return a[k -1]

def solution2(s):
    n, k=map(int, s.split(' '))
    c=0
    for i in range(1, n+1):
        if n%i == 0:
            c+=1
        if c == k:
            return i
    else:
        return -1
            

# /Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 2/1. k번째 약수/in1.txt

def test():
    for i in range(5):
        num = i+1
        filePath_input="/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 2/1. k번째 약수/in" + str(num) + ".txt"
        filePath_output="/Users/kimyeseul/dev/algorithm/algorithm-python/ignore/pythonalgorithm_formac/섹션 2/1. k번째 약수/out" + str(num) + ".txt"
        sys.stdin=open(filePath_input, "rt")
        s=input()
        # print(solution(s))
        a=solution2(s)
        sys.stdin=open(filePath_output, "rt")
        o=input()
        print(a == int(o))

test()