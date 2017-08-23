def sortedMerge(listA, listB):
    indexSort = len(listA) - 1
    indexA = len(listA) - len(listB) - 1
    indexB = len(listB) - 1

    while indexB >= 0:
        if listA[indexA] > listB[indexB]:
            listA[indexSort] = listA[indexA]
            indexA -= 1
        else:
            listA[indexSort] = listB[indexB]
            indexB -= 1
        indexSort -= 1


if __name__ == "__main__":
    listA = [1, 3, 5, 7, 9, 0, 0, 0, 0]
    listB = [2, 4, 6, 8]

    sortedMerge(listA, listB)
    print(listA)
