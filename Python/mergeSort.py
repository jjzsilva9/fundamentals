def mergeSort(array):
    mid = len(array)//2
    if len(array)%2 != 0:
        mid +=1
    left = array[:mid]
    right = array[mid:]
    if len(left) != 1:
        mergeSort(left)
    if len(right) != 1:
        mergeSort(right)
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        array[k] = right[j]
        j += 1
        k = k + 1
    print(array)
    return array

array = [42, 42214, 7, 4, 3, 9]
mergeSort(array)
