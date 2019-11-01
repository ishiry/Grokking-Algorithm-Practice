# quicksort array

def qsort_array(arr):
    if len(arr) < 2:
        return arr

    else:
        pivot = arr[0]
        arr_small = [i for i in arr[1:] if i <= pivot]
        arr_big = [i for i in arr[1:] if i >= pivot]
        return arr_small + [pivot] + arr_big

# 1 element
print(qsort_array([1]))

# 5 element
print(qsort_array([1,2,3,4,5]))