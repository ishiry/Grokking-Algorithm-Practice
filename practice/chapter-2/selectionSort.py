# function for selection sort
# O(n) function runs n times,
# hence, max time complexity at O(n2)

from findSmallest import find_smallest


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print (selectionSort([1,2,3,4234,56,2]))


