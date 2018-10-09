# this is my implementation of merge sort


def merge(array1, array2):
    ret_array = []

    i = 0  # array1 index tracker
    j = 0  # array2 index tracker

    while i != len(array1) and j != len(array2):
        if array1[i] <= array2[j]:
            ret_array.append(array1[i])
            i += 1
        else:
            ret_array.append(array2[j])
            j += 1

    if i == len(array1):
        for temp in array2[j:]:
            ret_array.append(temp)
    else:
        for temp in array1[i:]:
            ret_array.append(temp)

    return ret_array

def merge_sort(arry):

    if len(arry) == 1:
        return arry

    middle = int(len(arry)/2)

    temp1 = merge_sort(arry[:middle])
    temp2 = merge_sort(arry[middle:])

    return merge(temp1, temp2)


test = [1, 4, 67, 12, 54, 68, 1, 67, 100, 2, 5, 8, 7]
print(merge_sort(test))
