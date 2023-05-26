'''

'''

# def solution(a, b):
#     count=0
#     for i in range(len(a)):
#         # print(i, '--->', end=' ')
#         sum=a[i]
#         for j in range(i+1, len(a)):
#             if sum == b:
#                 count+=1
#                 # print(count)
#                 break
#             sum+=a[j]
#             # print('({})'.format(sum), end=' ')
#         # print(sum, count)
#         else: 
#             if sum==b: count+=1
#             # else: print('pass')
#     return str(count)
                
def solution(a, b):
    count=0
    for i in range(len(a)):
        sum=a[i]
        for j in range(i+1, len(a)):
            if sum == b:
                count+=1
                break
            sum+=a[j]
        else: 
            if sum==b: count+=1
    return str(count)
