def linear_search(array, search_value):
    for i in range(len(array)):
        if array[i]==search_value: return i
        elif array[i]>search_value: break # 정렬된 배열인 경우 일찍 종료할 수 있다.
    return None