def bubblesort(list):
    for i in range(len(list) -1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

    print(list)



bubbleList = [5, 1, 3, 2, 4]
bubblesort(bubbleList)
