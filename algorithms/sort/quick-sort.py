arr=[45,21,23,36,15,67,11,60,20,33]

def quick_sort(lt,rt):
    if lt<rt:
        pivot=arr[rt]
        p=lt
        for i in range(lt,rt):
            if arr[i]<=pivot:
                arr[p],arr[i]=arr[i],arr[p]
                p+=1
        arr[p],arr[rt]=pivot,arr[p]
        quick_sort(lt,p-1)
        quick_sort(p+1,rt)
        

quick_sort(0,len(arr)-1)
print(arr)