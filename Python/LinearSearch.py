def search(aList, target):
    targetFound = False
    #Stops searching if item found
    while not targetFound:
        #For each item in aList
        for i in aList:
            #Comparison
            if i == target:
                #Returns index and bool value
                targetFound = True
                print(str(target) + " found at index " + str(aList.index(i)))
                return True
        print("Item not in aList")
        return False

aList = ["foo", "bar", "bat"]
search(aList, "bat")

