def insertionSort(list):
    for j in range(len(list)):
        nextItem = list[j]
        i = j-1
        while i >= 0 and list[i] > nextItem:
            list[i + 1] = list[i]
            i = i - 1
        list[i + 1] = nextItem
    print(list)


insertionList = [3, 2, 4, 5, 1]
insertionSort(insertionList)

