def peaksAndValleys(array):
    if len(array) < 3:
        return
    for ix in range(len(array)-1):
        # peak
        if ix % 2:
            if array[ix] < array[ix + 1]:
                array[ix], array[ix + 1] = array[ix + 1], array[ix]
        else:
            if array[ix] > array[ix + 1]:
                array[ix], array[ix + 1] = array[ix + 1], array[ix]
    return array
a = [12, 6, 3, 1, 0, 14, 13, 20, 22, 10]
print(peaksAndValleys(a))