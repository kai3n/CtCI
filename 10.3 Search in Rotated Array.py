def SearchInRotatedArray(myList, target):
    first, last = 0, len(myList) - 1

    while first <= last:
        mid = (first + last) // 2
        if myList[mid] == target:
            return mid
        if myList[mid] < myList[last]:
            if myList[mid] < target <= myList[last]:
                first = mid + 1
            else:
                last = mid - 1
        else:
            if myList[first] <= target < myList[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return -1


if __name__ == "__main__":
    myList = [50, 5, 20, 30, 40]
    print(SearchInRotatedArray(myList, 40))
