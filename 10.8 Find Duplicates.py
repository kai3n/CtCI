
def findDuplicates(numberList):
    b = [False] * 32000
    for number in numberList:
        if b[number] == True:
            print(number)
        b[number] = True

findDuplicates([1,1,2,3,3,4,4,4,5,6,6])