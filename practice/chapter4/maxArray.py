#done with some help from online

def max_array(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        maxim = max(arr[0],max_array(arr[1:]))
        return maxim


#test array with length 0
arr = []
print(max_array(arr))

#test array with length 1
arr = [1]
print(max_array(arr))

#test array with length 1
arr = [1,2,456546,7]
print(max_array(arr))