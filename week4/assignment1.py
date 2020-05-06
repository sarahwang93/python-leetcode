def binarySearch(array1, item):
    start = 0
    end = len(array1)-1

    if len(array1) == 0:
        return -1

    while start < end:
        mid = int((start + end)//2)
        if array1[mid] < item:
            start = mid + 1
        elif array1[mid] > item:
            end = mid
        else:
            return mid
    return -1


if __name__ == "__main__":
    array1 = [1,5,8,12,13]
    array2 = [8,1,23,1,11]

    for j in array2:
        print(binarySearch(array1, j))