arr=[23,11,45,36,15,67,33,21]
def merge_sort(lt,rt):
    if lt<rt:
        mid=(lt+rt)//2
        merge_sort(lt,mid)
        merge_sort(mid+1,rt)
        tmp=[] # 정렬된 배열
        p1,p2=lt,mid+1
        while p1<=mid and p2<=rt:
            if arr[p1]<arr[p2]:
                tmp.append(arr[p1])
                p1+=1
            else:
                tmp.append(arr[p2])
                p2+=1
        if p1<=mid:
            tmp+=arr[p1:mid+1]
        if p2<=rt:
            tmp+=arr[p2:rt+1]
        for i in range(len(tmp)):
            arr[lt+i]=tmp[i]

merge_sort(0,7)
print(arr)