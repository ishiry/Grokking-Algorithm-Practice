## count elements in an array

def count_array_elem(arr):
    if len(arr) == 0:
        return 0
    else:
        first = arr[0]
        rest = arr[1:]
        sum = 1 + count_array_elem(rest)
        return sum


#test empyt array
arr = []
print(count_array_elem(arr))

#test array with int
arr = [1,2,3,4]
print(count_array_elem(arr))

#test array with float
arr = ['a','v','c']
print(count_array_elem(arr))