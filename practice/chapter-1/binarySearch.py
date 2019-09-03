
#function for binary search
def binary_search (list,item):
    low = 0
    high = len(list) - 1

    #get step count
    step = 0


    while low <= high:
        print(step)
        mid = low + high
        guess = list[mid]
        if guess == item:
            return print('number at index',mid)
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        step = step + 1
    return None

#comment
#its not sensitive to duplicates, as long as the list is in order
my_list = [1,2,3,4,5,6,7,8,9]

print(binary_search(my_list,5))