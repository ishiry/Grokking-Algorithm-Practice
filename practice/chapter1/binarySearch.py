
#function for binary search
def binary_search (list,item):
    low = 0
    high = len(list) - 1

    #get step count
    step = 0


    while low <= high:
        mid = low + high
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        step = step + 1
    return None
