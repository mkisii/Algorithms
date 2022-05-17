def binary_search(my_list,item):
    low = 0
    high = len(my_list) - 1

    while low <= high:

        mid = (low + high)
        guess = my_list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid- 1
        else:
            low = mid + 1

    return None

list = [1,2,3,4,5,6,7,8,9,10]

print( "Index Number:", binary_search(list,10))