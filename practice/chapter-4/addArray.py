## add elements in an array

def add_array(arr):
    if len(arr) == 0:
        return 0
    else:
        first = arr[0]
        rest = arr[1:]
        sum = first + add_array(rest)
        return sum


#test empyt array
arr = []
print(add_array(arr))

#test array with int
arr = [1,2,3,4]
print(add_array(arr))

#test array with float
arr = [1.2,23,3.567,4]
print(add_array(arr))