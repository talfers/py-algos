# binary search function
def binary_search(arr, val):
    start = 0
    end = len(arr) - 1
    mid = round((start + end) / 2)
    while arr[mid] != val and start <= end:
        if arr[mid] < val:
            start = mid + 1
        else:
            end = mid - 1
        mid = round((start + end) / 2)
    else:
        if arr[mid] == val:
            print(mid)
            return mid
        else:
            print(-1)
            return -1

# import test arr
from test_data import test_arr

# execute function
binary_search(test_arr, 55)
