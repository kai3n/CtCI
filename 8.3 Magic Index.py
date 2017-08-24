def magicIndex(arr):
    first = 0
    last = len(arr)-1

    while first <= last:
        mid = (first+last)//2
        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:
            last = mid-1
        else:
            first = mid+1
    return False

print(magicIndex([1, 2, 2, 3, 6, 9, 15, 21]))

def magicIndex2(arr, min, max):
    mid = (min + max) // 2

    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return magicIndex2(arr, min, mid-1)
    else:
        return magicIndex2(arr, min+1, max)

print(magicIndex([1, 2, 2, 3, 6, 9, 15, 21]))