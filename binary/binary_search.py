
my_list = [1,2,3,4,5]
def binary_search(list,item):
    # The index of the first value in the list[]
    low = 0
    # The last index in the list
    high = len(list) - 1

    while low <= high:
        # Mid index of the list
        mid =(low + high) //2

       #The value of the middle index
        guess = list[mid]

        # Compare if the value gussed is equal to the item being searched
        if guess == item:
            return mid

        # Compare if value being searched is greate than the gussed value
        if guess > item:
            high = mid - 1

        else:
            low = mid + 1


    return None

print( "Index value:", binary_search(my_list,2))