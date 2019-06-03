# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    print('before sort', arr)
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index+1, len(arr)):
            if (arr[smallest_index] > arr[j]):
                smallest_index = j
        # TO-DO: swap

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    # print('after sort', arr)

    return arr


# selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])


def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
