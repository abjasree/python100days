def separate(array, left, right):
    pointer1 = left - 1
    pivot = array[right]
    for pointer2 in range(left, right):
        if array[pointer2] <= pivot:
            pointer1 += 1
            array[pointer1], array[pointer2] = array[pointer2], array[pointer1]
    array[pointer1 + 1], array[right] = array[right], array[pointer1 + 1]
    return pointer1 + 1

def quicksort(array, left, right):
    if left < right: 
        separated = separate(array, left, right)
        quicksort(array, left, separated - 1)
        quicksort(array, separated + 1, right)
    return array





test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test, 0, len(test)-1))
