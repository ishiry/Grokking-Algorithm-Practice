
#function for binary search
def binary_search (list,item):
    low = 0
    high = len(list) - 1


    while low <= high:
        print(low, high)
        mid = low + high
        guess = list[mid]
        print(guess)
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

#comment
#its not sensitive to duplicates, as long as the list is in order
my_list = [1,2,3,4,5,6,6,7,7,8]

print(binary_search(my_list,5))