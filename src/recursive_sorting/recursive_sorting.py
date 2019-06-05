# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # temporary list with 0 as placeholders
    merged_arr = [0] * elements
    # TO-DO
    # initialize index evaluators at 0
    j, k, l = 0, 0, 0
    # while both of the lists have not been icremented through
    while j < len(arrA) and k < len(arrB):
        if arrA[j] < arrB[k]:
            # replace placeholder with smaller item
            merged_arr[l] = arrA[j]
            # increment evaluation index on arrA and merged_arr
            l += 1
            j += 1
        else:
            # replace placeholder with smaller item
            merged_arr[l] = arrB[k]
            # increment evaluation index on arrB and merged_arr
            l += 1
            k += 1

    # Will only run if arrA has not been incremented through
    while j < len(arrA):
        merged_arr[l] = arrA[j]
        l += 1
        j += 1
    # Will only run if arrB has not been incremented through
    while k < len(arrB):
        merged_arr[l] = arrB[k]
        l += 1
        k += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    print('merge_sort called')
    if len(arr) > 1:
        print("array", arr)
        print("length", len(arr))
        mid = len(arr)//2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        arr = merge(left, right)
    return arr


# print(merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
# print(merge_sort([10, 1]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
