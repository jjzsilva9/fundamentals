def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    done = False
    while not done:
        while low <= high and array[low] <= pivot:
            low += 1
        while high >= low and array[high] >= pivot:
            high -= 1
        if high < low:
            if array[high] < pivot:
                array[high], array[start] = array[start], array[pivot]
        
    array[high], array[start] = array[start], array[high]
    return high
    

def quicksort(array, start, end):
    if start < end:
        split = partition(array, start, end)
        quicksort(array, start, split-1)
        quicksort(array, split+1, end)
    return array

test = [1, 7, 3, 78, 4]
print(quicksort(test, 0, len(test) - 1))   
